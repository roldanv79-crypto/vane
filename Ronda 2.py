# Ejercicio 21

def fibonacci_pares(n):
    
    a, b = 0, 1
    pares = []

    while a <= n:
        if a % 2 == 0:
            pares.append(a)
        else:        
            pass 

        a, b = b, a + b
        
    return pares

limite = 100
resultado = fibonacci_pares(limite)
print(f"Números de Fibonacci pares hasta {limite}: {resultado}")

# Ejercicio 22 

def procesar_radar(velocidades):
    print(f"{'Velocidad':<15} | {'Estado':<20} | {'Multa'}")
    print("-" * 50)
    
    for v in velocidades:
       
        if v > 120:
            estado = "Exceso Grave"
            multa = "$500"
        elif v >= 100:
            estado = "Exceso Moderado"
            multa = "$200"
        else:
            estado = "Bajo el límite"
            multa = "$0"
        
        print(f"{v:>3} km/h        | {estado:<20} | {multa}")

registro_autopista = [90, 115, 130, 100, 85, 121, 45]
procesar_radar(registro_autopista)

# Ejercicio 23

def limpiar_duplicados(lista_sucia):
    lista_limpia = []
    
    for numero in lista_sucia:
        
        if numero not in lista_limpia:
            lista_limpia.append(numero)
        else:
            pass 
            
    return lista_limpia

numeros_repetidos = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 3]

resultado = limpiar_duplicados(numeros_repetidos)

print(f"Lista original: {numeros_repetidos}")
print(f"Lista sin duplicados: {resultado}")

# Ejercicio 24

def calcular_tiempo_duplicacion(capital_inicial, interes_anual):
    capital_actual = capital_inicial
    objetivo = capital_inicial * 2
    anios = 0
    
    while capital_actual < objetivo:
        
        capital_actual += capital_actual * (interes_anual / 100)
        anios += 1
        
        if capital_actual >= objetivo:
            print(f"¡Meta alcanzada en el año {anios}!")
        else:
            print(f"Año {anios}: Saldo actual = ${capital_actual:.2f}")
            
    return anios

mi_capital = 1000
tasa = 7  

total_anios = calcular_tiempo_duplicacion(mi_capital, tasa)

print(f"\n--- RESULTADO FINAL ---")
print(f"Para duplicar ${mi_capital} al {tasa}% anual, necesitas {total_anios} años.")

# Ejercicio 25

def censurar_texto(texto, prohibidas):
    palabras_texto = texto.split()
    resultado = []
    
    for palabra in palabras_texto:
       
        palabra_limpia = palabra.strip(",.¡!¿?").lower()
        
        if palabra_limpia in prohibidas:
            resultado.append("**")
        else:
            resultado.append(palabra)
    
    texto_censurado = " ".join(resultado)
    return texto_censurado

frase = "verga, este código es un desastre y es una basura total."
lista_negra = ["verga", "basura", "desastre"]

final = censurar_texto(frase, lista_negra)

print(f"Original: {frase}")
print(f"Censurado: {final}")

# Ejercicio 26

def calificar_examenes(notas):
    reporte_letras = []
    
    print(f"{'Nota Numérica':<15} | {'Calificación'}")
    print("-" * 35)
    
    for nota in notas:
        
        if nota >= 90:
            letra = "A (Excelente)"
        elif nota >= 80:
            letra = "B (Muy Bueno)"
        elif nota >= 70:
            letra = "C (Satisfactorio)"
        elif nota >= 60:
            letra = "D (Suficiente)"
        else:
            letra = "F (Insuficiente)"
        
        reporte_letras.append(letra)
        print(f"{nota:>13}     | {letra}")
        
    return reporte_letras

examenes = [95, 82, 67, 45, 100, 78, 59]

resultado = calificar_examenes(examenes)

# Ejercicio 27

def analizar_mayusculas(parrafo):
   
    palabras = parrafo.split()
    palabras_mayusculas = []
    
    for palabra in palabras:
     
        palabra_limpia = palabra.strip("¿¡\"'(")
        
        if palabra_limpia and palabra_limpia[0].isupper():
            palabras_mayusculas.append(palabra_limpia)
        else:
           
            pass
            
    return palabras_mayusculas

texto_ejemplo = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, vivía Don Quijote."

resultado = analizar_mayusculas(texto_ejemplo)

print(f"Texto original: {texto_ejemplo}")
print(f"Palabras encontradas: {resultado}")
print(f"Total: {len(resultado)} palabras.")

# Ejercicio 28

def generar_piramide_impar(altura):
    print(f"--- Pirámide de Altura {altura} (Solo Filas Impares) ---\n")
    
    fila = 1
    
    while fila <= altura:
  
        if fila % 2 != 0:
           
            espacios = " " * (altura - fila)
            
            asteriscos = "*" * (2 * fila - 1)
            
            print(f"{espacios}{asteriscos}")
        else:
            
            pass
        
        fila += 1

