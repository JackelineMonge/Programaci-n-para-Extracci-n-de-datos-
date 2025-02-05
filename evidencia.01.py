#EVIDENCIA 01
#Crear tres clases distintas:
   # 1.- Personas.
   #2.- Animales.
   # 3.- Vehiculos.
   
   #Agregar un mínimo de 3 atributos a cada uno que tengan sentido con la clase desarrollada.  
   
   #Finalmente, instanciar dos objetos distintos de cada clase, asignar los valores como argumentos para cada atributo y hacer un despliegue de estos.
   #Salida de ejemplo:
   #  Persona – Ocupación: Ingeniero.
   #  Persona – Edad: 50 años.
   # Persona – Nombre: Paquito.

class Personas:
    def __init__(self, apodo, estatura, peso):
        self.apodo=apodo
        self.estatura= estatura
        self.peso= peso
        
maria= Personas("marichuy", 1.60, 70.5)
print(maria.apodo)
print(maria.estatura)
print(maria.peso)

carlos= Personas("charlie", 1.80, 90.5)
print(carlos.apodo)
print(carlos.estatura)
print(carlos.peso)

valeria= Personas("vale", 1.50, 49.8)
print(valeria.apodo)
print(valeria.estatura)
print(valeria.peso)

class Animales:
    def __init__(self, nombre, color, alimentacion):
        self.nombre= nombre
        self.color= color
        self.alimentacion= alimentacion
jirafa= Animales("melisssa", "amarilla", "vegetariano")
print(jirafa.nombre)
print(jirafa.color)
print(jirafa.alimentacion)

oso= Animales("teddy", "cafe", "carnivoro")
print(oso.nombre)
print(oso.color)
print(oso.alimentacion)

class Vehiculos:
    def __init__(self, marca, color, cilindros):
        self.marca= marca
        self.color= color
        self.cilindros= cilindros
mazda= Vehiculos("mazda2", "rojo", "6")
print(mazda.marca)
print(mazda.color)
print(mazda.cilindros)

nissan= Vehiculos("versa", "azul", "4")
print(nissan.marca)
print(nissan.color)
print(nissan.cilindros)
 
