"""
Conexión y operaciones con base de datos MySQL para sistema de olimpic.
Autor: jackeline monge nunez

"""
from mysql.connector import connect, Error

class GestorConexion:
    @staticmethod
    def abrir_conexion():
        try:
            conexion = connect(
                host="localhost",
                user="root",
                password="",
                database="olimpics",
                port="3306"
            )
            print("Conexión realizada exitosamente")
            return conexion
        except Error as err:
            print(f"Fallo al conectar con la base de datos: {err}")

    @staticmethod
    def cerrar_conexion(conexion):
        if conexion:
            conexion.close()
            print("Conexión cerrada correctamente")


class TablaPaises:
    @staticmethod
    def agregar(conexion, nombre_pais):
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO pais (nombre) VALUES (%s)", (nombre_pais,))
            conexion.commit()
            print(f"Agregado: {nombre_pais}")

    @staticmethod
    def actualizar(conexion, id_pais, nombre_nuevo):
        with conexion.cursor() as cursor:
            cursor.execute(
                "UPDATE pais SET nombre = %s WHERE id = %s",
                (nombre_nuevo, id_pais)
            )
            conexion.commit()
            print(f"Actualizado el país con ID {id_pais} a {nombre_nuevo}")

    @staticmethod
    def eliminar(conexion, id_pais):
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM pais WHERE id = %s", (id_pais,))
            conexion.commit()
            print(f"País con ID {id_pais} eliminado")

    @staticmethod
    def listar(conexion, condicion=""):
        with conexion.cursor() as cursor:
            cursor.execute(f"SELECT * FROM pais {condicion}")
            return cursor.fetchall()


class TablaEventos:
    @staticmethod
    def agregar(conexion, anio_evento):
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO evento (year) VALUES (%s)", (anio_evento,))
            conexion.commit()
            print(f"Evento del año {anio_evento} registrado")

    @staticmethod
    def actualizar(conexion, id_evento, nuevo_anio):
        with conexion.cursor() as cursor:
            cursor.execute(
                "UPDATE evento SET year = %s WHERE id = %s",
                (nuevo_anio, id_evento)
            )
            conexion.commit()
            print(f"Evento con ID {id_evento} actualizado a {nuevo_anio}")

    @staticmethod
    def eliminar(conexion, id_evento):
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM evento WHERE id = %s", (id_evento,))
            conexion.commit()
            print(f"Evento con ID {id_evento} eliminado")

    @staticmethod
    def listar(conexion, condicion=""):
        with conexion.cursor() as cursor:
            cursor.execute(f"SELECT * FROM evento {condicion}")
            return cursor.fetchall()


class TablaResultados:
    @staticmethod
    def registrar(conexion, id_evento, id_pais, id_genero, oro, plata, bronce):
        with conexion.cursor() as cursor:
            sentencia = """INSERT INTO resultados 
                           (id_evento, id_pais, id_genero, oro, plata, bronce) 
                           VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sentencia, (id_evento, id_pais, id_genero, oro, plata, bronce))
            conexion.commit()
            print("Resultado registrado con éxito")

    @staticmethod
    def modificar(conexion, id_evento, id_pais, id_genero, oro, plata, bronce):
        if any(val < 0 for val in (oro, plata, bronce)):
            print("Error: Las cantidades de medallas no pueden ser negativas")
            return False

        with conexion.cursor() as cursor:
            consulta = """UPDATE resultados SET 
                          oro = %s, plata = %s, bronce = %s 
                          WHERE id_evento = %s AND id_pais = %s AND id_genero = %s"""
            cursor.execute(consulta, (oro, plata, bronce, id_evento, id_pais, id_genero))
            conexion.commit()
            print("Resultado modificado correctamente")
            return True

    @staticmethod
    def listar(conexion, filtro=""):
        with conexion.cursor() as cursor:
            cursor.execute(f"SELECT * FROM resultados {filtro}")
            return cursor.fetchall()


if __name__ == "__main__":
    try:
        conexion = GestorConexion.abrir_conexion()
        if conexion:
            # Países
            TablaPaises.agregar(conexion, "México")
            TablaPaises.actualizar(conexion, 1, "Estados Unidos")
            print(TablaPaises.listar(conexion, "WHERE id < 10"))

            # Eventos
            TablaEventos.agregar(conexion, "2024")
            print(TablaEventos.listar(conexion))

            # Resultados
            TablaResultados.registrar(conexion, 1, 1, 1, 5, 3, 2)
            print(TablaResultados.listar(conexion))

    finally:
        if 'conexion' in locals():
            GestorConexion.cerrar_conexion(conexion)
