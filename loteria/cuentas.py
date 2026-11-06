"""Cuentas del video 2: ¿ganar la lotería te arruina?

Sigue el dinero de los boletos, no a personas. Todo sale de los archivos de esta carpeta:

- navidad_2026_programa_premios.csv: programa de premios por serie del Sorteo de Navidad del 22 de diciembre de 2026
  (SELAE, aprobado el 26 de enero de 2026), transcripto del PDF oficial el 2026-11-05.
- powerball_sorteos_descargado_2026-11-05.csv: pozo anunciado, valor de contado y ganadores de cada categoría de los
  289 sorteos de Powerball del 2025-01-01 al 2026-11-04, leídos de powerball.com el 2026-11-05.
- powerball_sorteo_2022-11-07_descargado_2026-11-05.csv: el sorteo del pozo récord (7 de noviembre de 2022), leído de
  powerball.com el 2026-11-05, con los ganadores con y sin Power Play sumados. Se calcula aparte de los 243 sorteos.
- florida_tabla1.csv: tabla 1 de Hankins, Hoekstra y Skiba (2011).

Los supuestos de cada cuenta están escritos junto a ella. Sin costos de viaje ni de cobro.
"""

import csv
import json
import math
import random
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent

# --- Datos fijos, con su fuente (ver fuentes.md) ---------------------------------------------------------------

# Powerball: 5 de 69 y 1 de 26, a 2 dólares (powerball.com, tabla de premios y preguntas frecuentes, 2026-11-05).
PB_WHITE, PB_PICK, PB_RED, PB_PRICE = 69, 5, 26, 2.0
# Premios fijos sin Power Play: (aciertos blancos, acierta la roja, premio).
PB_FIXED = [(5, False, 1_000_000), (4, True, 50_000), (4, False, 100), (3, True, 100), (3, False, 7),
            (2, True, 7), (1, True, 4), (0, True, 4)]
PB_OFFICIAL_ODDS = {"5+1": 292_201_338.00, "5": 11_688_053.52, "4+1": 913_129.18, "4": 36_525.17, "3+1": 14_494.11,
                    "3": 579.76, "2+1": 701.33, "1+1": 91.98, "0+1": 38.32, "cualquiera": 24.87}
# Orden de las columnas de ganadores del CSV, de la categoría más alta a la más baja.
PB_TIERS = ["5+1", "5", "4+1", "4", "3+1", "3", "2+1", "1+1", "0+1"]
# Regla estatal de Oregón (OAR 177-085-0025): 50 % de las ventas a premios; el pozo mayor recibe como máximo 34,0066 %.
PB_PRIZE_POOL, PB_JACKPOT_POOL_MAX = 0.50, 0.340066
# Cuotas: 30 pagos que suben 5 % por año, el primero inmediato (powerball.com, preguntas frecuentes).
PB_PAYMENTS, PB_GROWTH = 30, 0.05
# Desde el 22 de julio de 2026 el pozo se comparte con el Reino Unido, cuyos ganadores no figuran en las categorías
# menores de esta tabla. Para estimar boletos vendidos solo se usan los sorteos anteriores.
PB_LAST_US_ONLY = "2026-07-20"

# EE. UU., impuesto federal 2026 para una persona sola (IRS, formulario 1040-ES 2026, Schedule X):
# (desde, tasa). Retención de 24 % al cobrar premios grandes (IRS, instrucciones del W-2G).
US_BRACKETS = [(0, 0.10), (12_400, 0.12), (50_400, 0.22), (105_700, 0.24), (201_775, 0.32), (256_225, 0.35),
               (640_600, 0.37)]
US_WITHHOLDING = 0.24
# Supuesto que favorece al boleto: sin impuesto estatal (varía de un estado a otro) y premios fijos sin impuestos.

