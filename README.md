Aquí tienes el Markdown para tu repositorio de GitHub, con la explicación sobre la detección de figuras geométricas y las instrucciones para instalar y ejecutar el código.

```markdown
# Detección de Figuras Geométricas con MediaPipe

Este proyecto utiliza **MediaPipe** para detectar figuras geométricas básicas (Círculo, Triángulo y Cuadrado) usando los puntos clave de las manos. A través de la cámara, se procesan los movimientos de la mano y se identifican las figuras geométricas según las distancias y ángulos entre ciertos puntos de la mano.

## Figuras Detectadas

1. **Círculo**: Se detecta cuando los puntos del pulgar y el índice forman un ángulo menor a 53 grados.
2. **Triángulo**: Se detecta cuando el ángulo entre los puntos es mayor a 53 grados pero menor a 68 grados.
3. **Rectángulo**: Se detecta cuando el ángulo es mayor a 68 grados.

## Requisitos

1. Python 3.7 o superior.
2. Dependencias:
    - `mediapipe`
    - `opencv-python`
    - `numpy`

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/detecion-figuras-geometricas.git
   cd detecion-figuras-geometricas
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

   Si no tienes el archivo `requirements.txt`, instala las dependencias manualmente:
   ```bash
   pip install mediapipe opencv-python numpy
   ```

## Ejecución

1. Ejecuta el script con:
   ```bash
   python deteccion_figuras.py
   ```

   Esto abrirá una ventana con la transmisión de video en tiempo real de tu cámara y la detección de figuras geométricas según los movimientos de tus manos.

2. Para salir de la ejecución, presiona la tecla **Esc**.

## Explicación del Código

Este programa usa **MediaPipe** para detectar las manos y sus puntos clave. Los puntos más relevantes en este caso son:
- **Pulgar**: `THUMB_MCP` y `THUMB_TIP`
- **Índice**: `INDEX_FINGER_TIP`

Se calcula la distancia entre estos puntos y el ángulo formado para determinar qué figura geométrica se está formando.

### Cálculos Matemáticos

- **Distancia**: Se calcula usando el teorema de Pitágoras entre los puntos clave.
- **Ángulo**: Se calcula usando la ley de los cosenos entre los tres puntos clave. Dependiendo del ángulo, se detectan las diferentes figuras geométricas.

### Figuras:
- **Círculo**: Si el ángulo es menor a 53 grados, se dibuja un círculo entre el índice y el pulgar.
- **Triángulo**: Si el ángulo está entre 53 y 68 grados, se dibuja un triángulo.
- **Rectángulo**: Si el ángulo es mayor a 68 grados, se dibuja un rectángulo.

## Captura de Imágenes

Si deseas ver cómo se ven las imágenes generadas, puedes acceder a los siguientes enlaces:

- ![Ejemplo Círculo](url_de_imagen_del_círculo)
- ![Ejemplo Triángulo](url_de_imagen_del_triángulo)
- ![Ejemplo Rectángulo](url_de_imagen_del_rectángulo)

## Contribuciones

Si deseas mejorar este proyecto, ¡estaré encantado de recibir tus contribuciones! Si encuentras errores o mejoras, abre un **Issue** o envía un **Pull Request**.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
```

### Explicación breve de la detección de figuras geométricas:
La **detección de figuras geométricas** se basa
