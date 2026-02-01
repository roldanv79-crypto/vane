# 1 ejercicio

def calcular_promedio_inteligente():
    print("--- Sistema de Promedios Inteligentes ---")
    
    entrada = input("Ingresa las notas separadas por un espacio (ej: 85 70 45): ")
    
    notas = [float(n) for n in entrada.split()]
    
    if not notas:
        print("No ingresaste ninguna nota.")
        return
    
    suma_total = 0
    for nota in notas:
        suma_total += nota
    
    promedio = suma_total / len(notas)
    
    print(f"\nTu promedio final es: {promedio:.2f}")
    
    if promedio > 60:
        print("Resultado: **Aprobado**")
    else:
        print("Resultado: **Reprobado**")

calcular_promedio_inteligente()

# 2 ejercicio

def es_par_y_multiplo_de_3(numero):
    """Determina si un número cumple ambas condiciones."""
    return numero % 2 == 0 and numero % 3 == 0

print("Números que cumplen la condición:")
for i in range(1, 101):
    if es_par_y_multiplo_de_3(i):
        print(f"El número {i} es par y múltiplo de 3.")

# 3 ejercicio 

password_correcta = "vanessa"
intentos_maximos = 3
contador = 0

print("--- Sistema de Login Seguro ---")

while contador < intentos_maximos:
    
    password_ingresada = input(f"Intento {contador + 1}/{intentos_maximos} - Ingresa tu contraseña: ")
    
    if password_ingresada == password_correcta:
        print("\n¡Acceso concedido!")
        print("Bienvenido al sistema, usuario. ¡Qué gusto verte!")
        break  
    
    contador += 1
    
    if contador < intentos_maximos:
        print("Contraseña incorrecta. Inténtalo de nuevo.\n")
    else:
        print("\nAcceso bloqueado. Has agotado tus 3 intentos.")

# 4 ejercicio

# 1 km es aprox. 0.621371 millas
def conversor_selectivo(lista_km):
    millas = []
    for km in lista_km:
        
        if km > 0:
            resultado = km * 0.621371
            millas.append(round(resultado, 2))
    return millas

entrada = input("Ingresa las distancias en km separadas por espacios: ")

try:
    
    lista_km = [float(n) for n in entrada.split()]

    if any(n <= 0 for n in lista_km):
        print("Error: Se detectaron distancias menores o iguales a cero.")
    
    resultado = conversor_selectivo(lista_km)
    print(f"Resultado de la conversión: {resultado}")

except ValueError:
    print("Error: Ingresa únicamente números.")

# 5 ejercicio

def buscador_de_letras():
    
    frase = input("Introduce una frase: ")
    busqueda = input("Introduce la letra a buscar: ")

    contador = 0

    for letra in frase:
        if letra.lower() == busqueda.lower():
            contador += 1
    
    if len(busqueda) != 1:
        print(" Error: Debes introducir exactamente UN carácter.")
    
    elif contador > 0:
        print(f" ¡Éxito! La letra '{busqueda}' aparece {contador} veces.")
    
    else:
        print(f" Error: La letra '{busqueda}' no existe en la frase.")

buscador_de_letras()

# 6 ejercicio

def salto_de_multiplos():
    
    for numero in range(1, 21):
        
        if numero % 4 == 0:
            
            continue 
        
        elif numero % 2 == 0:
            print(f"{numero} - Es par (pero no múltiplo de 4)")
            
        else:
            print(f"{numero} - Es impar")

salto_de_multiplos()

# 7 ejercicio

inventario = {
    "manzanas": 10,
    "pan": 5,
    "leche": 0,
    "café": 8
}

