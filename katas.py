# Ejercicio 1: Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(cadena):
    # Eliminamos los espacios y convertimos a minúsculas para evitar diferencias entre mayúsculas y minúsculas
    cadena = cadena.replace(" ", "").lower()
    # Creamos un diccionario para almacenar las frecuencias
    frecuencias = {}
    for letra in cadena:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1
    return frecuencias

# Ejemplo de uso
print(frecuencia_letras("Hola mundo"))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 2: Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

def doble_valores(lista):
    return list(map(lambda x: x * 2, lista))

# Ejemplo de uso
print(doble_valores([2, 4, 6, 8]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3: Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, objetivo):
    return [palabra for palabra in lista_palabras if objetivo in palabra]

# Ejemplo de uso
lista = ["hola", "adios", "halo", "saludo"]
print(filtrar_palabras(lista, "al"))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 4: Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función zip().

def diferencia_listas(lista1, lista2):
    return [a - b for a, b in zip(lista1, lista2)]

# Ejemplo de uso
lista1 = [5, 10, 15]
lista2 = [1, 2, 3]
print(diferencia_listas(lista1, lista2))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 5: Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def calcular_media_estado(lista, nota_aprobado = 5):
    if not lista:
        return 0, "suspenso"  # Si la lista está vacía, devolvemos 0 y "suspenso"
    media = sum(lista) / len(lista)
    if media >= 5:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return media, estado

# Ejemplo de uso
media1 = [4, 5, 6]
media2 = [1, 2, 3]
print(calcular_media_estado(media1))
print(calcular_media_estado(media2))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 6: Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1  # Caso base: el factorial de 0 y 1 es 1	
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
print(factorial(5))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 7: Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda x: " ".join(map(str, x)), lista_tuplas))

# Ejemplo de uso
print(tuplas_a_strings([(1, 2), (3, 4), (5, 6)]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 8: Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir_numeros():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 / num2
        print(f"La división fue exitosa. Resultado: {resultado}")
    except ValueError:
        print("Error: Ingresa valores numéricos.")
    except ZeroDivisionError: 
        print("Error: No se puede dividir por cero.")
    except Exception: # Si por alguna razón no es una excepción conocida, se ejecuta este bloque. 
        print("Error inesperado.")

# Ejemplo de uso
dividir_numeros()

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 9: Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda x: x not in prohibidas, lista_mascotas))

