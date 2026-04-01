import os
import abc 
from datetime import datetime
import matplotlib.pyplot as plt
from docxtpl import DocxTemplate
from gtts import gTTS

class MetaRiesgoOrbital(abc.ABCMeta):
    def __new__(cls, name, bases, dct):
        if name not in ("Satelite", "ABC") and "decodificar_trama" not in dct:
            raise TypeError(f"Error: {name} debe implementar 'decodificar_trama()'")
        return super().__new__(cls,name,bases,dct)

class Satelite(abc.ABC, metaclass=MetaRiesgoOrbital):
    def __init__(self, nombre, altitud_km):
        self.nombre = nombre
        self.altitud = altitud_km
        self.__claves_encriptacion = "SECRET_HEX_2026"
        self.historial_orbita = []

    @abc.abstractmethod
    def decodificar_trama(self, hexadecimal):
        pass

def verificar_ventana_comunicacion(func):
    def wrapper(self, *args, **kwargs):
        if datetime.now().second % 2 == 0:
            print(f" [ENLACE ESTABLE] conectado con {self.nombre}")
            return func(self, *args, **kwargs)
        else:
            print(f"[SIN SEÑAL] Satélite fuera de rango. Reintente en un segundo")
            return None
    return wrapper
    
class SateliteComunicaciones(Satelite):
    def decodificar_trama(self, hexadecimal):
        val = int(hexadecimal, 16)
        return {"telemetria": (val/10, "km")}
    
    @verificar_ventana_comunicacion
    def simular_mision(self, ciclos):
        print(f"Iniciando monitoreo de órbita para {self.nombre}")
        i = 0
        while i < ciclos:
            caida = 1.1 * (i * 0.3)
            self.altitud -= caida
            self.historial_orbita.append(self.altitud)

            if self.altitud < 350:
                print (f"ALERTA: Altitud Crítica ({round(self.altitud, 2)} km)")
                if self.altitud < 310:
                    print("ACTIVANDO PROPULSORES DE EMERGENCIA")
                    self.altitud += 55

            i += 1
        return self.historial_orbita
    
def ejecutar_pipeline_mision (sat):
    fecha_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    ruta= f"Auditoria_{sat.nombre}_{fecha_str}"
    if not os.path.exists(ruta):
        os.makedirs(ruta)

    try:
        doc = DocxTemplate("plantilla_mision.docx")
        contexto = {

            'fecha': datetime.now().strftime("%d/%m/%Y  %H:%M"),
            'nombre_sat': sat.nombre,
            'altitud_final': round(sat.altitud, 2),
            'estado': "ESTABLE" if sat.altitud > 310 else "REINGRESO INMINENTE",
            'mensaje_alerta': "MANIOBRA EXITOSA" if sat.altitud > 350 else "CORRECION URGENTE REALIZADA"        
        }
        doc.render(contexto)
        word_path = os.path.join(ruta, "Bitacora_Final.docx")
        doc.save(word_path)
        print (f"Documento Word generado en: {word_path}")
    except Exception as e:
        print(f"Error al crear el word: {e}. Está el archivo 'plantilla_mision.docx' cerrado?")

    plt.figure(figsize=(8,4))
    plt.plot(sat.historial_orbita, color='blue', linewidth=2, label="Trayectoria LEO")
    plt.axhline(y=310, color='red', linestyle='--', label="Límite Crítico")
    plt.title(f"Análisis de Decaimiento Orbital: {sat.nombre}")
    plt.xlabel("Tiempo (Pasos)")
    plt.ylabel("Altitud (km)")
    plt.grid(True)
    plt.legend()
    graph_path= os.path.join(ruta, "decaimiento.png")
    plt.savefig(graph_path)
    plt.close()
    print(f"Gráfico guardado en: {graph_path}")

    alerta_txt = f"Atención control de misión, el satélite {sat.nombre} ha reportado decaimiento orbital"
    tts = gTTS(text=alerta_txt, lang='es')
    audio_path= os.path.join(ruta, "alerta_voz.mp3")
    tts.save(audio_path)
    print(f"Audio generado en: {audio_path}")

if __name__=="__main__":
    try:
        mi_satelite = SateliteComunicaciones("Alfa-LEO", 530.0)
        tramas_hex = ["0FA2", "11B4", "0E2F"]
        for t in tramas_hex:
            datos = mi_satelite.decodificar_trama(t)
            print(f"Trama {t} decodificada: {datos['telemetria'][0]} {datos['telemetria'][1]}") 

        resultado = mi_satelite.simular_mision(30)
        if resultado:
            ejecutar_pipeline_mision(mi_satelite)
            print("\n PROCESO COMPLETADO EXITOSAMENTE.")
        else:
            print("\n REINTENTE LA EJECUCION PARA CAPTURAR LA VENTANA DE COMUNICACION.")

    except Exception as e:
        print(f" Error ineperado en el sistema: {e}")


    