# Sorteo de Navidad 2026 (SELAE): 205 series de 100.000 billetes a 200 euros, décimos de 20 euros, 70 % a premios.
NAV_SERIES, NAV_NUMBERS, NAV_BILLETE, NAV_DECIMOS = 205, 100_000, 200, 10
NAV_PRIZE_SHARE = 0.70
# Gravamen especial (Agencia Tributaria): 20 % sobre lo que pasa de 40.000 euros, por décimo.
ES_TAX, ES_EXEMPT = 0.20, 40_000

# Otros juegos, para comparar probabilidades: Melate (México, 6 de 56, 15 pesos, pronosticos.gob.mx)
# y Baloto (Colombia, 5 de 43 y 1 de 16, 6.000 pesos, baloto.com).
MELATE = {"numeros": 56, "elige": 6, "precio": 15, "moneda": "MXN"}
BALOTO = {"numeros": 43, "elige": 5, "super": 16, "precio": 6_000, "moneda": "COP"}
# Quini 6 (Argentina, Lotería de Santa Fe, preguntas frecuentes, leídas el 2026-11-05): 6 números de un total de 46,
# del 00 al 45; el Tradicional (primer sorteo y La Segunda) paga 6, 5 y 4 aciertos; 2.000 pesos el Tradicional.
# Cada sorteo extrae 6 números: "18 extracciones" entre los dos sorteos del Tradicional y la Revancha.
QUINI6 = {"numeros": 46, "elige": 6, "precio": 2_000, "moneda": "ARS"}
# Loto de Chile (Polla Chilena de Beneficencia): no entra. Su sitio oficial rechazó la lectura el 2026-11-05 y las
# reglas solo se vieron en la prensa (ver fuentes.md, "Revisar").

# Canadá (Agarwal, Mikhed y Scholnick, documento de trabajo 18-22 de la Fed de Filadelfia, 2018): por código postal,
# con una mediana de 13 hogares, 0,455 quiebras de vecinos en los 3 años siguientes al premio en promedio;
# +0,03 con un premio igual al ingreso mediano (29.229 dólares canadienses) y +0,052 con uno de 100.000.
CANADA = {"base_0_2": 0.455, "mas_con_mediana": 0.03, "mas_con_100000": 0.052, "ingreso_mediano": 29_229,
          "hogares_por_codigo": 13}

# Meta de inflación de la Reserva Federal: 2 % anual (federalreserve.gov). Solo para expresar cuotas en poder de compra.
INFLATION = 0.02
SEED = 2026


def one_in(probability):
    return round(1 / probability, 2) if probability else None


def us_federal_tax(amount):
    tax = 0.0
    for index, (start, rate) in enumerate(US_BRACKETS):
        end = US_BRACKETS[index + 1][0] if index + 1 < len(US_BRACKETS) else math.inf
        if amount > start:
            tax += (min(amount, end) - start) * rate
    return tax


def spain_tax(per_decimo):
    return max(0.0, per_decimo - ES_EXEMPT) * ES_TAX


# --- Probabilidades por combinatoria ---------------------------------------------------------------------------

def powerball_odds():
    whites = comb(PB_WHITE, PB_PICK)
    rows = {}
    for k in range(PB_PICK, -1, -1):
        ways = comb(PB_PICK, k) * comb(PB_WHITE - PB_PICK, PB_PICK - k)
        for red in (True, False):
            p = ways / whites * (1 / PB_RED if red else (PB_RED - 1) / PB_RED)
            rows[f"{k}+1" if red else f"{k}"] = p
    tiers = {key: rows[key] for key in PB_TIERS}
    any_prize = sum(tiers.values())
    fixed_ev = sum(rows[f"{w}+1" if r else f"{w}"] * prize for w, r, prize in PB_FIXED)
    return {
        "combinaciones": whites * PB_RED,
        "combinaciones_blancas": whites,  # Paso intermedio para la pizarra: 69 tomados de a 5, antes de la roja.
        "por_categoria_1_en": {key: one_in(p) for key, p in tiers.items()},
        "coincide_con_tabla_oficial": all(abs(one_in(p) - PB_OFFICIAL_ODDS[key]) < 0.01 for key, p in tiers.items())
        and abs(round(1 / any_prize, 2) - PB_OFFICIAL_ODDS["cualquiera"]) < 0.01,
        "cualquier_premio_1_en": one_in(any_prize),
        "premios_fijos_valor_esperado": round(fixed_ev, 4),
        "premios_fijos_pct_del_boleto": round(fixed_ev / PB_PRICE * 100, 2),
        "_p": tiers,
    }


