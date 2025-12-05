# 🎮 Adivina el Número - Python Game

Bienvenido a Adivina el Número, un juego interactivo de consola desarrollado en Python. Este proyecto combina lógica de programación, gestión de archivos externos (Excel), interfaz colorida y efectos de sonido para crear una experiencia de usuario completa.

## 🚀 Características Principales

🤖 **Modo Solitario** : Desafía a la CPU intentando adivinar un número aleatorio entre 1 y 1000.

⚔️ **Modo Multijugador (PvP)**: Un jugador establece el número secreto y el otro intenta adivinarlo con pistas ocultas.

📊 **Persistencia de Datos**: ¡Tus estadísticas no se pierden! El juego genera y actualiza automáticamente con el historial de todas las partidas.

🎨 **Interfaz Mejorada**: Uso de la librería colorama para feedback visual (Verde para victorias, Rojo para errores, Amarillo para pistas).

🎵 **Atmósfera**: Música de fondo (BGM)implementada con pygame para una experiencia inmersiva.

🎚️ **Niveles de Dificultad**: Sistema ajustable (Fácil, Medio, Difícil) que altera el número de intentos disponibles.

## 📋 Requisitos del Sistema

Para ejecutar este juego sin problemas, necesitas:

Python: Versión 3.10, 3.11, 3.12 o 3.13.

Nota: Se recomienda no usar versiones Alpha como Python 3.14 debido a incompatibilidades con pygame.

Sistema Operativo: Windows, macOS o Linux.

## 🛠️ Instalación y Ejecución

Sigue estos pasos para probar el juego en tu ordenador:

1. **Clonar el repositorio**:

   ```bash
   git clone [https://github.com/nachofort/SQL-Python-Practice.git](https://github.com/nachofort/SQL-Python-Practice.git)
   cd SQL-Python-Practice/Python/Game


2. **Instalar las dependencias**:
El juego utiliza librerías externas. Instálalas ejecutando:

```bash
pip install -r requirements.txt
```

(Si no tienes el archivo requirements.txt, ejecuta: ```pip install openpyxl colorama pygame```)

Ejecutar el juego:

```text
python juego.py
```


## 📂 Estructura del Proyecto

El código está modularizado para seguir buenas prácticas. Nota que el archivo Excel no aparece aquí porque se genera automáticamente en tu ordenador la primera vez que juegas (y está excluido por el `.gitignore`):

```text
📁 TU_PROYECTO/
├── 📄 juego.py              # Archivo principal (Main Loop)
├── 📄 funciones.py          # Lógica del juego, menús y validaciones
├── 🎵 musica1.mp3           # Archivo de audio para la música de fondo
├── 📄 requirements.txt      # Lista de librerías necesarias
├── 📄 .gitignore            # Configuración para ignorar archivos temporales y Excel
└── 📄 README.md             # Documentación del proyecto
```

## 🕹️ Controles

* Usa el teclado numérico para seleccionar opciones del menú.
* Introduce tus intentos numéricos y pulsa `ENTER`.
* Sigue las pistas en pantalla:
  * 🔼 **Mayor:** El número secreto es más alto.
  * 🔽 **Menor:** El número secreto es más bajo.

## 👨‍💻 Autor

Desarrollado por **Ignacio Fort** como proyecto de Python.
