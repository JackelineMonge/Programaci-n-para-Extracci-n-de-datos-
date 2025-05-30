# Nombre completo: Jackeline Monge Nunez
# Grupo: 951
# Fecha de realización: 11 de Febrero del 2025
# Descripción: Este ejercicio crea una clase llamada "Estadística" que incluye los métodos
# para calcular la frecuencia de números, la moda y el histograma de una lista de números.

class Estadistica:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    # Frecuencia de Números:
    def frecuencia_numeros(self):
        frecuencia = []
        for num in set(self.lista):
            frecuencia.append((num, self.lista.count(num)))
        return frecuencia


    # Moda:
    def moda(self):
        frecuencia = self.frecuencia_numeros()
        moda = max(frecuencia, key=lambda x: x[1])
        return moda[0]


    # Histograma:
    def histograma(self):
        frecuencia = self.frecuencia_numeros()
        for num, count in sorted(frecuencia):
            print(f'{num} {"*" * count}')

lista = Estadistica([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
lista.histograma()

