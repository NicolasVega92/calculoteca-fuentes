# Fuentes: ¿ganar la lotería te arruina?

Las cuentas se reproducen con `python cuentas.py`, que lee los archivos de esta carpeta y escribe `cuentas.json` y `powerball_valor_por_sorteo.csv`. Los PDF de los estudios no se incluyen: se bajan de los enlaces de cada fila, y su nombre dice la fecha en que se bajaron para este video.

## Datos guardados

| Archivo | Qué es | De dónde, y cuándo |
|---|---|---|
| `navidad_2026_programa_premios.csv` | Premios por serie del Sorteo de Navidad del 22 de diciembre de 2026 | [SELAE, *Programas de premios, cuarto trimestre de 2026*](https://www.loteriasyapuestas.es/f/loterias/documentos/Loter%C3%ADa%20Nacional/programas%20de%20premios/PROGRAMAS_PREMIOS_CUARTO_TRIMESTRE_2026_SABADOS.pdf), página del Sorteo de Navidad, fechada en Madrid el 26 de enero de 2026. Leído en el navegador integrado y transcripto el 2026-11-05: el servidor rechaza la descarga directa, así que el PDF no quedó guardado |
| `powerball_sorteos_descargado_2026-11-05.csv` | Pozo anunciado, valor de contado y ganadores de cada categoría, con y sin Power Play sumados, de los 289 sorteos del 2025-01-01 al 2026-11-04 | Páginas `draw-result` de [powerball.com](https://www.powerball.com/previous-results), leídas el 2026-11-05. La suma de todas las celdas (200.610.844,8) coincide con la de la página |
| `powerball_sorteo_2022-11-07_descargado_2026-11-05.csv` | El sorteo del pozo récord, 7 de noviembre de 2022: 2.040 millones anunciados, 997,6 al contado, 1 ganador del pozo y los ganadores de cada categoría, con y sin Power Play sumados | [powerball.com, draw-result del 2022-11-07](https://www.powerball.com/draw-result?gc=powerball&date=2022-11-07), leída el 2026-11-05. Se leyó dos veces la tabla; las sumas por categoría son propias |
| `florida_tabla1.csv` | Tabla 1: ganadores con y sin quiebra, por monto y por ventana de años | Hankins, Hoekstra y Skiba (2011), p. 963. PDF en `hankins_hoekstra_skiba_2011_descargado_2026-11-05.pdf` |
| `agarwal_mikhed_scholnick_wp18-22_descargado_2026-11-05.pdf` | Estudio de Canadá | [Fed de Filadelfia, WP 18-22](https://philadelphiafed.org/-/media/FRBP/Assets/working-papers/2018/wp18-22.pdf) |
| `cesarini_2016_qje_descargado_2026-11-05.pdf` | Estudio de Suecia | [IFN, reimpresión 2016-28](https://www.ifn.se/media/n14kekao/reprint2016-28.pdf) |
| `irs_f1040es_2026_descargado_2026-11-05.pdf` | Escalas del impuesto federal de 2026 | [IRS, formulario 1040-ES 2026](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |

## Comprobado en la fuente

| Afirmación | Dato | Fuente |
|---|---|---|
| Sorteo de Navidad 2026: emisión | 205 series de 100.000 billetes a 200 euros: 4.100 millones de euros. El 70 % va a premios: 2.870 millones | SELAE, programa de premios del 22 de diciembre de 2026 (arriba) |
| Sorteo de Navidad 2026: premios por serie | 15.304 premios que suman 14 millones por serie. El primero, 4 millones el billete (400.000 el décimo); décimos de 20 euros | SELAE, programa de premios (arriba) |
| Sorteo de Navidad 2025 | 198 series, décimo de 20 euros, emisión de 3.960 millones; "el total que se destina a premios (70% de la emisión)", 2.772 millones; 1.807 bolas de premios | [SELAE, Datos curiosos del Sorteo de Navidad 2025](https://www.selae.es/es/web-corporativa/comunicacion/publicaciones/noticias-navidad/datos-curiosos-del-sorteo-extraordinario-de-navidad-2025), 2025-12-05 |
| Adónde va el 30 % | "El 30% restante se destina a gastos de gestión, administración y Tesoro Público" | [Loterías y Apuestas del Estado, El Sorteo Extraordinario de Navidad y sus premios](https://www.loteriasyapuestas.es/es/loteria-nacional/historia-del-juego/el-sorteo-extraordinario-de-navidad-y-sus-premios). La página está desactualizada (195 series de 85.000 billetes) |
| Impuesto a los premios en España | 20 % sobre lo que pasa de 40.000 euros, por décimo; un premio de 100.000 paga 12.000 y cobra 88.000 | [Agencia Tributaria, Premios del sorteo de la Lotería de Navidad](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2025/diciembre/15/premios-sorteo-loteria-navidad.html), 2025-12-15 |
| Powerball: reglas | 5 números de 69 y 1 de 26; 2 dólares la jugada; sorteos lunes, miércoles y sábado | [powerball.com, preguntas frecuentes](https://www.powerball.com/faqs) |
| Powerball: premios y probabilidades | Pozo, 1 en 292.201.338; cualquier premio, 1 en 24,87; premios fijos de 1 millón a 4 dólares | [powerball.com, tabla de premios](https://www.powerball.com/powerball-prize-chart). `cuentas.py` llega a las mismas cifras por combinatoria |
| Powerball: cuotas o contado | Un pago inmediato y 29 anuales que suben 5 % por año. El contado es lo que hay en el pozo para financiar esas cuotas. Los montos anunciados son antes de impuestos | [powerball.com, preguntas frecuentes](https://www.powerball.com/faqs) |
| Powerball: qué fija el pozo | Las ventas y las tasas de interés: "the higher the interest rates, the higher the advertised Grand Prize" | [powerball.com, preguntas frecuentes](https://www.powerball.com/faqs) |
| Powerball: premio compartido | Si hay varios boletos ganadores, el pozo se divide en partes iguales | [powerball.com, preguntas frecuentes](https://www.powerball.com/faqs) |
| Powerball: el récord | El pozo más alto ganado fue el de 2.040 millones de noviembre de 2022; el del 24 de diciembre de 2025, de 1.820 millones, es el segundo | [LotteryUSA, Most epic jackpots from 2025](https://www.lotteryusa.com/news/most-epic-jackpots-from-2025), leída el 2026-11-05: "the second-highest Powerball jackpot ever won" y "The highest Powerball jackpot ever won was $2.04 billion". El monto y el contado de 2022 salen de la página oficial del sorteo. La página oficial de 2025 dice 1.820 millones; el verificador cita a NPR con 1.817 como pozo final: el guion dice "unos 1.820" |
| Powerball en el Reino Unido | Desde el 21 de julio de 2026 se vende allá, a 4 libras, y comparte solo el pozo | [powerball.com, preguntas frecuentes](https://www.powerball.com/faqs) |
| Powerball: reparto de las ventas | 50 % de las ventas a premios; el pozo mayor recibe como máximo 68,0131 % de eso (34,0066 % de las ventas) | [Regla de Oregón OAR 177-085-0025](https://oregon.public.law/rules/oar_177-085-0025), leída en oregon.public.law. Coincide con la cuenta propia: el pozo creció 33,5 % de lo vendido |
| Impuesto federal de EE. UU. en 2026 | Para una persona sola, 37 % sobre lo que pasa de 640.600 dólares | [IRS, formulario 1040-ES 2026](https://www.irs.gov/pub/irs-pdf/f1040es.pdf), Schedule X |
| Retención al cobrar | 24 % de los premios de más de 5.000 dólares | [IRS, instrucciones de los formularios W-2G y 5754 (enero de 2026)](https://www.irs.gov/instructions/iw2g) |
| Meta de inflación de EE. UU. | 2 % anual | [Reserva Federal, preguntas frecuentes](https://www.federalreserve.gov/faqs/economy_14400.htm) |
| Melate | Números del 1 al 56, se eligen 6; 15 pesos la combinación sola | [Pronósticos, Melate](https://pronosticos.gob.mx/Melate/Melate). La probabilidad, 1 en 32.468.436, es cuenta propia: la página no la publica |
| Baloto | 5 números del 1 al 43 y una superbalota del 1 al 16; 6.000 pesos | [baloto.com, cómo jugar](https://www.baloto.com/como-jugar) y [portada](https://www.baloto.com/). La probabilidad, 1 en 15.401.568, es cuenta propia |
| Quini 6 (Argentina) | "elegir 6 números sobre un total de 46 que van desde el '00' al '45 inclusive'". El Tradicional (primer sorteo y La Segunda) paga 6, 5 y 4 aciertos; 2.000 pesos el Tradicional, "sujetos a actualizaciones"; sorteos los miércoles y domingos. Cada sorteo extrae 6 números: el pozo extra usa "las 18 extracciones" de los dos sorteos del Tradicional y la Revancha | [Lotería de Santa Fe, preguntas frecuentes del Quini 6](https://www.loteriasantafe.gov.ar/quini-preguntas-frecuentes/), leída el 2026-11-05. La probabilidad, 1 en 9.366.819 por sorteo, es cuenta propia: la página no la publica. El reglamento completo está en la sección de descargas y no se abrió |
| El mito del 70 % | La NEFE dice que varios medios le atribuyeron que "70 percent of lottery winners end up bankrupt", que la cifra la dijo un participante en una reunión de expertos de 2001 y que no está respaldada por investigación de la NEFE ni la puede confirmar | [NEFE, Research Statistic on Financial Windfalls and Bankruptcy](https://nefe.org/news/2018/01/research-statistic-on-financial-windfalls-and-bankruptcy.aspx), 2018-01-12 |
| Florida: muestra | Ganadores de Fantasy 5 de más de 600 dólares, del 29 de abril de 1993 al 27 de noviembre de 2002, con premios de hasta 150.000. 34.987 ganadores | Hankins, Hoekstra y Skiba, [*The Review of Economics and Statistics* 93(3), 2011](https://ideas.repec.org/a/tpr/restat/v93y2011i3p961-969.html), sección II y tabla 1. [PDF](https://www.gwern.net/doc/sociology/2011-hankins.pdf) |
| Florida: los 2.000 quebrados | **Sale del paper:** "1,934 Fantasy 5 winners were linked to a bankruptcy in the five years after winning". La nota de prensa de Vanderbilt lo redondea a "almost 2,000" de "almost 35,000" | Hankins y otros, p. 963; [Vanderbilt News, 2009-07-07](https://news.vanderbilt.edu/2009/07/07/lotteries-from-big-bucks-to-bankruptcy-83864/) |
| Florida: tasa normal | Esa cifra equivale a poco más de 1 % por año, parecido al 1,0 % de todos los adultos de Florida de 1993 a 2001 | Hankins y otros, p. 963 |
| Florida: posterga, no evita | Quienes ganan de 50.000 a 150.000 quiebran menos en los primeros dos años y más de los tres a los cinco | Hankins y otros, resumen y tabla 1 |
| Florida: la diferencia no es casualidad | El grupo de grandes es chico (1.212, con 12 y 52 quiebras), pero en la especificación preferida la quiebra de los grandes baja 1,63 puntos en los dos primeros años (p = 0,001) y sube 1,21 de los tres a los cinco (p = 0,049); en cinco años no quiebran más ni menos | Hankins y otros, p. 963, especificación de la columna 4, leído en `hankins_2011.txt` |
| Florida: ¿el estudio más grande? | **No se afirma.** El paper solo dice que lo anterior eran encuestas informales (p. 961) y no se buscaron otros estudios. El guion dice "un estudio con casi 35.000 ganadores" | Hankins y otros, p. 961 |
| Canadá: vecinos | Un premio igual al ingreso mediano (29.229 dólares canadienses) suma 0,03 quiebras de vecinos por código postal en 3 años: 6,6 % sobre el promedio de 0,455, que es el de los códigos postales de los ganadores (5.352 en esa ventana, con un premio medio de 6.911 dólares canadienses), no el de barrios sin premio (WP 18-22, p. 16 y tabla 1). Uno de 100.000 suma 0,052, un 11 % | Agarwal, Mikhed y Scholnick, [Fed de Filadelfia WP 18-22, 2018](https://philadelphiafed.org/-/media/FRBP/Assets/working-papers/2018/wp18-22.pdf), pp. 1 y 16 |
| Canadá: muestra | Una sola provincia, que no pueden nombrar; premios de más de 1.000 dólares del 1 de abril de 2004 al 31 de marzo de 2014; 7.377 premios; se descartan los de más de 150.000. Un código postal tiene una mediana de 13 hogares | WP 18-22, pp. 1, 8 y 9 |
| Suecia: salud | En adultos, ninguna evidencia de que la riqueza cambie la mortalidad o el uso de la salud, salvo quizás un poco menos de remedios de salud mental. Los premios suman casi 1.000 millones de dólares | Cesarini, Lindqvist, Östling y Wallace, [*Quarterly Journal of Economics* 131(2), 2016](https://ideas.repec.org/a/oup/qjecon/v131y2016i2p687-738..html), resumen y p. 689 |
| Suecia: satisfacción con la vida | Los ganadores de premios grandes están más satisfechos con su vida, de 5 a 22 años después, y el efecto no se apaga; en felicidad y salud mental el efecto es bastante menor | Lindqvist, Östling y Cesarini, [*Review of Economic Studies* 87(6), 2020](https://econpapers.repec.org/RePEc:oup:restud:v:87:y:2020:i:6:p:2703-2726.), resumen |

## Cuentas propias (de `cuentas.py`)

| Dato | Valor | Cómo |
|---|---|---|
| Combinaciones de Powerball | 292.201.338 | 69 tomados de a 5, por 26 |
| Jugadas para 50 % de chance de ganar el pozo en un solo sorteo | 146.100.669 combinaciones distintas, o sea 292.201.338 dólares | La mitad de las 292.201.338 combinaciones. Corregido el 2026-11-05: antes daba 202.538.535 con la fórmula de boletos en sorteos distintos, que no corresponde a un solo sorteo |
| Años jugando 3 veces por semana para una chance esperada | 1.873.086 | 292.201.338 sobre 156 jugadas por año |
| Melate y Baloto | 1 en 32.468.436 y 1 en 15.401.568 | 56 tomados de a 6; 43 tomados de a 5 por 16 |
| Quini 6 | 1 en 9.366.819 por sorteo: 94 veces más difícil que el primer premio de Navidad, y Powerball 31 veces más difícil que el Quini 6 | 46 tomados de a 6. Agregado el 2026-11-05 |
| Powerball, solo las blancas | 11.238.513 combinaciones, que por las 26 rojas dan 292.201.338 | 69 tomados de a 5. Paso intermedio para la pizarra |
| Navidad: probabilidad del primer premio | 1 en 100.000 por décimo | Un número entre 100.000 |
| Navidad: recorrido de 100 euros | 30 a gestión y Tesoro; 20 al primer premio; 8,75 al segundo y al tercero; 4,4 a cuartos y quintos; 8,97 a la pedrea; 2,9 a aproximaciones y centenas; 14,98 a las dos últimas cifras; 10 al reintegro; −4,55 de impuesto: vuelven 65,45 | Programa de premios y gravamen por décimo |
| Navidad: valor esperado de un décimo | 13,09 euros de 20 | Lo mismo, por décimo |
| Navidad: qué le pasa a cada décimo | 86,18 % no cobra nada, 8,6 % solo recupera los 20 euros y 5,21 % cobra más | Simulación de 200 sorteos con la semilla 2026. Supone que los premios se suman en un mismo número |
| Navidad: comprar un décimo de cada número | Cuesta 2 millones, vuelven 1.309.000 después de impuestos: se pierden 691.000 con el primer premio asegurado | Programa de premios |
| Powerball: recorrido de 100 dólares | 50 a premios: 15,99 a premios fijos y 34,01 al pozo; 50 a las loterías estatales y costos | Probabilidad por premio fijo; regla de Oregón para el 50 % |
| Powerball: recorrido de 100 dólares después del impuesto federal | Vuelven 37,42: 15,99 de premios fijos y 21,43 del pozo, que pierde una tasa efectiva de 36,98 % | Tasa que pagaron los 11 pozos ganados en los 243 sorteos, cada ganador por su parte del contado, con el impuesto federal de 2026 de una persona sola. Premios fijos sin impuestos y sin impuesto estatal: favorece al boleto. Comparable con el 65,45 de Navidad, que ya descuenta el gravamen español |
| Powerball: jugadas por sorteo | 8,1 millones de mediana con pozos de menos de 100 millones; 248 millones el 6 de septiembre de 2025, con 1.790 millones anunciados | Ganadores de las ocho categorías menores sobre su probabilidad. Comprobación: predice 14,0 ganadores del pozo en 243 sorteos y hubo 14 |
| Powerball: aporte al pozo | 33,5 % de lo vendido | Suba del valor de contado entre sorteos sin ganador, sobre las ventas estimadas. La regla dice como máximo 34,0066 % |
| Powerball: el boleto del pozo más grande (24 de diciembre de 2025, 1.820 millones) | 6,55 dólares si se cuenta el anunciado; 3,18 al contado; 2,12 después del impuesto federal; 1,72 si se cuenta que puede haber otro ganador | Ver los supuestos abajo |
| Powerball: ¿algún sorteo vale lo que cuesta? | Ninguno de los 243 llega a 2 dólares. El mejor, el de arriba, 1,72 | Misma cuenta en todos los sorteos |
| Powerball: el pozo récord (7 de noviembre de 2022, 2.040 millones) | 7,30 dólares con el anunciado; 3,73 al contado; 2,47 después del impuesto federal de 2026; 1,71 si puede haber otro ganador. 278,68 millones de jugadas estimadas, 0,954 otros ganadores esperados, parte esperada del pozo 64,5 % | Misma cuenta que los 243 sorteos, aparte de ellos. Se usa el impuesto de 2026, no el de 2022, para que la base sea la misma |
| Powerball: comprar todas las combinaciones el 24 de diciembre de 2025 | Cuesta 584 millones; se espera perder 83 millones (82.919.388): premios fijos 93,5 millones y pozo neto esperado 408 millones | Premios fijos más el pozo neto por la misma parte esperada del boleto suelto, 77,56 %. Corregido el 2026-11-05: antes dividía entre 1 + λ y daba 148 millones |
| Cuotas: sorteo del 4 de noviembre de 2026 | 847 millones anunciados, 363,1 al contado (42,9 %). Cuotas de 12,7 millones a 52,5 millones; la última vale 29,5 millones de hoy con 2 % de inflación. El contado equivale a cobrar las cuotas con un interés de 5,38 % anual | 30 pagos que suben 5 %; tasa que iguala el valor presente al contado |
| Florida: quiebras en 5 años | 5,53 % de todos; 5,28 % de los que ganaron de 50.000 a 150.000; 6,0 % de los que ganaron menos de 10.000. Si fuera el 70 %, serían 24.491 personas, no 1.934 | Tabla 1 |
| Florida: posterga | En los dos primeros años, 0,99 % de los grandes y 3,14 % de los chicos; de los tres a los cinco, 4,29 % y 2,86 % | Tabla 1 |
| Canadá en barrios | Por cada 1.000 barrios de ganadores, 455 quiebras de vecinos en 3 años en promedio; 30 más si alguien gana el ingreso mediano y 52 más si gana 100.000 | Cifras del estudio, por 1.000 |

**Supuestos del valor del boleto de Powerball:** impuesto federal de 2026 de una persona sola sobre el pago al contado, sin impuesto estatal, y premios fijos sin impuestos. Los tres favorecen al boleto, así que la conclusión no depende de ellos. No se cuenta el Power Play ni Double Play. Los otros ganadores se calculan como un Poisson con las jugadas estimadas de ese sorteo. Solo se usan los sorteos hasta el 20 de julio de 2026, porque después entran jugadas del Reino Unido que no figuran en los ganadores de las categorías menores.

## Cuidados al escribir

- **Los 2.000 de Florida no son millonarios:** ganaron de 600 a 150.000 dólares. El estudio no mide a los que ganan el pozo de una lotería grande. Decir "ganadores de premios medianos".
- **Florida, ventanas:** cada ganador se cuenta en las tres ventanas de la tabla 1, por eso los totales suman lo mismo (34.987). Las quiebras se unieron por nombre, apellido y condado: puede haber errores, que el estudio discute.
- **"Igual que cualquiera":** el estudio compara con todos los adultos de Florida, no con gente parecida. Decir "parecido a la tasa de cualquier adulto de Florida en esos años".
- **Canadá, en proporción y en absoluto:** el 6,6 % es real, pero sobre una base chica: 30 quiebras más por cada 1.000 barrios en 3 años. Decir las dos cosas.
- **Canadá, versión:** las cifras son del documento de trabajo de 2018. La versión publicada en *Review of Financial Studies* (2020) no se leyó.
- **El 30 % de España:** la frase sobre gestión, administración y Tesoro está en una página vieja de SELAE. El 70 % sí está en el programa de 2026.
- **Navidad, simulación:** los porcentajes de décimos que no cobran nada salen de repartir los premios al azar; varían un poco de un sorteo a otro.
- **Jugadas de Powerball:** son una estimación propia, no un dato oficial de ventas. Decir "estimamos, a partir de cuántos ganaron premios chicos".
- **Powerball, impuestos estatales:** varían de 0 a más de 10 % según el estado, y no se usan. Decir que la cuenta los deja afuera a favor del boleto.
- **El interés de 5,38 %:** es la tasa que hace equivalentes las cuotas y el contado anunciados. No es una oferta de inversión ni una recomendación.
- **Ganadores privados:** no nombrar a nadie ni decir dónde se vendió un boleto ganador.
- **La NEFE:** citar lo que dice su comunicado; no decir quién fue el participante de 2001, porque la NEFE no lo nombra.

## Sin comprobar: no entra al guion todavía

| Dato | Estado |
|---|---|
| Resolución del BOE del Sorteo de Navidad 2026 | **Revisar.** No se encontró en el BOE. El 70 % quedó comprobado en el programa oficial de SELAE |
| Porcentaje de las ventas que va a premios en Melate y en Baloto | **Revisar.** Las páginas no lo publican y el acuerdo de Baloto es un escaneo sin texto |
| Cada cuánto se sortean Melate y Baloto | **Revisar.** No se leyó |
| Cifras de la versión publicada del estudio de Canadá (2020) | **Revisar** |
| Cómo trata YouTube los videos sobre juegos de azar en la guía de contenido apto para anunciantes | **Revisar.** La página leída (support.google.com/youtube/answer/6162278) no tiene una sección sobre juegos de azar |
| Texto oficial de las reglas de Powerball de la Asociación Multiestatal | **Revisar.** Se usó la regla de Oregón; las de Colorado y Maine dan el mismo 68,0131 % según la búsqueda, pero no se abrieron |
| Impuesto estatal sobre premios | Sin buscar: no se usa |
| Loto de Chile (Polla Chilena de Beneficencia) | **Revisar.** El sitio oficial (polla.cl) rechazó la lectura el 2026-11-05 con un bloqueo de seguridad, también en el navegador integrado. La prensa (Pauta, 24horas) describe 6 números del 1 al 41 más un comodín, lo que daría 1 en 4.496.388, pero sin la regla oficial abierta **Chile queda afuera del guion** y de `cuentas.json` |
| Porcentaje de las ventas que va a premios en el Quini 6 | **Revisar.** La página de preguntas frecuentes no lo publica. Igual que Melate y Baloto, el Quini 6 entra solo en la comparación de probabilidades |

Las personas que aparezcan con nombre serán hipotéticas, y el ratón es un personaje de ficción: no da consejos.
