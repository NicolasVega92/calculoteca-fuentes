"""Saca de ie_data.xls (Robert Shiller, shillerdata.com) los meses que usa este video.

Hay que bajar ie_data.xls y dejarlo en esta carpeta. Necesita xlrd.
P es el promedio mensual de los cierres diarios del índice; D, el dividendo anual; CPI, el índice de precios.
"""

import csv
from pathlib import Path

import xlrd

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "ie_data.xls"
TARGET = HERE / "sp500_shiller.csv"
FIRST, LAST = 1927, 1960


def main():
    sheet = xlrd.open_workbook(SOURCE).sheet_by_name("Data")
    rows = []
    for index in range(sheet.nrows):
        date, price, dividend, _, cpi = sheet.row_values(index)[:5]
        if not isinstance(date, float) or not FIRST <= int(date) <= LAST:
            continue
        # Las fechas son números: octubre de 1929 es 1929.1, no 1929.10.
        rows.append((int(date), round((date - int(date)) * 100), price, dividend, cpi))
    with TARGET.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["anio", "mes", "precio", "dividendo_anual", "ipc"])
        writer.writerows(rows)
    print(len(rows), "meses en", TARGET.name)


if __name__ == "__main__":
    main()
