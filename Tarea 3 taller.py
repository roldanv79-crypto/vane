# Ejercicio 1
from abc import ABC, abstractmethod
import re

class Empleado(ABC):
    def __init__(self, nombre, codigo, salario_base):
        if not self.validar_codigo_empleado(codigo):
            raise ValueError(f"Código {codigo} inválido. Debe ser EMP-XXXX")
        
        self.nombre = nombre
        self.codigo = codigo
        self._salario_base = salario_base

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0:
            print(" Error: El salario no puede ser negativo.")
        else:
            self._salario_base = valor

    @staticmethod
    def validar_codigo_empleado(codigo):
        # Valida el formato EMP-seguido de 4 números
        patron = r"^EMP-\d{4}$"
        return bool(re.match(patron, codigo))

    @abstractmethod
    def calcular_salario_neto(self):
        pass

class Gerente(Empleado):
    def calcular_salario_neto(self):
        # El gerente recibe un bono del 20%
        return self.salario_base * 1.20

class Desarrollador(Empleado):
    def calcular_salario_neto(self):
        # Al desarrollador se le retiene un 10% por impuestos/seguro
        return self.salario_base * 0.90

# --- Pruebas del Ejercicio 1 ---
try:
    g1 = Gerente("Vanessa Roldan", "EMP-1010", 3120)
    d1 = Desarrollador("Alejandro Marin", "EMP-2020", 2300)

    print(f" {g1.nombre} ({g1.codigo}): ${g1.calcular_salario_neto()}")
    print(f" {d1.nombre} ({d1.codigo}): ${d1.calcular_salario_neto()}")
    
    # Intento de salario negativo
    d1.salario_base = -500 
except ValueError as e:
    print(f"Error de validación: {e}")

# Ejercicio 2

from abc import ABC, abstractmethod

def verificar_conexion(func):
    def envoltura(self, *args, **kwargs):
        if not self.conectado:
            return f" Acción cancelada: El dispositivo '{self.nombre}' está offline."
        return func(self, *args, **kwargs)
    return envoltura

class DispositivoInteligente(ABC):
    _total_dispositivos = 0  

    def __init__(self, nombre):
        self.nombre = nombre
        self.conectado = True 
        DispositivoInteligente._incrementar_contador()

    @classmethod
    def _incrementar_contador(cls):
        cls._total_dispositivos += 1

    @classmethod
    def obtener_conteo(cls):
        return f" Dispositivos totales en la casa: {cls._total_dispositivos}"

    @abstractmethod
    def activar_funcion_principal(self):
        pass

class Termostato(DispositivoInteligente):
    def __init__(self, nombre, temp_inicial=20):
        super().__init__(nombre)
        self._temperatura_objetivo = temp_inicial

    @property
    def temperatura_objetivo(self):
        return self._temperatura_objetivo

    @temperatura_objetivo.setter
    def temperatura_objetivo(self, valor):
        if 10 <= valor <= 30:
            self._temperatura_objetivo = valor
        else:
            print(" Valor fuera de rango (10°C - 30°C)")

    @verificar_conexion
    def activar_funcion_principal(self):
        return f" Ajustando clima a {self._temperatura_objetivo}°C en {self.nombre}."

class CamaraSeguridad(DispositivoInteligente):
    @verificar_conexion
    def activar_funcion_principal(self):
        return f" Grabando video de seguridad en {self.nombre}..."

# Pruebas 
t1 = Termostato("Sala Principal", 22)
c1 = CamaraSeguridad("Cámara de Entrada")

print(DispositivoInteligente.obtener_conteo())
print(t1.activar_funcion_principal())

# Probar restricción de conexión
c1.conectado = False
print(c1.activar_funcion_principal())

# Validar temperatura
t1.temperatura_objetivo = 45