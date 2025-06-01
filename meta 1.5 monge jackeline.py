# Nombre: Mnge Nunez Jackeline
# Grupo: 951
# Fecha: 09/03/2025

import pandas as pd


# Ejercicio 1
# Descripción: Este ejercicio genera un DataFrame con los datos de ventas y gastos mensuales.

def generar_reporte_mensual():
    print("\n--- Ejercicio 1 ---\n")
    datos = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
        "Monto_Ventas": [30500, 35600, 28300, 33900],
        "Monto_Gastos": [22000, 23400, 18100, 20700]
    }

    df_ventas = pd.DataFrame(datos)
    return df_ventas


# Ejercicio 2
# Descripción: En este ejercicio se lee un archivo CSV con cotizaciones y se generan estadísticas.

def analizar_cotizaciones():
    print("\n--- Ejercicio 2 ---\n")
    df_cot = pd.read_csv("dataset/cotizacion.csv", sep=";", thousands=".", decimal=",")

    resumen = {
        "Empresa": ["Máximo", "Mínimo", "Promedio"],
        "Final": [df_cot.Final.max(), df_cot.Final.min(), df_cot.Final.mean()],
        "Maximo": [df_cot.Máximo.max(), df_cot.Máximo.min(), df_cot.Máximo.mean()],
        "Minimo": [df_cot.Mínimo.max(), df_cot.Mínimo.min(), df_cot.Mínimo.mean()],
        "Volumen": [df_cot.Volumen.max(), df_cot.Volumen.min(), df_cot.Volumen.mean()],
        "Efectivo": [df_cot.Efectivo.max(), df_cot.Efectivo.min(), df_cot.Efectivo.mean()]
    }

    df_resumen = pd.DataFrame(resumen)
    return df_resumen


# Ejercicio 3
# Descripción: Se analiza la base de datos del Titanic con distintas consultas básicas.

def explorar_titanic():
    print("\n--- Ejercicio 3 ---\n")
    df_titanic = pd.read_csv("dataset/titanic.csv", sep=";", thousands=".", decimal=",")

    print("\n--- Cantidad de datos ---\n")
    print(df_titanic.size)

    print("\n--- Nombres de columnas ---\n")
    print(df_titanic.columns)

    print("\n--- Primeras 10 filas ---\n")
    print(df_titanic.head(10))

    print("\n--- Últimas 10 filas ---\n")
    print(df_titanic.tail(10))

    print("\n--- 10 filas aleatorias ---\n")
    print(df_titanic.sample(10))


if __name__ == "__main__":
    df_mensual = generar_reporte_mensual()
    print(df_mensual)

    df_estadisticas = analizar_cotizaciones()
    print(df_estadisticas)

    explorar_titanic()
