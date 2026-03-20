class Dispositivo:
    # 1. Atributo de clase
    cantidad_total_registrada = 0

    def __init__(self, marca, modelo):
        # 2. Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        # Aumentar contador global
        Dispositivo.cantidad_total_registrada += 1

    # 3. Método para invertir el estado
    def cambiar_estado(self):
        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True

class Telefono(Dispositivo):
    def __init__(self, marca, modelo):
        # 4. Herencia y atributo de lista
        super().__init__(marca, modelo)
        self.aplicaciones = []

    # 5. Método para instalar apps
    def instalar_app(self, nombre_app):
        self.aplicaciones.append(nombre_app)
        print(f"Instalada: {nombre_app} en {self.marca} {self.modelo}")

# 6. Función externa con bucle y condicional
def mostrar_telefonos_encendidos(lista_telefonos):
    print("\n--- Teléfonos Encendidos ---")
    for tel in lista_telefonos:
        if tel.encendido:
            print(f"📱 {tel.marca} {tel.modelo}")

# --- Pruebas del sistema ---

# Creación de instancias
t1 = Telefono("Xiaomi", "Redmi 9a")
t2 = Telefono("Samsung", "Galaxy S24")
t3 = Telefono("Motorola", "Moto G")

# Modificación de estados
t1.cambiar_estado() # Encendido
t3.cambiar_estado() # Encendido

# Instalación de apps
t1.instalar_app("Instagram")
t2.instalar_app("Facebook")

# Ejecución de la función externa
mis_telefonos = [t1, t2, t3]
mostrar_telefonos_encendidos(mis_telefonos)

print(f"\nTotal de dispositivos registrados: {Dispositivo.cantidad_total_registrada}")

class Jugador:
    # 1. Atributo de clase
    puntuacion_base = 100

    def __init__(self, nombre_usuario):
        # 2. Atributos de instancia
        self.nombre_usuario = nombre_usuario
        self.puntos_actuales = Jugador.puntuacion_base

    # 3. Método para sumar puntos
    def ganar_puntos(self, cantidad):
        self.puntos_actuales += cantidad
        print(f" {self.nombre_usuario} ganó {cantidad} puntos. Total: {self.puntos_actuales}")


# 4. Clase JugadorVIP que hereda de Jugador
class JugadorVIP(Jugador):
    def __init__(self, nombre_usuario, multiplicador):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre_usuario)
        self.multiplicador = multiplicador

    # 5. Método específico para VIP con multiplicador
    def ganar_puntos_vip(self, cantidad):
        puntos_extra = cantidad * self.multiplicador
        self.puntos_actuales += puntos_extra
        print(f"VIP {self.nombre_usuario} ganó {puntos_extra} puntos (x{self.multiplicador}). Total: {self.puntos_actuales}")


# 6. Función externa para filtrar jugadores
def filtrar_mejores_jugadores(lista_jugadores, puntaje_minimo):
    mejores = []
    for jugador in lista_jugadores:
        if jugador.puntos_actuales >= puntaje_minimo:
            mejores.append(jugador.nombre_usuario)
    return mejores

# --- Ejemplo de uso ---
player1 = Jugador("Jose")
player2 = JugadorVIP("Vanessa", 2)

player1.ganar_puntos(50)         # Total: 150
player2.ganar_puntos_vip(40)     # Total: 180 (100 base + 40*2)

ranking = filtrar_mejores_jugadores([player1, player2], 160)
print(f"\nJugadores destacados (min 160 pts): {ranking}")

class Vehiculo:
    # 1. Atributo de clase (común para toda la flota)
    costo_por_litro = 1.50

    def __init__(self, matricula, combustible_litros):
        # 2. Atributos de instancia
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.en_ruta = True

    # 3. Lógica de consumo: 1L cada 10km
    def viajar(self, kilometros):
        if not self.en_ruta:
            print(f"El vehículo {self.matricula} no puede viajar, está fuera de ruta.")
            return

        consumo_necesario = kilometros / 10
        
        if self.combustible_litros >= consumo_necesario:
            self.combustible_litros -= consumo_necesario
            print(f" {self.matricula} recorrió {kilometros}km. Quedan {self.combustible_litros:.1f}L.")
        else:
            self.combustible_litros = 0
            self.en_ruta = False
            print(f" {self.matricula} se quedó sin gasolina a mitad del trayecto.")

# 4. Herencia y atributo específico para Camion
class Camion(Vehiculo):
    def __init__(self, matricula, combustible_litros, cargas_entregadas):
        super().__init__(matricula, combustible_litros)
        self.cargas_entregadas = cargas_entregadas # Lista de strings

    # 5. Método para procesar la cola de entregas
    def entregar_carga(self):
        if self.cargas_entregadas:
            carga_eliminada = self.cargas_entregadas.pop()
            print(f"Carga '{carga_eliminada}' entregada por el camión {self.matricula}.")
        else:
            print(f"El camión {self.matricula} no tiene más cargas pendientes.")

# 6. Función de simulación con verificación de tipo (isinstance)
def simular_jornada(lista_vehiculos, distancias_a_recorrer):
    print("--- INICIO DE LA JORNADA ---")
    for i in range(len(lista_vehiculos)):
        vehiculo = lista_vehiculos[i]
        distancia = distancias_a_recorrer[i]
        
        # El vehículo viaja
        vehiculo.viajar(distancia)
        
        # Si es camión y sigue operativo, entrega carga
        if isinstance(vehiculo, Camion) and vehiculo.en_ruta:
            vehiculo.entregar_carga()
    print("--- FIN DE LA JORNADA ---\n")

# --- Prueba del simulador ---
v1 = Vehiculo("ABC-123", 5) # Solo tiene para 50km
c1 = Camion("TRK-999", 50, ["Alimentos", "Electrónicos", "Muebles"])

flota = [v1, c1]
rutas = [60, 100] # El v1 debería fallar, el c1 debería entregar una carga

simular_jornada(flota, rutas)
