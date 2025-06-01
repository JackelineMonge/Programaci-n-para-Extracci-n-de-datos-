"""
Análisis de ventas de frutas por tienda usando pandas (agrupación y tablas dinámicas).
Autor: Jackeline Monge
Grupo 951
"""
import pandas as pd

def construir_datos_ventas():
    info = {
        "Sucursal": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
        "Articulo": ["Manzana", "Platano", "Naranja"] * 3,
        "Tipo": ["Fruta"] * 9,
        "Costo": ["30", "20", "35", "25", "30", "45", "35", "20", "25"],
        "Unidades": ["50", "30", "20", "60", "25", "35", "55", "20", "30"],
        "Nota": ["A", "B", "C", "A", "B", "A", "C", "B", "A"]
    }
    return pd.DataFrame(info)

def codificar_columnas(df):
    df["ID Sucursal"] = df["Sucursal"].replace({"A": 1, "B": 2, "C": 3})
    df["Valoración"] = df["Nota"].replace({"A": 3, "B": 2, "C": 1})
    return df

def agregar_ventas_totales(df):
    df = df.copy()
    df[["Costo", "Unidades"]] = df[["Costo", "Unidades"]].apply(pd.to_numeric)
    df["Total_Vendido"] = df["Costo"] * df["Unidades"]
    return df

def resumen_ventas_por_producto(df):
    tabla = pd.pivot_table(
        df,
        values="Total_Vendido",
        index="Articulo",
        columns="Sucursal",
        aggfunc="sum",
        fill_value=0
    )
    return tabla

if __name__ == "__main__":
    df_base = construir_datos_ventas()
    df_etiquetado = codificar_columnas(df_base)
    df_completo = agregar_ventas_totales(df_etiquetado)
    resumen = resumen_ventas_por_producto(df_completo)

    print("=== Tabla con códigos asignados ===")
    print(df_etiquetado.head())

    print("\n=== Total vendido por sucursal ===")
    print(df_completo.groupby("Sucursal")["Total_Vendido"].sum().reset_index())

    print("\n=== Resumen dinámico: Producto vs. Sucursal ===")
    print(resumen)