try:
    medida = int(input("Introduce la altura de la pirámide: "))
    generar_piramide_impar(medida)
except ValueError:
    print("Por favor, introduce un número entero válido.")

# Ejercicio 29

def gestionar_reserva(lista_asientos, asiento_deseado):
    
    for i in range(len(lista_asientos)):
       
        if i == asiento_deseado:
            
            if lista_asientos[i] == 0:
                print(f"¡Éxito! El asiento {i} esta disponible.")
                return lista_asientos
            else:
                lista_asientos[i] == 1
                print(f"¡Error! El asiento {i} ha sido reservado.")
                return lista_asientos
    
    print("El número de asiento no existe.")
    return lista_asientos

asientos_cine = [0, 1, 0, 0, 1, 1] 
asientos_cine = gestionar_reserva(asientos_cine, 0)
asientos_cine = gestionar_reserva(asientos_cine, 1)
asientos_cine = gestionar_reserva(asientos_cine, 2)
asientos_cine = gestionar_reserva(asientos_cine, 3)
asientos_cine = gestionar_reserva(asientos_cine, 4)
asientos_cine = gestionar_reserva(asientos_cine, 5)

# Ejercicio 30

def calcular_promedio_ventas(lista_ventas):
    total_suma = 0
    dias_con_ventas = 0
    
    for venta in lista_ventas:
     
        if venta > 0:
            total_suma += venta
            dias_con_ventas += 1
        else:
            continue  
            
    if dias_con_ventas > 0:
        promedio = total_suma / dias_con_ventas
        return promedio
    else:
        return 0

ventas_quincena = [150, 0, 200, 0, 350, 100, 0, 500]
resultado = calcular_promedio_ventas(ventas_quincena)

print(f"El promedio de ventas (sin contar días en cero) es: {resultado}")

# Ejercicio 31

def contar_vocales(palabra):

    vocales = "aeiou"
    palabra = palabra.lower()
   
    for vocal in vocales:
        conteo = 0
        
        for letra in palabra:
            if letra == vocal:
                conteo += 1
        
        if conteo > 0:
            print(f"La vocal '{vocal}' aparece {conteo} veces.")
        else:
            
            pass

entrada = input("Introduce una palabra: ")
contar_vocales(entrada)

# Ejercicio 32

def sumar_digitos(numero):
    
    cadena_numero = str(numero)
    suma_total = 0
    
    print(f"Procesando el número: {numero}")

    for caracter in cadena_numero:
       
        if caracter.isdigit():
            digito = int(caracter)
            suma_total += digito
            print(f"Sumando: {digito} -> Total parcial: {suma_total}")
        else:
            print(f"Omitiendo carácter no numérico: '{caracter}'")
            
    return suma_total

resultado = sumar_digitos(987654321)
print(f"\n--- Resultado Final: {resultado} ---")

# Ejercicio 33

def encriptar_texto(mensaje):
    resultado = ""
   
    for caracter in mensaje:
       
        if caracter.isalpha():
            
            if caracter.lower() == 'z':
                nueva_letra = 'a' if caracter.islower() else 'A'
            else:
                nueva_letra = chr(ord(caracter) + 1)
            resultado += nueva_letra
        else:
            resultado += caracter
            
    return resultado

texto_original = "Hola vanessa.roldan."
texto_encriptado = encriptar_texto(texto_original)

print(f"Original:   {texto_original}")
print(f"Encriptado: {texto_encriptado}")

# Ejercicio 34

def mover_elevador(piso_actual, piso_destino):
    
    if -1 <= piso_destino <= 10:
        
        while piso_actual != piso_destino:
            if piso_actual < piso_destino:
                piso_actual += 1
                print(f"Subiendo... Piso {piso_actual}")
            else:
                piso_actual -= 1
                print(f"Bajando... Piso {piso_actual}")
        
        print(f"Has llegado al piso {piso_destino}.")
        return piso_actual 
    else:
        print("Error: El piso solicitado no existe en este edificio.")
        return piso_actual

piso_donde_estoy = 0 
continuar = True
print("--- Bienvenido al Elevador ---")

while continuar:
    destino = input("\n¿A qué piso deseas ir? (Escribe 'salir' para bajar del elevador): ")
    
    if destino.lower() == 'salir':
        continuar = False
        print("Saliendo del edificio. ¡Buen día!")
    else:
        piso_donde_estoy = mover_elevador(piso_donde_estoy, int(destino))

# Ejercicio 35

def validar_isbn(codigo):
    codigo_limpio = codigo.replace("-", "").replace(" ", "")
    
    if len(codigo_limpio) == 10:
        suma_control = 0
        peso = 10
        
        for caracter in codigo_limpio:
            if caracter.isdigit():
                
                suma_control += int(caracter) * peso
                peso -= 1 
            elif caracter.upper() == 'X' and peso == 1:
                
                suma_control += 10
            else:
                return "Error: Carácter no válido detectado."

        if suma_control % 11 == 0:
            return " El código ISBN es VÁLIDO."
        else:
            return " El código ISBN es INVÁLIDO."
    else:
        return "Error: El código debe tener 10 dígitos."