# Ejemplo de uso
print(filtrar_mascotas(["Perro", "Gato", "Mapache", "Cocodrilo"]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 10: Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception): # Creamos una excepción personalizada
    pass

def calcular_promedio(lista):
    if not lista:
        raise ListaVaciaError("La lista está vacía.")
    return sum(lista) / len(lista)

# Ejemplo de uso
try:
    print(calcular_promedio([1, 2, 3, 4]))
    print(calcular_promedio([]))
except ListaVaciaError as e:
    print(e)

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 11: Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        else:
            print(f"Edad introducida: {edad}")
    except ValueError as e:
        print(f"Error: {e}")

# Ejemplo de uso
pedir_edad()

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 12: Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map().

def longitud_palabras(frase):
    return list(map(len, frase.split()))

# Ejemplo de uso
print(longitud_palabras("Hola mundo Python"))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 13: Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

def mayusculas_minusculas(caracteres):
    return list(map(lambda x: (x.upper(), x.lower()), set(caracteres)))

# Ejemplo de uso
print(mayusculas_minusculas("abcABC"))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 14: Crea una función que retorne las palabras de una lista de palabras que comience con una letra en específico. Usa la función filter().

def palabras_que_comienzan_con(lista_palabras, letra):
    return list(filter(lambda x: x.startswith(letra), lista_palabras))

# Ejemplo de uso
print(palabras_que_comienzan_con(["hola", "adios", "halo", "saludo"], "h"))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 15: Crea una función que sume 3 a cada número de una lista dada.

def sumar_tres(lista):
    return list(map(lambda x: x + 3, lista))

# Ejemplo de uso
print(sumar_tres([1, 2, 3, 4]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 16: Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def palabras_mas_largas_que(cadena, n):
    return list(filter(lambda x: len(x) > n, cadena.split()))

# Ejemplo de uso
print(palabras_mas_largas_que("Hola mundo Python es genial", 4))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 17: Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572).

def lista_a_numero(lista_digitos):
    return int("".join(map(str, lista_digitos)))

# Ejemplo de uso
print(lista_a_numero([5, 7, 2]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 18: Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90.

estudiantes = [
    {"nombre": "Carlos", "edad": 25, "calificación": 95},
    {"nombre": "Arturo", "edad": 22, "calificación": 85},
    {"nombre": "Samantha", "edad": 31, "calificación": 90},
    {"nombre": "Adrian", "edad": 18, "calificación": 53},
]

def estudiantes_excelentes(estudiantes):
    return list(filter(lambda x: x["calificación"] >= 90, estudiantes))

# Ejemplo de uso
print(estudiantes_excelentes(estudiantes))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 19: Crea una función que filtre los números impares de una lista dada.

def filtrar_impares(lista):
    return list(filter(lambda x: x % 2 != 0, lista))

# Ejemplo de uso
print(filtrar_impares([1, 2, 3, 4, 5]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 20: Para una lista con elementos tipo integer y string, obtén una nueva lista sólo con los valores int. Usa la función filter().

def filtrar_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

# Ejemplo de uso
print(filtrar_enteros([1, "a", 2, "b", 3]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 21: Crea una función que calcule el cubo de un número dado.

def cubo(numero):
    return numero ** 3

# Ejemplo de uso
print(cubo(10))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 22: Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce().

from functools import reduce

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

# Ejemplo de uso
print(producto_total([1, 2, 3, 4]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 23: Concatena una lista de palabras. Usa la función join().

def concatenar_palabras(lista_palabras):
    return " ".join(lista_palabras)

# Ejemplo de uso
print(concatenar_palabras(["Hola", "mundo", "Python"]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 24: Calcula la diferencia total en los valores de una lista. Usa la función reduce().

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

# Ejemplo de uso
print(diferencia_total([10, 2, 3]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 25: Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    return len(cadena)

# Ejemplo de uso
print(contar_caracteres("Hola mundo"))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 26: Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y

# Ejemplo de uso
print(resto(10, 3))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 27: Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    return sum(lista) / len(lista)

# Ejemplo de uso
print(promedio([1, 2, 3, 4]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 28: Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    elementos_vistos = set() # Conjunto para almacenar elementos vistos
    for elemento in lista:
        if elemento in elementos_vistos:
            return elemento
        elementos_vistos.add(elemento)
    return None # Si no hay duplicados, devolvemos None

# Ejemplo de uso
print(primer_duplicado([1, 2, 3, 4, 2, 5]))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 29: Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter "#", excepto los últimos cuatro.

def enmascarar_texto(texto):
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]

# Ejemplo de uso
print(enmascarar_texto("1234567890"))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 30: Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)
# Ejemplo de uso
palabra1 = "rosa"
palabra2 = "aros"
if son_anagramas(palabra1, palabra2):
    print("Son anagramas")
else:
    print("No son anagramas")

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 31: Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre(lista, nombre):
    if nombre in lista:
        print(f"El nombre {nombre} fue encontrado.")
    else:
        raise ValueError(f"El nombre {nombre} no está en la lista.")

# Ejemplo de uso
lista_nombres = ["Juan", "Ana", "Luis"]
nombre_buscar = "Ana"
try:
    buscar_nombre(lista_nombres, nombre_buscar)
except ValueError as e:
    print(e)

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 32: Escribe una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelva el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado['nombre'] == nombre_completo:
            return empleado['puesto']
    return "La persona no trabaja aquí."

# Ejemplo de uso
empleados = [
    {"nombre": "Juan Perez", "puesto": "Desarrollador"},
    {"nombre": "Ana Gomez", "puesto": "Diseñadora"}
]
print(buscar_puesto("Juan Perez", empleados))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 33: Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: [x + y for x, y in zip(lista1, lista2)]

# Ejemplo de uso
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(sumar_listas(lista1, lista2))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 34: Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: crecer_tronco, nueva_rama, crecer_ramas, guitar_rama e info_arbol. El objetivo es implementar estos métodos para manipular la estructura del árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def guitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "ramas": len(self.ramas),
            "longitud_ramas": self.ramas
        }

# Ejemplo de uso
arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.guitar_rama(1)
print(arbol.info_arbol())

#----------------------------------------------------------------------------------------------------------------------------

# No hay ejercicio 35 ?

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 36: Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, tiene_cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.tiene_cuenta_corriente = tiene_cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo.")
        self.saldo -= cantidad
        otro_usuario.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# Ejemplo de uso
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)
bob.transferir_dinero(alicia, 80)
alicia.retirar_dinero(50)
print(f"Saldo de Alicia: {alicia.saldo}")
print(f"Saldo de Bob: {bob.saldo}")

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 37: Crea una función llamada `procesar_texto` que procesa un texto según la opción especificada: `contar_palabras`, `reemplazar_palabras`, `eliminar_palabra`. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función `procesar_texto`.

def contar_palabras(texto):
    palabras = texto.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    return " ".join([p for p in texto.split() if p != palabra])

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida.")

# Ejemplo de uso
texto = "Hola mundo Hola"
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "Hola", "Adiós"))
print(procesar_texto(texto, "eliminar", "Hola"))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 38: Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def determinar_hora(hora):
    if 6 <= hora < 12:
        return "Es de día."
    elif 12 <= hora < 18:
        return "Es tarde."
    else:
        return "Es de noche."

# Ejemplo de uso
hora = int(input("Ingresa la hora (0-23): "))
print(determinar_hora(hora))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 39: Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente

def calificacion_texto(calificacion):
    if 0 <= calificacion <= 69:
        return "Insuficiente"
    elif 70 <= calificacion <= 79:
        return "Bien"
    elif 80 <= calificacion <= 89:
        return "Muy bien"
    elif 90 <= calificacion <= 100:
        return "Excelente"
    else:
        return "Calificación no válida."

# Ejemplo de uso
print(calificacion_texto(85))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 40: Escribe una función que tome dos parámetros: `figura` (una cadena que puede ser "rectangular", "circulo" o "triangular") y `datos` (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    if figura == "rectangular" or figura == "cuadrado":
        return datos[0] * datos[1]
    elif figura == "circulo":
        return math.pi * (datos[0] ** 2)
    elif figura == "triangular":
        return (datos[0] * datos[1]) / 2
    else:
        raise ValueError("Figura no válida.")

# Ejemplo de uso
cadena_figuras = ["rectangular", "circulo", "triangular"]
datos_necesarios = (5, 10)
print(calcular_area(cadena_figuras[0], datos_necesarios))

#----------------------------------------------------------------------------------------------------------------------------

# Ejercicio 41: Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero).
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.

def calcular_descuento():
    precio = float(input("Ingresa el precio original del artículo: "))
    tiene_cupon = input("¿Tienes un cupón de descuento? (Sí/No): ").lower()
    
    if tiene_cupon == "sí":
        descuento = float(input("Ingresa el porcentaje del cupón de descuento: "))
        if descuento > 0:
            precio *= (100 - descuento)
        else:
            print("El valor del cupón no es válido.")
    
    print(f"Precio final: {precio}")

# Ejemplo de uso
calcular_descuento()

