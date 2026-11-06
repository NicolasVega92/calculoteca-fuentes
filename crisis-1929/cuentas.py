"""Cuentas del ángulo: cuatro personas hipotéticas que entran con 1.000 dólares en septiembre de 1929.

Usa la serie mensual de Robert Shiller (sp500_shiller.csv, sale de extraer_shiller.py). Cada precio es el promedio
del mes, no el cierre de un día, así que el máximo y el mínimo diarios fueron más extremos. Sin costos ni impuestos.
"""

import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "sp500_shiller.csv"
START = 1000.0
ENTRY = (1929, 9)
DOW_HIGH, DOW_LOW = 381.17, 41.22
DEPOSITS = (0.10, 0.40, 0.50)
SAVER_MONTHS = 96
# FDIC, A Brief History of Deposit Insurance, cap. 3, tabla 5: suspensiones, depósitos y pérdidas (miles de dólares).
SUSPENSIONS = {1930: (1350, 837096, 237359), 1931: (2293, 1690232, 390476), 1932: (1453, 706187, 168302), 1933: (4000, 3596708, 540396)}
# Federal Reserve History, Banking Panics of 1930-31: "over 8,000" miembros y "nearly 16,000" no miembros.
BANKS_BEFORE = 24000
# FRED, series GDPCA (anual) e INDPRO (mensual), leídas el 2026-11-02.
REAL_GDP = {1929: 1191.124, 1933: 877.431}
INDUSTRY = {"1929-07": 7.9436, "1932-07": 3.6891}


def months():
    with DATA.open(encoding="utf-8") as file:
        return [
            {"fecha": (int(row["anio"]), int(row["mes"])), "precio": float(row["precio"]), "dividendo": float(row["dividendo_anual"]), "ipc": float(row["ipc"])}
            for row in csv.DictReader(file)
        ]


def label(date):
    return f"{date[0]}-{date[1]:02d}"