def boletos_para(probability, chance):
    """Boletos distintos sorteo a sorteo para tener esa probabilidad de ganar al menos una vez."""
    return math.log(1 - chance) / math.log(1 - probability)


# --- Sorteo de Navidad -----------------------------------------------------------------------------------------

def navidad_program():
    with (HERE / "navidad_2026_programa_premios.csv").open(encoding="utf-8") as file:
        return [{"premio": r["premio"], "cantidad": int(r["cantidad_por_serie"]), "billete": int(r["euros_por_billete"])}
                for r in csv.DictReader(file)]


def navidad():
    program = navidad_program()
    serie_value = NAV_NUMBERS * NAV_BILLETE
    prizes = sum(row["cantidad"] * row["billete"] for row in program)
    emission = NAV_SERIES * serie_value
    count = sum(row["cantidad"] for row in program)
    # Recorrido de 100 euros: a qué va cada parte, en promedio.
    flow = {}
    tax_total = 0.0
    for row in program:
        decimo = row["billete"] / NAV_DECIMOS
        tax = spain_tax(decimo) * NAV_DECIMOS * row["cantidad"]
        tax_total += tax
        flow[row["premio"]] = round(row["cantidad"] * row["billete"] / serie_value * 100, 3)
    groups = {
        "primero": ["primero"], "segundo_y_tercero": ["segundo", "tercero"], "cuartos_y_quintos": ["cuarto", "quinto"],
        "pedrea": ["pedrea"], "aproximaciones_y_centenas": [r["premio"] for r in program if r["premio"].startswith(("aprox", "centena"))],
        "dos_ultimas_cifras": [r["premio"] for r in program if r["premio"].startswith("dos_cifras")], "reintegro": ["reintegro"],
    }
    por_100 = {name: round(sum(flow[key] for key in keys), 2) for name, keys in groups.items()}
    por_100["impuesto_a_premios_grandes"] = round(-tax_total / serie_value * 100, 2)
    net = (prizes - tax_total) / serie_value
    # Lo que cobra un décimo de cada premio, antes y después del gravamen.
    decimo = {row["premio"]: {"bruto": row["billete"] / NAV_DECIMOS,
                              "neto": row["billete"] / NAV_DECIMOS - spain_tax(row["billete"] / NAV_DECIMOS)}
              for row in program if row["premio"] in ("primero", "segundo", "tercero", "cuarto", "quinto", "pedrea", "reintegro")}
    # Comprar un décimo de cada uno de los 100.000 números: el primer premio es seguro.
    all_cost = NAV_NUMBERS * NAV_BILLETE / NAV_DECIMOS
    all_back_gross = prizes / NAV_DECIMOS
    all_back_net = (prizes - tax_total) / NAV_DECIMOS
    return {
        "emision_euros": emission, "premios_euros": emission * NAV_PRIZE_SHARE,
        "premios_por_serie": prizes, "premios_por_serie_coincide_70_pct": prizes == serie_value * NAV_PRIZE_SHARE,
        "premios_por_serie_cantidad": count,
        "decimo_euros": NAV_BILLETE / NAV_DECIMOS,
        "probabilidad_primero_1_en": NAV_NUMBERS,
        "probabilidad_algun_premio_pct": round(count / NAV_NUMBERS * 100, 2),
        "de_cada_100_premios_son_reintegro": round(9_999 / count * 100, 1),
        "recorrido_100_euros": {"gestion_y_tesoro": round((1 - NAV_PRIZE_SHARE) * 100, 2), **por_100,
                                "vuelve_en_premios_neto": round(net * 100, 2)},
        "valor_esperado_decimo_neto": round(net * NAV_BILLETE / NAV_DECIMOS, 2),
        "impuesto_por_serie": tax_total,
        "un_decimo_por_premio": decimo,
        "comprar_todos_los_numeros": {"cuesta": all_cost, "vuelve_bruto": all_back_gross, "vuelve_neto": all_back_net,
                                      "pierde_neto": all_cost - all_back_net},
        "decimos_para_50_pct_de_ganar_el_primero_en_anios_distintos": round(boletos_para(1 / NAV_NUMBERS, 0.5)),
    }