def procesar_pedido(pedido):
    print("--- Iniciando validación de pedido ---")
    
   
    posible_venta = True
    
    for producto in pedido:
        if producto not in inventario:
            print(f" Error: El producto '{producto}' no existe en nuestro catálogo.")
            posible_venta = False
        elif inventario[producto] <= 0:
            print(f" Agotado: No queda stock de '{producto}'.")
            posible_venta = False
        else:
            print(f" Disponible: '{producto}' (Stock: {inventario[producto]})")

    if posible_venta:
        print("\nPROCESANDO DESCUENTO...")
        for producto in pedido:
            inventario[producto] -= 1
        print(" Venta completada con éxito. Stock actualizado.")
    else:
        print("\n Pedido cancelado: Faltan artículos o hay errores en la lista.")

orden_cliente = ["manzanas", "café", "pan"]

print("Estado inicial:", inventario)
procesar_pedido(orden_cliente)
print("Estado final:", inventario)

# 8 ejercicio

def encontrar_primos(limite):
    primos = []

    for num in range(2, limite + 1):
        es_primo = True
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False  
                break
      
        if es_primo:
            primos.append(num)
        else:
            continue 
            
    return primos

limite_usuario = 50
resultado = encontrar_primos(limite_usuario)
print(f"Los números primos hasta el {limite_usuario} son: {resultado}")

# 9 ejercicio

def calcular_iva(precio):
    """Calcula el precio final aplicando el IVA correspondiente."""
   
    if precio > 100:
        tasa = 0.16  
    else:
        tasa = 0.08 
    
    precio_final = precio + (precio * tasa)
    return precio_final, tasa * 100

precios_productos = [50, 120, 85, 250, 10]

print("--- Resumen de Facturación ---")

for p in precios_productos:
    total, porcentaje = calcular_iva(p)
    print(f"Precio base: ${p} | IVA: {porcentaje:.0f}% | Total: ${total:.2f}")

# 10 ejercicio

saldo = 1000.0

while True:
    print("\n--- MENÚ DE CAJERO ---")
    print("1. Ver saldo")
    print("2. Retirar")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print(f"Tu saldo actual es: ${saldo}")
    
    elif opcion == "2":
       
        monto_retiro = float(input("¿Cuánto deseas retirar?: "))
        
        if monto_retiro > saldo:
            print(" Error: Fondos insuficientes.")
        elif monto_retiro <= 0:
            print(" Por favor, ingresa un monto válido.")
        else:
            saldo -= monto_retiro
            print(f" Retiro exitoso. Tu nuevo saldo es: ${saldo}")
            
    elif opcion == "3":
        print("Gracias por usar el cajero. ¡Hasta pronto!")
        break 
    
    else:
        print(" Opción no válida, intenta de nuevo.")

# 11 ejercicio

import re

def es_nombre_valido(nombre):
    """
    Valida que el nombre tenga al menos 2 letras y no sea solo números o basura.
    """
    
    if len(nombre) < 2:
        return False
    
    return nombre.isalpha()

def limpiar_usuarios(lista_sucia):
    nombres_limpios = []
    
    for entrada in lista_sucia:
        
        paso1 = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ ]', '', entrada)
        
        
        paso2 = " ".join(paso1.split())
        
        
        nombre_final = paso2.title()
        
       
        if es_nombre_valido(nombre_final.replace(" ", "")):
            nombres_limpios.append(nombre_final)
        else:
            print(f" Entrada rechazada: '{entrada}' no parece un nombre real.")
            
    return nombres_limpios

usuarios_crudos = ["  jua#n perez  ", "m4ria_lopez", "12345", "  An@a  ", "b", "LUIS!!!"]

resultado = limpiar_usuarios(usuarios_crudos)

print("\n Lista Final Limpia:")
print(resultado)

# 12 ejercicio

def filtrar_espejos(lista_palabras):
    palindromos_validos = []

    for palabra in lista_palabras:
        #
        palabra_limpia = palabra.lower().strip()
        
        palabra_invertida = palabra_limpia[::-1]

        if palabra_limpia != palabra_invertida:
           
            continue
        elif len(palabra_limpia) <= 5:
            
            print(f" '{palabra_limpia}' es palíndromo pero mide 5 o menos letras.")
        else:
            
            palindromos_validos.append(palabra_limpia)
            print(f" '{palabra_limpia}' ha sido capturada por el espejo.")

    return palindromos_validos

