# Fuentes: la crisis de 1929

Las cuentas se reproducen con `python cuentas.py`, que lee `sp500_shiller.csv` y escribe `cuentas.json` y `trayectos.csv`. La serie mensual sale de `extraer_shiller.py`, que lee `ie_data.xls`: hay que bajarlo de shillerdata.com y dejarlo en esta carpeta.

## Comprobado en la página

| Afirmación | Dato | Fuente |
|---|---|---|
| Máximo y mínimo del Dow Jones | 381,17 el 3 de septiembre de 1929; 41,22 el 8 de julio de 1932: 89 % abajo | [Federal Reserve History](https://www.federalreservehistory.org/essays/stock-market-crash-of-1929) |
| Volvió al máximo, sin contar dividendos | 23 de noviembre de 1954 | [Federal Reserve History](https://www.federalreservehistory.org/essays/stock-market-crash-of-1929) |
| Lunes y Martes Negros | Casi 13 % y casi 12 %; a mediados de noviembre había perdido casi la mitad | [Federal Reserve History](https://www.federalreservehistory.org/essays/stock-market-crash-of-1929) |
| Serie mensual del índice, dividendos y precios | Promedios mensuales desde 1871; se usan de 1927 a 1960 | [Robert Shiller, `ie_data.xls`](https://shillerdata.com/), descargado el 2026-11-02 |
| Depósito para comprar con crédito | De 10 a 30 % antes de 1928; de 10-20 % a 40-50 % a mediados de 1929. Los autores avisan que no hay datos completos | [Borowiecki, Dzieliński y Tepper, nota 16](https://www.sdu.dk/-/media/files/om_sdu/institutter/ivoe/econ/the+great+margin+call.pdf) |
| Bancos suspendidos, 1930 a 1933 | 1.350, 2.293, 1.453 y 4.000: 9.096 en total | [FDIC, cap. 3, tabla 5](https://www.fdic.gov/resources/publications/brief-history-of-deposit-insurance/book/brief-history-deposit-insurance-3.pdf) y cuenta propia |
| Pérdidas de los depositantes, 1930 a 1933 | 1.337 millones de dólares sobre 6.830 millones: 19,6 % | [FDIC, cap. 3, tabla 5](https://www.fdic.gov/resources/publications/brief-history-of-deposit-insurance/book/brief-history-deposit-insurance-3.pdf) y cuenta propia |
| Bancos antes de la crisis | Más de 8.000 miembros de la Reserva Federal y casi 16.000 no miembros | [Federal Reserve History](https://www.federalreservehistory.org/essays/banking-panics-1930-31) |
| Bancos que no reabrieron tras el feriado de 1933 | Unos 4.000 | [Federal Reserve History](https://www.federalreservehistory.org/essays/bank-holiday-of-1933) |
| Dinero y precios | El dinero cayó casi 30 % de fines de 1930 al invierno de 1933, y los precios promedio, según la página, en igual medida | [Federal Reserve History](https://www.federalreservehistory.org/essays/great-depression) |
| Fondo del derrumbe | Marzo de 1933 | [Federal Reserve History](https://www.federalreservehistory.org/essays/great-depression) |
| Seguro de depósitos | Ley firmada el 16 de junio de 1933; fondo temporal desde enero de 1934, hasta 2.500 dólares; permanente desde julio de 1934, hasta 5.000 | [Federal Reserve History](https://www.federalreservehistory.org/essays/glass-steagall-act) |
| Oro | Suspensión del patrón oro el 20 de abril de 1933 | [Federal Reserve History](https://www.federalreservehistory.org/essays/roosevelts-gold-program) |
| Ley de Reserva de Oro | 30 de enero de 1934; 35 dólares la onza, antes 20,67 | [Federal Reserve History](https://www.federalreservehistory.org/essays/gold-reserve-act) |
| Producto real | 1.191 en 1929 y 877 en 1933: cayó 26,3 % | [FRED, GDPCA](https://fred.stlouisfed.org/series/GDPCA) y cuenta propia |
| Producción industrial | Máximo en julio de 1929 y mínimo en julio de 1932: cayó 53,6 % | [FRED, INDPRO](https://fred.stlouisfed.org/series/INDPRO) y cuenta propia |
| Desempleo | Máximo de 25,59 % en mayo de 1933 | [NBER en FRED](https://fred.stlouisfed.org/series/M0892AUSM156SNBR) |
| Acciones negociadas | Casi 13 millones el 24 de octubre, más del triple de un día promedio; 16,4 millones el 29 de octubre | [Massachusetts Historical Society](https://www.masshist.org/beehiveblog/2014/10/black-days-the-wall-street-crash-of-1929) |
| Ventas forzadas | Al menos 7 de los 10 días de baja del 24 de octubre al 15 de noviembre; las llamadas de margen solían salir de noche | [Borowiecki, Dzieliński y Tepper, sección 3](https://www.sdu.dk/-/media/files/om_sdu/institutter/ivoe/econ/the+great+margin+call.pdf) |
| Por qué cayó entonces | Sigue en debate; el estudio apunta a depósitos más exigentes en 1929 y a las bajas de septiembre y principios de octubre | [Borowiecki, Dzieliński y Tepper, resumen](https://www.sdu.dk/-/media/files/om_sdu/institutter/ivoe/econ/the+great+margin+call.pdf) |
| Primeros bancos | 256 suspensiones en noviembre de 1930 y 352 en diciembre; Bank of United States, unos 200 millones en depósitos, 11 de diciembre de 1930 | [FDIC, 1930-1939](https://www.fdic.gov/about/history/deposit-insurance/1930-1939.html) |
| Marzo de 1933 | Avisos en los hoteles; todos los estados en feriado el 4 de marzo; feriado nacional el 6; ley de emergencia el 9, con 40 minutos de debate en la Cámara; moneda impresa las 24 horas; discurso por radio el 12 | [FDIC, cap. 3](https://www.fdic.gov/resources/publications/brief-history-of-deposit-insurance/book/brief-history-deposit-insurance-3.pdf) |
| El oro y la recuperación | Quienes dejaron el patrón oro se recuperaron a partir de ese momento, según Eichengreen y Sachs | [Federal Reserve History](https://www.federalreservehistory.org/essays/roosevelts-gold-program) |
| Por qué se contagiaron los bancos | Los depositantes retiraron en masa de otros bancos y el pánico pasó de un pueblo a otro | [Federal Reserve History](https://www.federalreservehistory.org/essays/banking-panics-1930-31) |
| Por qué bajó el dinero | Los banqueros acumularon reservas y el público guardó efectivo; eso redujo el dinero y los precios lo siguieron | [Federal Reserve History](https://www.federalreservehistory.org/essays/banking-panics-1930-31) |
| El papel de la Reserva Federal | Se la creó en parte como prestamista de última instancia; no frenar la caída del dinero fue su "most serious sin of omission", según el ensayo de Gary Richardson | [Federal Reserve History](https://www.federalreservehistory.org/essays/great-depression) |
| "25 años" es engañoso | Con dividendos y deflación, quien compró en el máximo se recuperó a fines de 1936 | [Mark Hulbert, The New York Times, 2009, copia en HNN](https://www.hnn.us/article/79770); solo se pudo leer el comienzo |

## Cuidados al escribir

- **Depósito de 10 %:** [Federal Reserve History](https://www.federalreservehistory.org/essays/stock-market-crash-of-1929) lo llama "typically 10 percent", sin fecha precisa. Para septiembre de 1929 no alcanza: el estudio citado arriba muestra que ya se pedía mucho más. No decir que alguien compró con 10 % en ese momento.
- **Hulbert y estas cuentas:** coinciden en fines de 1936. Noviembre de 1936 es cuenta propia con los datos de Shiller. Que esa recuperación se perdiera hasta julio de 1949 también es cuenta propia, y no se leyó si Hulbert lo menciona.
- **Comprobación:** Aguanta en poder de compra coincide con la columna de retorno total real de Shiller en diciembre de 1936, 1945 y 1954.
- **Desempleo:** decir "uno de cada cuatro". La serie del NBER da 0,91 % en septiembre de 1929, muy por debajo del 3,2 % anual que aparece en otros resúmenes: son series distintas, así que no usarla para contar desde cuánto subió.
- **Suspendido no es quebrado:** la FDIC aclara que algunos bancos suspendidos volvieron a abrir. Decir "9.096 bancos cerraron sus puertas por problemas, y algunos reabrieron".
- **Parte de los bancos:** 9.096 sobre unos 24.000 da 37,9 %. Es cuenta propia, con dos números redondos de otra página: decir "más de un tercio".
- **Fecha de la Ley de Reserva de Oro:** una página de Federal Reserve History dice 4 de enero y otra, 30 de enero. Se usa la segunda, que es la dedicada a esa ley; conviene confirmarlo en otra fuente.
- **Precios:** el dato de Federal Reserve History deduce los precios de la caída del dinero. No es un índice de precios.
- **Banco de 100 dólares:** es un ejemplo inventado, rotulado en pantalla, para mostrar el mecanismo. Las proporciones no salen de ningún banco real.
- **1.000 dólares en casa:** es cuenta propia con el índice de precios de Shiller. Supone billetes guardados fuera de los bancos. La persona hipotética no cuenta como una quinta: es una comparación aparte.
- **"Su omisión más grave":** es la opinión del autor de un ensayo publicado en el sitio de la Reserva Federal, no una postura oficial. Decir "un ensayo de su propio sitio de historia".

## Sin comprobar: no entra al guion todavía

| Dato | Estado |
|---|---|
| Total de préstamos a corredores | Ninguna página leída da la cifra |
| Cifras exactas de acciones: 12.894.650 y 16.410.030 | Solo resúmenes de búsqueda. Usar las redondeadas de arriba |

Las cuatro personas son hipotéticas y el ratón es un personaje de ficción: no da consejos.