def navidad_simulated(draws=200):
    """Reparte los premios al azar sobre los 100.000 números, como el sorteo, y cuenta lo que cobra cada número.

    Supuesto: los premios son compatibles entre sí y se suman, como en el programa. Mide cuántos números
    no cobran nada, cuántos solo recuperan el décimo y cuántos ganan más de lo que costó.
    """
    rng = random.Random(SEED)
    program = {row["premio"]: row for row in navidad_program()}
    totals = {"nada": 0, "solo_reintegro": 0, "mas_que_el_decimo": 0}
    for _ in range(draws):
        numbers = rng.sample(range(NAV_NUMBERS), 1 + 1 + 1 + 2 + 8 + 1794)
        first, second, third = numbers[0], numbers[1], numbers[2]
        fourths, fifths, pedrea = numbers[3:5], numbers[5:13], numbers[13:]
        pay = {}

        def add(number, amount):
            pay[number] = pay.get(number, 0) + amount

        add(first, program["primero"]["billete"])
        add(second, program["segundo"]["billete"])
        add(third, program["tercero"]["billete"])
        for n in fourths:
            add(n, program["cuarto"]["billete"])
        for n in fifths:
            add(n, program["quinto"]["billete"])
        for n in pedrea:
            add(n, program["pedrea"]["billete"])
        for prize, key in ((first, "aproximacion_primero"), (second, "aproximacion_segundo"), (third, "aproximacion_tercero")):
            for n in ((prize - 1) % NAV_NUMBERS, (prize + 1) % NAV_NUMBERS):
                add(n, program[key]["billete"])
        for prize, key in ((first, "centena_primero"), (second, "centena_segundo"), (third, "centena_tercero"),
                           (fourths[0], "centena_cuartos"), (fourths[1], "centena_cuartos")):
            base = prize // 100 * 100
            for n in range(base, base + 100):
                if n != prize:
                    add(n, program[key]["billete"])
        for prize, key in ((first, "dos_cifras_primero"), (second, "dos_cifras_segundo"), (third, "dos_cifras_tercero")):
            for n in range(prize % 100, NAV_NUMBERS, 100):
                if n != prize:
                    add(n, program[key]["billete"])
        for n in range(first % 10, NAV_NUMBERS, 10):
            if n != first:
                add(n, program["reintegro"]["billete"])
        for amount in pay.values():
            if amount == NAV_BILLETE:
                totals["solo_reintegro"] += 1
            elif amount > NAV_BILLETE:
                totals["mas_que_el_decimo"] += 1
        totals["nada"] += NAV_NUMBERS - len(pay)
    return {key: round(value / draws / NAV_NUMBERS * 100, 2) for key, value in totals.items()} | {"sorteos_simulados": draws}


# --- Powerball según el pozo -----------------------------------------------------------------------------------

