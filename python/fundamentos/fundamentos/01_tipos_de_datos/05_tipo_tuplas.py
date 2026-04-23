#tuplasn ejemplo 
tupla_letras = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"
#cualquier tipo de dato
gato = ("Miu", 5, "persa", False)
print(gato[0]) #Imprime: Miu
#sonido gato
gato[0] = "Michi" #ERROR: TypeError: 'tuple' object does not support item assignment
gato = gato + ("4.1",)
print(gato) #Imprime: ('Miu', 5, 'persa', False, '4.1')
#tuplas dentro de funciones
def suma_multiplicaciones(x, y):
    suma = x + y
    multiplicacion = x * y
    return (suma, multiplicaciones)
    print(suma_multiplicaciones(10, 5))