# Nombre completo: Jackeline Monge Nunez
# Grupo: 951
# Fecha de realización: 11 de Febrero del 2025
# Descripción: Este ejercicio simula el historial de cambios de una hoja de cálculo, donde
# se pueden registrar cambios y deshacer el último cambio utilizando una pila.

# Función para registrar un cambio
def registrar_cambio(historial, celda, valor):
    historial.append((celda, valor))

# Función para deshacer el último cambio
def deshacer_cambio(historial):
    if historial:
        historial.pop()


historial_cambios = []
registrar_cambio(historial_cambios, 'A1', 10)
registrar_cambio(historial_cambios, 'B2', 20)

print(historial_cambios)

deshacer_cambio(historial_cambios)
print(historial_cambios) 