isbn_usuario = input("Introduce un ISBN-10 (ej. 0123456789): ")
resultado = validar_isbn(isbn_usuario)
print(resultado)

# Ejercicio 36

def gestionar_agenda():
  
    agenda = {}
    
    print("--- Bienvenido a tu Agenda de Contactos ---")
    
    while True:
        nombre = input("\nIntroduce el nombre del contacto (o escribe 'salir' para terminar): ").strip()
       
        if nombre.lower() == 'salir':
            print("Cerrando agenda...")
            break
        
        if nombre in agenda:
            print(f"¡Atención! El nombre '{nombre}' ya existe en tu agenda.")
            print(f"Su número actual es: {agenda[nombre]}")
        else:
           
            telefono = input(f"Introduce el teléfono para {nombre}: ")
            agenda[nombre] = telefono
            print("Contacto guardado con éxito.")

    print("\n--- Lista de Contactos Guardados ---")
    if not agenda:
        print("La agenda está vacía.")
    else:
        for contacto, tel in agenda.items():
            print(f"• {contacto}: {tel}")

gestionar_agenda()

# Ejercicio 37

def procesar_imc_pacientes(lista_pacientes):
    print(f"{'Paciente':<15} | {'IMC':<6} | {'Clasificación'}")
    print("-" * 40)

    for paciente in lista_pacientes:
        nombre = paciente[0]
        peso = paciente[1]
        altura = paciente[2]

       
        imc = peso / (altura ** 2)

        if imc < 18.5:
            estado = "Bajo peso"
        elif 18.5 <= imc < 25:
            estado = "Normal"
        elif 25 <= imc < 30:
            estado = "Sobrepeso"
        else:
            estado = "Obesidad"

        print(f"{nombre:<15} | {imc:<6.2f} | {estado}")

pacientes_hoy = [
    ["Ana García", 55, 1.65],
    ["Luis Pérez", 85, 1.75],
    ["Marta Ruiz", 110, 1.70],
    ["Juan Solo", 45, 1.60]
]

procesar_imc_pacientes(pacientes_hoy)

# Ejercicio 38

def calcular_total_carrito(carrito):
    total_neto = 0
    total_con_iva = 0
    
    print(f"{'Producto':<12} | {'Categoría':<10} | {'P. Final'}")
    print("-" * 40)

    for producto, datos in carrito.items():
        precio = datos["precio"]
        categoria = datos["categoria"]
       
        if categoria == "Alimento":
            precio_final = precio
            impuesto = 0
        elif categoria == "Lujo":
            precio_final = precio * 1.21
            impuesto = 21
        else:
            
            precio_final = precio
            impuesto = 0
       
        total_neto += precio
        total_con_iva += precio_final
        
        print(f"{producto:<12} | {categoria:<10} | ${precio_final:>8.2f} (+{impuesto}%)")

    print("-" * 40)
    print(f"Total a pagar: ${total_con_iva:.2f}")

mi_carrito = {
    "Manzanas": {"precio": 5.0, "categoria": "Alimento"},
    "Reloj Oro": {"precio": 1000.0, "categoria": "Lujo"},
    "Pan": {"precio": 1.5, "categoria": "Alimento"},
    "Perfume": {"precio": 80.0, "categoria": "Lujo"}
}

calcular_total_carrito(mi_carrito)

# Ejercicio 39

def analizar_actividad_fisica(pasos_semana):
    total_pasos = 0
    dias_activos = 0
    
    print("--- Reporte de Actividad Semanal ---")
    
    for i, pasos in enumerate(pasos_semana, start=1):
        total_pasos += pasos 
        
        if pasos < 5000:
            estado = "Sedentario"
        else:
            estado = "Activo"
            dias_activos += 1
            
        print(f"Día {i}: {pasos} pasos - {estado}")

    promedio = total_pasos / len(pasos_semana)
    
    print("-" * 35)
    print(f"Promedio de pasos: {promedio:.0f}")
    
    if promedio >= 7000:
        print("¡Excelente ritmo! Mantienes un estilo de vida muy saludable.")
    else:
        print("Intenta caminar un poco más para llegar a la meta recomendada.")

mis_pasos = [4200, 8500, 3100, 5200, 11000, 4800, 9000]

analizar_actividad_fisica(mis_pasos)

# Ejercicio 40

def ordenar_burbuja_manual(lista):
    n = len(lista)
    
    for i in range(n):
        
        for j in range(0, n - i - 1):
            
            if lista[j] > lista[j + 1]:
                
                temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temporal
                
    return lista
numeros = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:", numeros)

lista_ordenada = ordenar_burbuja_manual(numeros)

print("Lista ordenada:", lista_ordenada)

