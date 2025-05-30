# Nombre completo: Jackeline Monge Nunez
# Grupo: 951
# Fecha de realización: 16 de Febrero del 2025
# Descripción: Sistema de reservas con sets

#aqui esta la base de datos de habitaciones
habitaciones_disponibles = {101, 102, 103, 104, 105}
habitaciones_reservadas = set()

def reservar_habitacion(habitacion):
    """Reserva una habitación si está disponible."""
    if habitacion in habitaciones_disponibles:
        habitaciones_disponibles.remove(habitacion)
        habitaciones_reservadas.add(habitacion)
        print(f"Habitación {habitacion} reservada con éxito.")
    else:
        print(f"La habitación {habitacion} no está disponible para reservar.")

def liberar_habitacion(habitacion):
    """Libera una habitación reservada."""
    if habitacion in habitaciones_reservadas:
        habitaciones_reservadas.remove(habitacion)
        habitaciones_disponibles.add(habitacion)
        print(f"Habitación {habitacion} liberada con éxito.")
    else:
        print(f"La habitación {habitacion} no está reservada o no existe.")

def mostrar_disponibilidad():
    """Muestra las habitaciones disponibles y reservadas."""
    print("\nHabitaciones disponibles:", habitaciones_disponibles)
    print("Habitaciones reservadas:", habitaciones_reservadas)

#ejercicio de prueba
reservar_habitacion(101)
reservar_habitacion(102)
liberar_habitacion(101)
mostrar_disponibilidad()
reservar_habitacion(103)
mostrar_disponibilidad()