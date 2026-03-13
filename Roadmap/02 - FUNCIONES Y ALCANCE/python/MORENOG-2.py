"""
Funciones definidas por el usuario
"""

# funcion Simple
def saludar():
    print("Hola, bienvenido a la programación")

saludar()

#Funcion con retorno
def return_saludar():
    return "Hola, bienvenido"

print(return_saludar())

#Funcion con un argumentos
def saludar_nombre(nombre):
    return f"Hola {nombre}, bienvenido a la programación"

print(saludar_nombre("rafael"))

#Funcion con varios argumentos
def saludar_nombre_apellido(nombre, apellido):
    return f"Hola {nombre} {apellido}, bienvenido a la programación"

print(saludar_nombre_apellido("Rafael", "moreno"))

#Funcion con argumentos predeterminados
def saludar_nombre_apellido_predeterminado(nombre="Rafael", apellido="Moreno"):
    return f"Hola {nombre} {apellido}, bienvenido a la programación"

print(saludar_nombre_apellido_predeterminado())
print(saludar_nombre_apellido_predeterminado("Carlos"))

#Funcion con argumnetos y argumentos
def retorno_args_greet(nombre, apellido):
    return f"Hola {nombre} {apellido}!"

print(retorno_args_greet("Rafael", "Moreno"))

#Con retorno de varios valores
def multiples_valores():
    return "rafael", "moreno"

nombre, apellido = multiples_valores()
print(nombre)
print(apellido)

# Con un numero variable de argumentos
def variable_args(*nombre):
    for nombre in nombre:
        print(f"Hola {nombre}, bienvenido a la programación")

variable_args("Rafael", "Carlos", "Ana")

# Con un numero variable de argumentos con clave
def variable_args_clave(**nombres):
    for parame, nombre in nombres.items():
        print(f"Hola {nombre} ({parame}), bienvenido a la programación")

variable_args_clave(lenguaje="Python", nombre="Rafael", apellido="Moreno", edad = 26)