def powerball_draws(name="powerball_sorteos_descargado_2026-11-05.csv"):
    with (HERE / name).open(encoding="utf-8") as file:
        rows = []
        for r in csv.DictReader(file):
            winners = [int(r[key]) for key in ("ganadores_pozo", "ganadores_5", "ganadores_4_pb", "ganadores_4",
                                               "ganadores_3_pb", "ganadores_3", "ganadores_2_pb", "ganadores_1_pb",
                                               "ganadores_solo_pb")]
            rows.append({"fecha": r["fecha"], "anunciado": float(r["pozo_anunciado_millones"]) * 1e6,
                         "contado": float(r["valor_contado_millones"]) * 1e6, "ganadores": dict(zip(PB_TIERS, winners))})
        return rows


def tickets_sold(draw, p):
    """Estimación de jugadas vendidas: ganadores de las categorías menores sobre su probabilidad (máxima verosimilitud
    de Poisson con un mismo número de jugadas). No usa el pozo mayor."""
    lower = PB_TIERS[1:]
    return sum(draw["ganadores"][key] for key in lower) / sum(p[key] for key in lower)


def ticket_value(draw, p, fixed_ev, tickets):
    jackpot_p = p["5+1"]
    naive = draw["anunciado"] * jackpot_p + fixed_ev
    cash = draw["contado"] * jackpot_p + fixed_ev
    after_tax_jackpot = draw["contado"] - us_federal_tax(draw["contado"])
    after_tax = after_tax_jackpot * jackpot_p + fixed_ev
    # Otros ganadores del mismo sorteo: Poisson con media = otras jugadas por la probabilidad.
    lam = tickets * jackpot_p
    share = (1 - math.exp(-lam)) / lam if lam else 1.0
    shared = after_tax_jackpot * share * jackpot_p + fixed_ev
    return {"anunciado": naive, "contado": cash, "con_impuesto": after_tax, "compartido": shared,
            "parte_esperada_del_pozo": share, "otros_ganadores_esperados": lam}


