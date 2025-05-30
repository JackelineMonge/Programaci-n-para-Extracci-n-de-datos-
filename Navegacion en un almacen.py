# Nombre completo: Jackeline Monge Nunez
# Grupo: 951
# Fecha de realización: 11 de Febrero del 2025
# Descripción: Este ejercicio simula un robot que se mueve en un almacén representado como
# una matriz. El robot debe recoger productos y retornar al punto de inicio sin chocar con obstáculos.

# Función para verificar si los movimientos son correctos
def verificar_recogida_productos(almacen, movimientos):

    x, y = 0, 0
    productos = 0
    productos_recogidos = 0
    filas = len(almacen)
    columnas = len(almacen[0])


    if almacen[x][y] == 'P':
        productos_recogidos += 1


    for movimiento in movimientos:
        if movimiento == 'R':
            y += 1
        elif movimiento == 'D':
            x += 1
        elif movimiento == 'L':
            y -= 1
        elif movimiento == 'U':
            x -= 1


        if 0 <= x < filas and 0 <= y < columnas and almacen[x][y] != '#':
            if almacen[x][y] == 'P':
                productos_recogidos += 1
        else:
            return False


    if productos_recogidos == sum(row.count('P') for row in almacen) and (x, y) == (0, 0):
        return True
    return False

# Ejemplo
almacen = [
    ['.', '.', '#', 'P'],
    ['.', '#', '.', '.'],
    ['P', '.', 'P', '.'],
    ['#', '.', '#', '.']
]
movimientos_correctos = ['D', 'D', 'R', 'R', 'U', 'R', 'U', 'D', 'L', 'D', 'L', 'L', 'U', 'U']
print(verificar_recogida_productos(almacen, movimientos_correctos))  # True