def main():
    series = [month for month in months() if month["fecha"] >= ENTRY]
    entry = series[0]
    prices = {month["fecha"]: month["precio"] for month in series}

    # Aguanta: compra todo el primer mes y reinvierte cada dividendo.
    # De a poco: pone lo mismo repartido en 96 meses, también con dividendos reinvertidos.
    holder_shares = START / entry["precio"]
    saver_shares, paid = 0.0, 0.0
    path = []
    for index, month in enumerate(series):
        reinvest = 1 + month["dividendo"] / 12 / month["precio"]
        if index:
            holder_shares *= reinvest
            saver_shares *= reinvest
        if index < SAVER_MONTHS:
            saver_shares += START / SAVER_MONTHS / month["precio"]
            paid += START / SAVER_MONTHS
        deflator = entry["ipc"] / month["ipc"]
        path.append({
            "fecha": label(month["fecha"]),
            "precio_solo": round(START * month["precio"] / entry["precio"], 2),
            "aguanta": round(holder_shares * month["precio"], 2),
            "aguanta_real": round(holder_shares * month["precio"] * deflator, 2),
            "de_a_poco": round(saver_shares * month["precio"], 2),
            "de_a_poco_real": round(saver_shares * month["precio"] * deflator, 2),
            "aportado": round(paid, 2),
            "aguanta_veces_acciones": round(holder_shares * entry["precio"] / START, 2),
            "guardado_real": round(START * deflator, 2),
        })
    by_date = {point["fecha"]: point for point in path}

    # La pizarra dibuja estas curvas mes a mes (tools/pizarra.py, tipo "serie").
    with open(HERE / "trayectos.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["anio", "mes", "aguanta_real", "guardado_real"])
        for point in path:
            year, month = point["fecha"].split("-")
            writer.writerow([int(year), int(month), point["aguanta_real"], point["guardado_real"]])

    def back(key):
        """Primer mes en que recupera los 1.000, y primero desde el cual no vuelve a bajar de ahí."""
        first = next((point["fecha"] for point in path[1:] if point[key] >= START), None)
        last_below = max(index for index, point in enumerate(path) if point[key] < START)
        return {"primera_vez": first, "para_siempre": path[last_below + 1]["fecha"]}

    low = min(path, key=lambda point: point["precio_solo"])

    def saver_ahead():
        """Primer mes en que De a poco, ya con todo aportado, supera a Aguanta."""
        return [point for point in path if point["aportado"] >= START and point["de_a_poco"] > point["aguanta"]][0]["fecha"]

    credit = []
    for deposit in DEPOSITS:
        line = entry["precio"] * (1 - deposit)
        wiped = next((month for month in series if month["precio"] <= line), None)
        credit.append({
            "deposito_pct": deposit * 100,
            "compra_total": round(START / deposit, 2),
            "borra_con_caida_pct": deposit * 100,
            "primer_promedio_mensual_bajo_esa_linea": label(wiped["fecha"]) if wiped else None,
        })

    fechas = ("1929-11", "1932-06", "1932-12", "1935-04", "1936-11", "1936-12", "1937-03", "1938-03", "1945-01", "1945-12", "1948-09", "1949-07", "1954-09", "1954-12")
    months_all = {month["fecha"]: month for month in months()}
    leverage_gain = (START / 0.40 * prices[(1929, 9)] / months_all[(1929, 1)]["precio"] - START / 0.40 + START) / START - 1
    cheapest = min((month for month in series if month["fecha"] <= (1934, 12)), key=lambda month: month["ipc"])
    total_suspended = sum(row[0] for row in SUSPENSIONS.values())
    total_deposits = sum(row[1] for row in SUSPENSIONS.values())
    total_losses = sum(row[2] for row in SUSPENSIONS.values())
    result = {
        "dow_caida_pct": round((DOW_HIGH - DOW_LOW) / DOW_HIGH * 100, 1),
        "indice_mensual_caida_pct": round((entry["precio"] - low["precio_solo"] / START * entry["precio"]) / entry["precio"] * 100, 1),
        "mes_mas_bajo": low["fecha"],
        "vuelve_solo_precio": back("precio_solo"),
        "vuelve_aguanta": back("aguanta"),
        "vuelve_aguanta_real": back("aguanta_real"),
        "de_a_poco_supera_lo_aportado": path[max(index for index, point in enumerate(path) if point["de_a_poco"] < point["aportado"]) + 1]["fecha"],
        "rebote_1933_pct": round((prices[(1933, 12)] / prices[(1932, 12)] - 1) * 100, 1),
        "de_a_poco_supera_a_aguanta": saver_ahead(),
        "por_fecha": {date: by_date[date] for date in fechas},
        "con_credito": credit,
        "aporte_mensual": round(START / SAVER_MONTHS, 2),
        "indice_suba_1927_a_sep_1929_pct": round((prices[(1929, 9)] / months_all[(1927, 1)]["precio"] - 1) * 100, 1),
        "indice_suba_ene_a_sep_1929_pct": round((prices[(1929, 9)] / months_all[(1929, 1)]["precio"] - 1) * 100, 1),
        "ganancia_con_40_pct_de_deposito_ene_a_sep_1929_pct": round(leverage_gain * 100, 1),
        "con_credito_si_cae_a_la_mitad": {"acciones": START / 0.40 / 2, "deuda": START / 0.40 - START},
        "precios_caida_pct": round((1 - cheapest["ipc"] / entry["ipc"]) * 100, 1),
        "precios_mes_mas_bajo": label(cheapest["fecha"]),
        "precios_suba_dic_1945_a_sep_1948_pct": round((months_all[(1948, 9)]["ipc"] / months_all[(1945, 12)]["ipc"] - 1) * 100, 1),
        "indice_caida_mar_1937_a_mar_1938_pct": round((1 - prices[(1938, 3)] / prices[(1937, 3)]) * 100, 1),
        "rendimiento_dividendo_jun_1932_pct": round(months_all[(1932, 6)]["dividendo"] / prices[(1932, 6)] * 100, 1),
        "indice_rebote_nov_1929_a_abr_1930_pct": round((prices[(1930, 4)] / prices[(1929, 11)] - 1) * 100, 1),
        "indice_abr_1930_contra_entrada_pct": round((prices[(1930, 4)] / entry["precio"] - 1) * 100, 1),
        "dividendo_dic_1929_a_jun_1932_caida_pct": round((1 - months_all[(1932, 6)]["dividendo"] / months_all[(1929, 12)]["dividendo"]) * 100, 1),
        "compra_de_a_poco_jun_1932_contra_sep_1929_veces": round(prices[(1929, 9)] / prices[(1932, 6)], 1),
        "deuda_mas_ventas_con_precios_bajos_pct": round((entry["ipc"] / cheapest["ipc"] - 1) * 100, 1),
        "precios_nov_1936_contra_entrada_pct": round((months_all[(1936, 11)]["ipc"] / entry["ipc"] - 1) * 100, 1),
        "meses_aguanta_real_bajo_1000_desde_1945": [point["fecha"] for point in path if "1945-01" <= point["fecha"] and point["aguanta_real"] < START],
        "rendimiento_dividendo_sep_1929_pct": round(entry["dividendo"] / entry["precio"] * 100, 1),
        # Lo guardado sin invertir: 1.000 dólares que no ganan nada y que no se perdieron en un banco cerrado.
        "guardado": {
            "mejor_mes": max(path, key=lambda point: point["guardado_real"])["fecha"],
            "mejor_real": max(point["guardado_real"] for point in path),
            "por_debajo_de_1000_desde": path[max(index for index, point in enumerate(path) if point["guardado_real"] >= START) + 1]["fecha"],
            "real_por_fecha": {date: by_date[date]["guardado_real"] for date in ("1933-03", "1945-01", "1954-09")},
            "aguanta_real_lo_supera_para_siempre": path[max(index for index, point in enumerate(path) if point["aguanta_real"] < point["guardado_real"]) + 1]["fecha"],
        },
        "aguanta_sep_1954_contra_lo_que_vendio_vende_abajo_veces": round(by_date["1954-09"]["aguanta"] / by_date["1932-12"]["aguanta"], 1),
        "producto_caida_pct": round((1 - REAL_GDP[1933] / REAL_GDP[1929]) * 100, 1),
        "industria_caida_pct": round((1 - INDUSTRY["1932-07"] / INDUSTRY["1929-07"]) * 100, 1),
        "bancos": {
            "suspensiones_1930_33": total_suspended,
            "parte_de_los_bancos_pct": round(total_suspended / BANKS_BEFORE * 100, 1),
            "depositos_miles": total_deposits,
            "perdidas_miles": total_losses,
            "perdida_por_dolar_pct": round(total_losses / total_deposits * 100, 1),
        },
    }
    (HERE / "cuentas.json").write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
