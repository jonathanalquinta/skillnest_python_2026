#Creacion de la clase usuario - entidad
class Usuario:
    pass #Pronto pondremos métodos y atributos
    def __init__(self): #constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "millagihot@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0
        
#Instancias de una clase
miyagi = Usuario()  #variables
daniel = Usuario()  #variables 
Jonathan = Usuario()
print(miyagi.nombre)
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

# Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "larusso"
daniel.email = "danipitinchico@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

print(daniel.nombre)
print(daniel.apellido)
print(daniel.email)
print(daniel.limite_credito)
print(daniel.saldo_pagar)

#El Mio
Jonathan.nombre = "Jonathan"
Jonathan.apellido = "Aiyelef"
Jonathan.email = "Aiyelef@gmail.com"
Jonathan.limite_credito = 100000
Jonathan.saldo_pagar = 0

print(Jonathan.nombre)
print(Jonathan.apellido)
print(Jonathan.email)
print(Jonathan.limite_credito)
print(Jonathan.saldo_pagar)

#-------------------------------------
'''
crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancia para la clase con distintos estudiantes.
- Imprimir el nombre y apellido concatenando + especialidad.
'''
