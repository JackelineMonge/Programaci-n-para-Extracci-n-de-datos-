# Nombre: jackeline monge nunez
# Grupo: 951
# Fecha: 10 de abril del 2025
# Descripción: Funciones para tratamiento de datos duplicados y nulos con pandas
import pandas as pd
import numpy as np


def declarar_df():
    d = {
        "nombre": ["Ana", "María", "Pedro", None, "Juan", "Anahi"],
        "edad": [20, None, 21, 19, np.nan, 20],
        "salario": [1000, None, None, 2000, 2500, 1000]
    }
    df = pd.DataFrame(d)
    return df


def porcentaje_nulos(df):
    print("Porcentaje de valores nulos:")
    print(df.isnull().mean() * 100)


def contar_duplicados(df):
    print("Núm de renglones duplicados:")
    print(df.duplicated().sum())


def eliminar_columnas_nulas(df, max_porcentaje):
    print(f"Eliminando columnas con cierto % de valores nulos.")
    if not 0 <= max_porcentaje <= 1:
        raise ValueError("El porcentaje máximo debe estar entre 0 y 1")
    porcentaje_nulos_por_col = df.isnull().mean()
    columnas_a_eliminar = porcentaje_nulos_por_col[porcentaje_nulos_por_col >= max_porcentaje].index.tolist()
    df.drop(columns=columnas_a_eliminar, inplace=True)
    print(f"Columnas eliminadas: {columnas_a_eliminar}")
    print(df)


def sustituir_nulos(df, columnas, metodo):
    print(f"Rellenando nulos usando el método '{metodo}' en columnas: {columnas}")
    if metodo not in ['mean', 'bfill', 'ffill']:
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'.")

    for col in columnas:
        if metodo == 'mean':
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = df[col].fillna(df[col].mean())
            else:
                raise ValueError(f"La columna '{col}' no es numérica y no se puede usar 'mean'.")
        else:
            df[col] = df[col].fillna(method=metodo)

    print(df)


def eliminar_duplicados(df):
    print("Eliminando renglones duplicados")
    cantidad_antes = len(df)
    df.drop_duplicates(inplace=True)
    cantidad_despues = len(df)
    print(f"Renglones eliminados: {cantidad_antes - cantidad_despues}")
    print(df)


if __name__ == "__main__":
    df = declarar_df()
    print("DataFrame:")
    print(df)
    print("******************************")
    porcentaje_nulos(df)
    print("******************************")
    contar_duplicados(df)
    print("******************************")
    eliminar_columnas_nulas(df, 0.4)
    print("******************************")
    sustituir_nulos(df, ['edad', 'salario'], 'mean')
    print("******************************")
    eliminar_duplicados(df)
    print("******************************")