def powerball(p, fixed_ev):
    draws = powerball_draws()
    us_only = [d for d in draws if d["fecha"] <= PB_LAST_US_ONLY]
    table = []
    for draw in us_only:
        n = tickets_sold(draw, p)
        value = ticket_value(draw, p, fixed_ev, n)
        table.append({"fecha": draw["fecha"], "anunciado_millones": draw["anunciado"] / 1e6,
                      "contado_millones": draw["contado"] / 1e6, "jugadas_estimadas_millones": round(n / 1e6, 2),
                      "ganadores_pozo": draw["ganadores"]["5+1"],
                      **{f"valor_{k}": round(v, 3) for k, v in value.items()}})

    # Aporte al pozo: cuánto sube el valor de contado entre sorteos sin ganador, sobre lo vendido.
    growth, sales = 0.0, 0.0
    for before, after in zip(us_only, us_only[1:]):
        if before["ganadores"]["5+1"] == 0 and after["fecha"] <= PB_LAST_US_ONLY:
            growth += after["contado"] - before["contado"]
            sales += tickets_sold(after, p) * PB_PRICE

    by_jackpot = sorted(table, key=lambda row: row["anunciado_millones"])
    best = max(table, key=lambda row: row["valor_compartido"])
    smallest = by_jackpot[0]
    biggest = by_jackpot[-1]
    median = by_jackpot[len(by_jackpot) // 2]
    expected_winners = sum(row["valor_otros_ganadores_esperados"] for row in table)
    actual_winners = sum(row["ganadores_pozo"] for row in table)

    # Comprar todas las combinaciones en el sorteo del pozo más grande.
    all_cost = comb(PB_WHITE, PB_PICK) * PB_RED * PB_PRICE
    fixed_all = fixed_ev * comb(PB_WHITE, PB_PICK) * PB_RED
    big = next(d for d in us_only if d["fecha"] == biggest["fecha"])
    jackpot_net = big["contado"] - us_federal_tax(big["contado"])
    # Misma parte esperada del pozo que el boleto suelto: con K otros ganadores Poisson(λ), E[1/(1+K)] = (1 − e^−λ)/λ.
    share = ticket_value(big, p, fixed_ev, tickets_sold(big, p))["parte_esperada_del_pozo"]
    buy_all = {"fecha": biggest["fecha"], "cuesta": all_cost, "premios_fijos": round(fixed_all),
               "pozo_neto_si_no_hay_otro": round(jackpot_net),
               "parte_esperada_del_pozo": round(share, 4),
               "pozo_neto_esperado": round(jackpot_net * share),
               "resultado_esperado": round(fixed_all + jackpot_net * share - all_cost)}
    # Sin compartir, a qué valor de contado (antes de impuestos) un boleto vale lo que cuesta.
    low, high = 1e6, 1e11
    for _ in range(100):
        mid = (low + high) / 2
        if (mid - us_federal_tax(mid)) * p["5+1"] + fixed_ev < PB_PRICE:
            low = mid
        else:
            high = mid
    most_tickets = max(table, key=lambda row: row["jugadas_estimadas_millones"])
    buckets = []
    for low_m, high_m in ((0, 100), (100, 300), (300, 600), (600, 1000), (1000, 2000)):
        rows = [row for row in table if low_m <= row["anunciado_millones"] < high_m]
        tickets = sorted(row["jugadas_estimadas_millones"] for row in rows)
        buckets.append({"pozo_anunciado_millones": f"{low_m}-{high_m}", "sorteos": len(rows),
                        "jugadas_mediana_millones": tickets[len(tickets) // 2],
                        "valor_min": min(row["valor_compartido"] for row in rows),
                        "valor_max": max(row["valor_compartido"] for row in rows)})
    return {
        "sorteos_usados": len(table), "desde": table[0]["fecha"], "hasta": table[-1]["fecha"],
        "por_tamano_del_pozo": buckets, "mas_jugadas": most_tickets,
        "jugadas_estimadas_millones": {"pozo_mas_chico": smallest["jugadas_estimadas_millones"],
                                       "mediana": median["jugadas_estimadas_millones"],
                                       "pozo_mas_grande": biggest["jugadas_estimadas_millones"]},
        "aporte_al_pozo_pct_de_ventas": round(growth / sales * 100, 1) if sales else None,
        "aporte_maximo_por_regla_pct": PB_JACKPOT_POOL_MAX * 100,
        "ganadores_del_pozo_esperados_y_reales": [round(expected_winners, 1), actual_winners],
        "pozo_mas_chico": smallest, "pozo_mediano": median, "pozo_mas_grande": biggest, "mejor_valor": best,
        "algun_sorteo_vale_lo_que_cuesta": any(row["valor_compartido"] >= PB_PRICE for row in table),
        "contado_para_que_valga_2_sin_compartir_millones": round(high / 1e6, 1),
        "comprar_todas_las_combinaciones": buy_all,
        "_tabla": table,
    }


def powerball_record(p, fixed_ev):
    """El pozo récord, 7 de noviembre de 2022: fuera de los 243 sorteos, con el mismo método de jugadas y de valor.
    Usa el impuesto federal de 2026, igual que los demás sorteos, para que la comparación sea con la misma base."""
    draw = powerball_draws("powerball_sorteo_2022-11-07_descargado_2026-11-05.csv")[0]
    n = tickets_sold(draw, p)
    value = ticket_value(draw, p, fixed_ev, n)
    return {"fecha": draw["fecha"], "anunciado_millones": draw["anunciado"] / 1e6,
            "contado_millones": draw["contado"] / 1e6, "jugadas_estimadas_millones": round(n / 1e6, 2),
            "ganadores_pozo": draw["ganadores"]["5+1"], **{f"valor_{k}": round(v, 3) for k, v in value.items()},
            "vale_lo_que_cuesta": value["compartido"] >= PB_PRICE}


def powerball_after_tax(fixed_pct, jackpot_pct):
    """De cada 100 dólares, cuánto vuelve después del impuesto federal de 2026, con los supuestos del boleto:
    premios fijos sin impuestos y sin impuesto estatal. La parte del pozo se reduce con la tasa efectiva que pagaron
    los pozos ganados en los 243 sorteos, cada ganador por su parte del contado."""
    draws = [d for d in powerball_draws() if d["fecha"] <= PB_LAST_US_ONLY and d["ganadores"]["5+1"] > 0]
    gross = sum(d["contado"] for d in draws)
    net = 0.0
    for d in draws:
        each = d["contado"] / d["ganadores"]["5+1"]
        net += (each - us_federal_tax(each)) * d["ganadores"]["5+1"]
    rate = 1 - net / gross
    return {"pozos_ganados": len(draws), "tasa_efectiva_del_pozo_pct": round(rate * 100, 2),
            "premios_fijos": fixed_pct, "pozo_despues_de_impuesto": round(jackpot_pct * (1 - rate), 2),
            "vuelve_despues_de_impuesto_federal": round(fixed_pct + jackpot_pct * (1 - rate), 2)}


def annuity(jackpot, cash):
    first = jackpot * PB_GROWTH / ((1 + PB_GROWTH) ** PB_PAYMENTS - 1)
    payments = [first * (1 + PB_GROWTH) ** t for t in range(PB_PAYMENTS)]
    low, high = 0.0, 0.5
    for _ in range(200):
        r = (low + high) / 2
        present = sum(x / (1 + r) ** t for t, x in enumerate(payments))
        low, high = (r, high) if present > cash else (low, r)
    real = sum(x / (1 + INFLATION) ** t for t, x in enumerate(payments))
    return {"anunciado": jackpot, "contado": cash, "contado_pct_del_anunciado": round(cash / jackpot * 100, 1),
            "primer_pago": round(first), "ultimo_pago": round(payments[-1]),
            "ultimo_pago_en_poder_de_compra_de_hoy": round(payments[-1] / (1 + INFLATION) ** (PB_PAYMENTS - 1)),
            "suma_de_cuotas_en_poder_de_compra_de_hoy": round(real),
            "interes_implicito_pct": round(low * 100, 2),
            "impuesto_federal_si_cobra_todo_junto": round(us_federal_tax(cash)),
            "impuesto_federal_de_la_primera_cuota": round(us_federal_tax(first)),
            "retencion_al_cobrar": round(cash * US_WITHHOLDING)}


# --- Lo que midieron los estudios ------------------------------------------------------------------------------

def florida():
    with (HERE / "florida_tabla1.csv").open(encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    big = ("50000_a_100000", "100000_a_150000")
    small = ("menos_de_1000", "1000_a_10000")

    def rate(window, groups=None):
        sel = [r for r in rows if r["ventana"] == window and (groups is None or r["monto_ganado"] in groups)]
        yes = sum(int(r["con_quiebra"]) for r in sel)
        total = yes + sum(int(r["sin_quiebra"]) for r in sel)
        return {"quiebras": yes, "ganadores": total, "pct": round(yes / total * 100, 2)}

    return {"todos_0_a_5": rate("0_a_5"),
            "grandes_0_a_2": rate("0_a_2", big), "chicos_0_a_2": rate("0_a_2", small),
            "grandes_3_a_5": rate("3_a_5", big), "chicos_3_a_5": rate("3_a_5", small),
            "grandes_0_a_5": rate("0_a_5", big), "chicos_0_a_5": rate("0_a_5", small),
            "mito_70_pct_sobre_los_mismos_ganadores": round(0.70 * rate("0_a_5")["ganadores"])}


def canada():
    base = CANADA["base_0_2"]
    return {"aumento_pct_con_mediana": round(CANADA["mas_con_mediana"] / base * 100, 1),
            "aumento_pct_con_100000": round(CANADA["mas_con_100000"] / base * 100, 1),
            # 0,455 es el promedio en los códigos postales de los ganadores (años 0 a 2), no en barrios sin premio.
            "por_cada_1000_barrios": {"quiebras_promedio_en_barrios_de_ganadores": round(base * 1000),
                                      "mas_con_premio_mediano": round(CANADA["mas_con_mediana"] * 1000),
                                      "mas_con_premio_de_100000": round(CANADA["mas_con_100000"] * 1000)},
            "hogares_por_barrio": CANADA["hogares_por_codigo"]}


def main():
    pb = powerball_odds()
    p = pb.pop("_p")
    melate = comb(MELATE["numeros"], MELATE["elige"])
    baloto = comb(BALOTO["numeros"], BALOTO["elige"]) * BALOTO["super"]
    quini6 = comb(QUINI6["numeros"], QUINI6["elige"])
    pb_draws = powerball(p, pb["premios_fijos_valor_esperado"])
    table = pb_draws.pop("_tabla")
    last = powerball_draws()[-1]
    with open(HERE / "powerball_valor_por_sorteo.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(table[0]))
        writer.writeheader()
        writer.writerows(table)

    result = {
        "probabilidades": {
            "powerball": pb,
            # En un solo sorteo, con combinaciones distintas, la chance es n / 292.201.338: la mitad pide la mitad.
            # (Corregido el 2026-11-05: antes usaba la fórmula de boletos en sorteos distintos.)
            "powerball_jugadas_para_50_pct": math.ceil(pb["combinaciones"] / 2),
            "powerball_dolares_para_50_pct": math.ceil(pb["combinaciones"] / 2) * PB_PRICE,
            "powerball_anios_jugando_3_por_semana": round(1 / p["5+1"] / (3 * 52)),
            "navidad_primero_1_en": NAV_NUMBERS,
            "melate_1_en": melate, "baloto_1_en": baloto,
            "veces_mas_dificil_que_navidad": {"powerball": round(1 / p["5+1"] / NAV_NUMBERS),
                                              "melate": round(melate / NAV_NUMBERS),
                                              "baloto": round(baloto / NAV_NUMBERS)},
            # Añadidos el 2026-11-05 por decisión del dueño: Argentina entra solo en la comparación de probabilidades.
            "quini6_1_en_por_sorteo": quini6,
            "quini6_veces_mas_dificil_que_navidad": round(quini6 / NAV_NUMBERS),
            "powerball_veces_mas_dificil_que_quini6": round(1 / p["5+1"] / quini6),
        },
        "navidad": navidad(),
        "navidad_simulada_pct_de_decimos": navidad_simulated(),
        "powerball_recorrido_100": {"premios": PB_PRIZE_POOL * 100,
                                    "premios_fijos": pb["premios_fijos_pct_del_boleto"],
                                    "pozo_mayor": round(PB_PRIZE_POOL * 100 - pb["premios_fijos_pct_del_boleto"], 2),
                                    "loterias_estatales_y_costos": (1 - PB_PRIZE_POOL) * 100},
        "powerball_recorrido_100_despues_de_impuesto_federal": powerball_after_tax(
            pb["premios_fijos_pct_del_boleto"], round(PB_PRIZE_POOL * 100 - pb["premios_fijos_pct_del_boleto"], 2)),
        "powerball_por_sorteo": pb_draws,
        "powerball_pozo_record_2022": powerball_record(p, pb["premios_fijos_valor_esperado"]),
        "pago_unico_contra_cuotas": {
            "ultimo_sorteo": {"fecha": last["fecha"], **annuity(last["anunciado"], last["contado"])},
            "pozo_mas_grande": {"fecha": pb_draws["pozo_mas_grande"]["fecha"],
                                **annuity(pb_draws["pozo_mas_grande"]["anunciado_millones"] * 1e6,
                                          pb_draws["pozo_mas_grande"]["contado_millones"] * 1e6)},
            "supuestos": "Cuotas que suben 5 % por año, la primera inmediata; impuesto federal 2026 de una persona sola; "
                         "sin impuesto estatal; inflación de 2 % por año, la meta de la Reserva Federal.",
        },
        "florida": florida(),
        "canada": canada(),
    }
    (HERE / "cuentas.json").write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
