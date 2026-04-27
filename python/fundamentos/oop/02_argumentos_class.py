class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

# Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 20000)
ale = Usuario("Alexander", "Pino", "alexander@gmail.com", 5000, 10000)

# Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel


# -----------------------------------
# --- Tarea rápida
'''
Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancias para la clase con distintos estudiantes
- Imprimir el nombre y apellido concatenado + especialidad
'''

class Estudiante:
    def __init__(self, nombre, apellido, rut, especialidad, fecha_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

# Creación de instancias
Mía = Estudiante("Mía", "Khalifa", "67.567.100-5", "Recursos humanos", "13/11/2009")
Jeffry = Estudiante("Jeffry", "Epstein", "26.267.270-6", "Programación", "12/12/2009")
Marco = Estudiante("Marco", "Antonio", "29.458.070-4", "logistica", "16/02/2006")

# Imprimir
print(f"{Mía.nombre} {Mía.apellido} estudia: {Mía.especialidad}")
print(f"{Jeffry.nombre} {Jeffry.apellido} estudia: {Jeffry.especialidad}")
print(f"{Marco.nombre} {Marco.apellido} estudia: {Marco.especialidad}")