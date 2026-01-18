nombre_usuario = "Vanessa"
edad = 33
fecha_nacimiento = "02/12/92"
print(nombre_usuario)
print(edad)
print(fecha_nacimiento)
print(f"mi nombre es {nombre_usuario}, tengo {edad} años y naci el {fecha_nacimiento} ") 

#1 area de rectangulo
calculo_area_rectangulo = "(base, altura)" 
base = 5
altura = 10
base = int(input("base del rectangulo"))
altura = int(input("altura del rectangulo"))
area = base * altura 
print(f"El área del rectángulo es:{area}")

#2 conversor de temperatura
celsius = C = 10 
C = float(input("temperatura en celsius:"))
F = (C * (9/5)) + 32
print (f"la temperatura en Fahrenheit es:{F}")

#3 concatenacion de cadenas
nombre_apellido = input("ingrese sus nombres:")
print("el nombre y apellido es"+ "" + nombre_apellido) 

#5 Elegibilidad para votar
edad_usuario= input ("ingresa edad")
edad= int(edad_usuario)

if edad >= 18:
    print("la persona es mayor de edad")
else: 
    print(" la persona es menor de edad") 

#4 verificador de numero par o impar
numero = int(input("introduce un numero"))
if numero % 2 == 0:
    print("el numero es par")
else: 
    print("el numero es impar")
    
#6 comparador de numeros
numero_1 = float(input("primer número: "))
numero_2 = float(input("segundo número: "))

if numero_1 > numero_2:
    print(f"{numero_1} es mayor que {numero_2}")
elif numero_1 < numero_2:
    print(f"{numero_1} es menor que {numero_2}")
else:
    print(f"{numero_1} es igual a {numero_2}")

#7 operadores logicos
numero = int(input("Introduce un número: "))
if numero >= 10 and numero <= 20: 
    print(f"El número {numero} está entre 10 y 20.")
else:
    print(f"El número {numero} no está entre 10 y 20.")

#8 verificacion de contraseña simple
contraseña = "123456"
contraseña_usuario = input("Introduce la contraseña: ")

if contraseña == contraseña_usuario:
    print("Contraseña correcta.")
else:
    print("Contraseña incorrecta.")

#9 calculadora de descuento

precio_original = float(input("Introduce el precio del producto:"))
descuento_porcentaje = 0.15
umbral_precio = 100

if precio_original > umbral_precio:
    # Si el precio supera los $100, calcular el descuento
    descuento_aplicado = precio_original * descuento_porcentaje
    precio_final = precio_original - descuento_aplicado
    print(f"¡Se aplica un {descuento_porcentaje*100}% de descuento!")
    print(f"Precio original: {precio_original:.2f}")
    print(f"Descuento aplicado: {descuento_aplicado:.2f}")
    print(f"Precio final a pagar: {precio_final:.2f}")
else:
    # Si no supera los $100, no hay descuento
    precio_final = precio_original
    print("El precio no supera los $100, no se aplica descuento.")
    print(f"Precio final a pagar: ${precio_final:.2f}")

#10 Clasificador de Números ➕➖
numero = float(input("Ingresa un número"))

if numero > 0:
    print(f"El número {numero} es POSITIVO.")
elif numero < 0:
    print(f"El número {numero} es NEGATIVO.")
else:
    print(f"El número es CERO.")

#11 año bisiesto
año = int(input("Introduce un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")     
else:
    print(f"El año {año} no es bisiesto.")

#12 calculadora de calificaciones
nota = int(input("Ingresar tu nota (0-100): "))

if nota >= 90:
    print("Tu calificación es: A")
elif nota >= 80: 
    print("Tu calificación es: B")
elif nota >= 70: 
    print("Tu calificación es: C")
elif nota >= 60: 
    print("Tu calificación es: D")
else: 
    print("Tu calificación es: F")

#13 verificador de vocal y consonante
letra = input("Introduce una letra: ").lower()
if letra in 'aeiou':
    print(f"La letra '{letra}' es una vocal.")        
elif "a" <= letra <= "z":
    print(f"la letra '{letra}' es una consonante.")
else:
    print(f"esto'{letra}' no es una letra del abecedario.")


#14 seleccion de menu
menu = int(input("Elige una opcion del menu (1-3): "))

if menu == 1:
    print("Has elegido el menu 1. pasta")
elif menu == 2:
    print("Has elegido el menu 2. hamburguesa")
elif menu == 3:
    print("Has elegido el menu 3. pizza")
else:
    print("menu no válido.")

#15 tipo de triangulo
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

if a == b == c:
    print("El triángulo es equilátero.")
elif a == b or a == c or b == c:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")

#16 el mayor de tres numeros
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if (num1 >= num2) and (num1 >= num3):
    mayor = num1
elif (num2 >= num1) and (num2 >= num3):
    mayor = num2
else:
    mayor = num3

print(f"El número más grande es: {mayor}")

#17 calculadora IMC
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 25:
    print("Normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")

#18 calculadora de costo de envio
peso = float(input("Introduce el peso del paquete en kg: "))
zona = input("Introduce la zona de destino (local, nacional, internacional): ").lower()
if zona == "local":
    if peso <= 5:
        costo = 5.00
    else:
        costo = 10.00
elif zona == "nacional":
    if peso <= 5:
        costo = 10.00
    else:
        costo = 20.00
elif zona == "internacional":
    if peso <= 5:
        costo = 20.00
    else:
        costo = 40.00
else:
    costo = 0
    print("Zona no válida.")
if costo > 0:
    print(f"El costo de envío es: ${costo:.2f}")

#19 Resolucion de ecuacion cuadratica
import math
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))    
c = float(input("Introduce el coeficiente c: "))
discriminante = b**2 - 4*a*c
if discriminante > 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Dos soluciones reales: {raiz1} y {raiz2}")
elif discriminante == 0:
    raiz = -b / (2*a)
    print(f"Una solución real: {raiz}")
else:
    print("No hay soluciones reales.")


#20 Juego: Piedra, Papel o Tijera
jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()
if jugador1 == jugador2:
    print("Empate.")    
elif jugador1 == "piedra":
    if jugador2 == "tijera":
        print("Jugador 1 gana.")
    else:
        print("Jugador 2 gana.")
elif jugador1 == "papel":
    if jugador2 == "piedra":
        print("Jugador 1 gana.")
    else:
        print("Jugador 2 gana.")
elif jugador1 == "tijera":
    if jugador2 == "papel":
        print("Jugador 1 gana.")
    else:
        print("Jugador 2 gana.")
else:
    print("Jugada no válida.")