candidatos = ["reconocer", "ana", "rayar", "sometemos", "python", "luz azul", "ojo"]

resultado = filtrar_espejos(candidatos)

print("\n Palíndromos de más de 5 letras encontrados:")
print(resultado)

# 13 ejercicio

def calcular_factorial(n):
    """Calcula el factorial de un número n usando un acumulador."""
    acumulador = 1

    for i in range(1, n + 1):
        acumulador *= i
    return acumulador

while True:
    entrada = input("Introduce un número entero positivo: ")
    
    if not entrada.isdigit():
        print(" Eso no es un número. Inténtalo de nuevo.")
    else:
        numero = int(entrada)
        
        if numero < 0:
            print(" Por favor, introduce un número mayor o igual a cero.")
        elif numero == 0:
            print("El factorial de 0 es por definición 1.")
            break
        else:
            
            resultado = calcular_factorial(numero)
            print(f" El factorial de {numero} es: {resultado}")
            break

# 14 ejercicio

def calcular_nomina(empleados, pago_por_hora):
    nomina_final = []
    
    for empleado in empleados:
        nombre = empleado['nombre']
        horas = empleado['horas_trabajadas']
        
        if horas > 40:
            horas_normales = 40
            horas_extra = horas - 40
            sueldo = (horas_normales * pago_por_hora) + (horas_extra * (pago_por_hora * 2))
            tipo_pago = "Con horas extra"
        elif horas > 0:
            sueldo = horas * pago_por_hora
            tipo_pago = "Jornada estándar"
        else:
            sueldo = 0
            tipo_pago = "Sin horas registradas"
            
        nomina_final.append({
            "empleado": nombre,
            "sueldo_total": sueldo,
            "observacion": tipo_pago
        })
        
    return nomina_final

lista_empleados = [
    {"nombre": "Ana", "horas_trabajadas": 45},  # 40 normales + 5 extra
    {"nombre": "Luis", "horas_trabajadas": 38}, # Solo normales
    {"nombre": "Pedro", "horas_trabajadas": 40},# Límite exacto
    {"nombre": "Marta", "horas_trabajadas": 0}  # Caso borde
]

pago_base = 20  # Precio por hora
resultados = calcular_nomina(lista_empleados, pago_base)

for r in resultados:
    print(f"Empleado: {r['empleado']} | Sueldo: ${r['sueldo_total']} | ({r['observacion']})")

#  15 ejercicio

def filtrar_correos(lista_emails):
    correos_validos = []
    correos_invalidos = []

    for email in lista_emails:
        email_limpio = email.strip()

       
        if "@" in email_limpio and email_limpio.endswith(".com") and " " not in email_limpio:
            correos_validos.append(email_limpio)
        elif " " in email_limpio:
            correos_invalidos.append(f"{email_limpio} (Razón: Contiene espacios)")
        else:
            correos_invalidos.append(f"{email_limpio} (Razón: Formato inválido)")

    return correos_validos, correos_invalidos

base_datos = [
    "usuario@test.com", 
    "mal-email.com", 
    "persona@empresa.org", 
    "con espacio@web.com", 
    "contacto@web.com"
]

validos, rechazados = filtrar_correos(base_datos)

print(f" Correos Válidos: {validos}")
print(f" Correos Rechazados: {rechazados}")

# 16 ejercicio

import random

def jugar_adivinanza():
    
    numero_secreto = random.randint(1, 100)
    vidas = 10
    ganaste = False

    print("--- 🤖 ¡Bienvenido al Desafío de Adivinanza! ---")
    print("He pensado un número entre 1 y 100. Tienes 10 vidas para descubrirlo.")

    while vidas > 0:
        print(f"\n Vidas restantes: {vidas}")
        
        try:
            intento = int(input("Introduce tu número: "))
        except ValueError:
            print(" ¡Cuidado! Debes ingresar un número válido.")
            continue

        if intento == numero_secreto:
            print(f" ¡Felicidades! Has adivinado el número {numero_secreto}.")
            ganaste = True
            break
        elif intento > numero_secreto:
            print(" Muy alto. Intenta con uno más pequeño.")
        else:
            print(" Muy bajo. Intenta con uno más grande.")
        
        vidas -= 1

    if not ganaste:
        print(f"\n Te has quedado sin vidas. El número era {numero_secreto}. ¡Suerte la próxima!")

