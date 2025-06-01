"""
Análisis de ventas mensuales por producto usando pandas loc e iloc.
Autor: Jackeline Monge
Grupo 951
"""
import pandas as pd

def generar_datos_ventas():
    registros = {
        "X": [723, 121, 923],
        "Y": [194, 512, 243],
        "Z": [309, 222, 809]
    }
    return pd.DataFrame(registros)

class GestorEstadisticas:
    def __init__(self, datos):
        self.datos = datos

    def obtener_venta(self, articulo: str, indice_mes: int) -> int:
        return self.datos.loc[indice_mes, articulo]

    def resumen_mensual(self, indice_mes: int) -> pd.Series:
        return self.datos.loc[indice_mes]

    def extraer_por_meses(self, lista_meses: list) -> pd.DataFrame:
        return self.datos.loc[lista_meses]

    def valor_por_indice(self, fila_idx: int, col_idx: int) -> pd.Series:
        return self.datos.iloc[fila_idx, col_idx]

    def modificar_registro(self, mes_idx: int, articulo: str, nuevo_dato: int):
        self.datos.loc[mes_idx, articulo] = nuevo_dato

if __name__ == "__main__":
    ventas_df = generar_datos_ventas()
    gestor = GestorEstadisticas(ventas_df)

    print("=== Caso 1: Consulta de ventas del artículo X en enero ===")
    resultado = gestor.obtener_venta("X", 0)
    print(f"Ventas registradas: {resultado}")

    print("\n=== Caso 2: Resumen completo para febrero ===")
    resumen_febrero = gestor.resumen_mensual(1)
    print(f"Detalle por categoría:\n{resumen_febrero}")
    print(f"Suma total: {resumen_febrero.sum()}")

    print("\n=== Caso 3: Modificando datos de marzo para Y ===")
    valor_inicial = gestor.obtener_venta("Y", 2)
    print(f"Valor previo: {valor_inicial}")
    gestor.modificar_registro(2, "Y", 1200)
    print("Nuevo estado del DataFrame:")
    print(gestor.datos)
