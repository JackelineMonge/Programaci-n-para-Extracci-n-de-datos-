# Nombre: Jackeline Monge Nunez
# Grupo: 951
# Fecha: 13 de abril del 2025
# Descripción: Esta función normaliza los datos de un DataFrame usando el metodo Min-Max en las columnas especificadas y devuelve el DataFrame resultante.
import pandas as pd


# Normalización Min-Max
def normalizar_min_max(df: pd.DataFrame, columnas):
    for columna in columnas:
        if columna in df.columns:
            min_val = df[columna].min()
            max_val = df[columna].max()
            df[columna] = (df[columna] - min_val) / (max_val - min_val)
        else:
            print(f"La columna '{columna}' no existe en el DataFrame.")
    print(df)

# Normalización Z-Score
def normalizar_z_score(df: pd.DataFrame, columnas):
    for columna in columnas:
        if columna in df.columns:
            media = df[columna].mean()
            desviacion = df[columna].std()
            df[columna] = (df[columna] - media) / desviacion
        else:
            print(f"La columna '{columna}' no existe en el DataFrame.")
    print(df)


# Normalización Escalado Simple
def normalizar_escalado_simple(df: pd.DataFrame, columnas):
    for columna in columnas:
        if columna in df.columns:
            max_val = df[columna].max()
            df[columna] = df[columna] / max_val
        else:
            print(f"La columna '{columna}' no existe en el DataFrame.")
    print(df)


# Pruebas
if __name__ == "__main__":
    datos = {
        "edad": [18, 22, 25, 30, 35],
        "ingresos": [1000, 1500, 2000, 2500, 3000]
    }

    df = pd.DataFrame(datos)
    columnas = ["edad", "ingresos"]

    print("____________Min-Max_______________")
    normalizar_min_max(df.copy(), columnas)

    print("____________Z-Score_______________")
    normalizar_z_score(df.copy(), columnas)

    print("____________Escalado Simple_______________")
    normalizar_escalado_simple(df.copy(), columnas)