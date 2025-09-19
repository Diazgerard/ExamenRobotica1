# Sistema de Detección de Proximidad con LEDs

Un sistema de detección de proximidad basado en Raspberry Pi que utiliza un sensor ultrasónico HC-SR04 para medir distancias y controlar LEDs según la proximidad de objetos.

## 📋 Descripción

Este proyecto implementa un sistema de alerta visual que indica la proximidad de objetos mediante diferentes colores de LED:

- **LED Verde**: Objeto lejos (> 40 cm) - Encendido fijo
- **LED Rojo**: Objeto cerca (20-40 cm) - Parpadeo intermitente  
- **LED Azul**: Objeto muy cerca (≤ 20 cm) - Encendido fijo

## 🔧 Componentes Necesarios

### Hardware
- Raspberry Pi (cualquier modelo con GPIO)
- Sensor ultrasónico HC-SR04
- 3 LEDs (verde, rojo, azul)
- 3 resistencias de 220Ω (para los LEDs)
- Cables jumper macho-hembra
- Protoboard o PCB de pruebas

### Software
- Raspberry Pi OS
- Python 3
- Librería RPi.GPIO

## 📐 Diagrama de Conexiones

### Pines GPIO utilizados:

| Componente | Pin GPIO | Pin Físico |
|------------|----------|------------|
| LED Verde  | GPIO 18  | Pin 12     |
| LED Rojo   | GPIO 23  | Pin 16     |
| LED Azul   | GPIO 24  | Pin 18     |
| TRIG (HC-SR04) | GPIO 20 | Pin 38 |
| ECHO (HC-SR04) | GPIO 21 | Pin 40 |

### Conexiones del Sensor HC-SR04:
- **VCC** → 5V (Pin 2)
- **GND** → GND (Pin 6)
- **TRIG** → GPIO 20 (Pin 38)
- **ECHO** → GPIO 21 (Pin 40)

### Conexiones de los LEDs:
Cada LED debe conectarse con una resistencia de 220Ω en serie:
- **LED Verde**: GPIO 18 → Resistencia → LED → GND
- **LED Rojo**: GPIO 23 → Resistencia → LED → GND  
- **LED Azul**: GPIO 24 → Resistencia → LED → GND

## 🚀 Instalación y Uso

### 1. Preparar el entorno
```bash
# Actualizar el sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y pip (si no están instalados)
sudo apt install python3 python3-pip -y

# Instalar la librería GPIO
pip3 install RPi.GPIO
```

### 2. Clonar o descargar el proyecto
```bash
# Crear directorio del proyecto
mkdir sistema_proximidad
cd sistema_proximidad

# Copiar el archivo examen1.py al directorio
```

### 3. Ejecutar el programa
```bash
# Ejecutar con permisos de administrador (necesario para GPIO)
sudo python3 examen1.py
```

### 4. Detener el programa
Presiona `Ctrl + C` para detener el programa de forma segura.

## 📊 Funcionamiento

### Lógica de Operación

1. **Medición continua**: El sensor ultrasónico mide la distancia cada 100ms
2. **Procesamiento**: El programa evalúa la distancia y determina el estado del LED
3. **Control visual**: Se enciende el LED correspondiente según la proximidad

### Rangos de Distancia

```
Distancia > 40 cm    →  🟢 LED Verde (fijo)
20 cm < Distancia ≤ 40 cm  →  🔴 LED Rojo (parpadeo)
Distancia ≤ 20 cm    →  🔵 LED Azul (fijo)
```

### Algoritmo de Medición

El sensor utiliza ondas ultrasónicas para calcular la distancia:

1. Envía un pulso de 10μs por el pin TRIG
2. Mide el tiempo de retorno del eco en el pin ECHO
3. Calcula la distancia usando: `distancia = (tiempo × velocidad_sonido) / 2`
4. Velocidad del sonido ≈ 343 m/s (factor 17150 en el código)

## 📁 Estructura del Proyecto

```
sistema_proximidad/
├── examen1.py          # Código principal del sistema
├── README.md           # Este archivo de documentación
└── docs/              # (Opcional) Documentación adicional
    ├── esquemas/      # Diagramas de conexión
    └── imagenes/      # Fotos del montaje
```

## 🔍 Detalles del Código

### Funciones Principales

- **`medir_distancia()`**: Controla el sensor HC-SR04 y retorna la distancia en cm
- **Bucle principal**: Evalúa continuamente la distancia y controla los LEDs

### Configuración de GPIO

```python
GPIO.setmode(GPIO.BCM)      # Usa numeración BCM
GPIO.setwarnings(False)     # Desactiva advertencias
```

### Limpieza de Recursos

El programa incluye manejo de excepciones para limpiar los pines GPIO al finalizar:
```python
except KeyboardInterrupt:
    GPIO.cleanup()
```

## ⚠️ Consideraciones Importantes

### Seguridad
- Siempre ejecutar con `sudo` para acceso a GPIO
- Verificar conexiones antes de alimentar el circuito
- Usar resistencias apropiadas para proteger los LEDs

### Limitaciones
- Rango efectivo del HC-SR04: 2cm - 400cm
- Precisión: ±3mm
- Ángulo de detección: ~15°

### Troubleshooting

**Problema**: LEDs no encienden
- Verificar conexiones y polaridad de LEDs
- Confirmar que las resistencias están en serie
- Comprobar permisos de ejecución (`sudo`)

**Problema**: Lecturas erráticas del sensor
- Verificar conexiones del sensor
- Asegurar alimentación estable de 5V
- Evitar obstáculos que generen múltiples ecos

## 🔄 Posibles Mejoras

- [ ] Agregar buzzer para alertas sonoras
- [ ] Implementar interfaz web para monitoreo remoto
- [ ] Añadir registro de datos (logging)
- [ ] Calibración automática del sensor
- [ ] Soporte para múltiples sensores
- [ ] Integración con IoT (MQTT, API REST)

## 📝 Licencia

Este proyecto está disponible bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📞 Contacto

Para dudas o sugerencias sobre este proyecto de robótica, puedes contactar al desarrollador.

---

**Proyecto desarrollado para el curso de Robótica - 17º Trimestre**