if __name__ == "__main__":
    jugar_adivinanza()

# 17 ejercicio

def procesar_descuentos(lista_compras):
    print("\n" + "="*40)
    print("RESUMEN DE DESCUENTOS APLICADOS")
    print("="*40)
    
    for producto, categoria, precio in lista_compras:
        
        if categoria == "electronica":
            tasa = 0.30  
        elif categoria == "ropa":
            tasa = 0.20  
        elif categoria == "alimentos":
            tasa = 0.10  
        else:
            tasa = 0.0   
            
        precio_final = precio * (1 - tasa)
        print(f"🔹 {producto.capitalize()} ({categoria}): ${precio} -> ${precio_final:.2f}")


inventario_usuario = []

print("🛍️ Bienvenido al Sistema de Facturación")

while True:
    nombre = input("\nIngrese el nombre del producto (o 'salir' para terminar): ").lower()
    if nombre == 'salir':
        break
        
    cat = input(f"Ingrese categoría para {nombre} (electronica/ropa/alimentos): ").lower()
    valor = float(input(f"Ingrese el precio de {nombre}: "))
    
    inventario_usuario.append((nombre, cat, valor))

if inventario_usuario:
    procesar_descuentos(inventario_usuario)
else:
    print("No se ingresaron productos.")


# 18 ejercicio

def analizar_texto_dinamico():
    
    texto = input("Introduzca el párrafo que desea analizar: ")
    
    
    if not texto.strip():
        print(" No ingresaste ningún texto.")
        return

    for signo in ".,;:!?":
        texto = texto.replace(signo, "")

    palabras = texto.split()
    palabras_largas = []


    for p in palabras:
        longitud = len(p)
        
        if longitud > 7:
            palabras_largas.append(p)
        elif longitud == 0:
          
            continue
        else:
            
            pass

    print("\n--- Resultados del Análisis ---")
    if len(palabras_largas) > 0:
        print(f" Se encontraron {len(palabras_largas)} palabras con más de 7 letras:")
        print(palabras_largas)
    else:
        print(" No se encontraron palabras que superen las 7 letras.")

analizar_texto_dinamico()

# 19 ejercicio

def binario_a_decimal(binario_str):
    
    decimal = 0
    
    binario_str = binario_str[::-1]
    
    for i in range(len(binario_str)):
        digito = binario_str[i]
        
        
        if digito not in ('0', '1'):
            return f" Error: '{digito}' no es un dígito binario válido."
        
        if digito == '1':
            
            decimal += 2**i
            
    return f" El equivalente decimal es: {decimal}"

numero_usuario = input("Introduce un número binario: ")
resultado = binario_a_decimal(numero_usuario)
print(resultado)

# 20 ejercicio

def gestionar_permisos(usuarios_db):
    print(f"--- Reporte de Acciones Disponibles ---")
    
    
    for usuario in usuarios_db:
        nombre = usuario["nombre"]
        rango = usuario["rango"]
        
       
        if rango == "Admin":
            accion = "Permiso total: Puede BORRAR y EDITAR contenido. 🗑️"
        elif rango == "Editor":
            accion = "Permiso parcial: Solo puede EDITAR contenido. ✍️"
        else:
            accion = "Permiso denegado: Solo puede VER contenido. 👀"
            
        print(f"Usuario: {nombre} [{rango}] -> {accion}")

base_datos = [
    {"nombre": "Ana", "rango": "Admin"},
    {"nombre": "Pedro", "rango": "Editor"},
    {"nombre": "Lucía", "rango": "Invitado"}
]

gestionar_permisos(base_datos)
