import RPi.GPIO as GPIO
import time

# ----------------------------
# CONFIGURACIÓN DE PINES
# ----------------------------
LED_VERDE = 18
LED_ROJO = 23
LED_AZUL = 24

TRIG = 20
ECHO = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(LED_ROJO, GPIO.OUT)
GPIO.setup(LED_AZUL, GPIO.OUT)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# ----------------------------
# FUNCIONES
# ----------------------------
def medir_distancia():
    """Devuelve la distancia medida en cm"""
    GPIO.output(TRIG, False)
    time.sleep(0.05)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    duracion = pulse_end - pulse_start
    distancia = duracion * 17150
    return round(distancia, 2)

# ----------------------------
# PROGRAMA PRINCIPAL
# ----------------------------
try:
    while True:
        dist = medir_distancia()
        print("Distancia:", dist, "cm")

        if dist > 40:  
            # Lejos → LED verde encendido
            GPIO.output(LED_VERDE, 1)
            GPIO.output(LED_ROJO, 0)
            GPIO.output(LED_AZUL, 0)

        elif 20 < dist <= 40:  
            # Cerca → LED rojo parpadea
            GPIO.output(LED_VERDE, 0)
            GPIO.output(LED_AZUL, 0)
            GPIO.output(LED_ROJO, 1)
            time.sleep(0.2)
            GPIO.output(LED_ROJO, 0)
            time.sleep(0.2)

        elif dist <= 20:  
            # Muy cerca → LED azul fijo
            GPIO.output(LED_VERDE, 0)
            GPIO.output(LED_ROJO, 0)
            GPIO.output(LED_AZUL, 1)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programa terminado")
    GPIO.cleanup()