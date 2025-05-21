# 🏗️ Clase 7: Módulos, Entornos Virtuales, Errores y Archivos

Esta clase es fundamental para construir aplicaciones Python más grandes, robustas y organizadas. Cubrimos cómo estructurar el código, gestionar dependencias, manejar errores y persistir datos.

## ✅ Temas Cubiertos

- **Módulos**:
  - Concepto: Archivos `.py` para organizar y reutilizar código.
  - Importación: `import modulo`, `from modulo import funcion`, `as alias`.
  - Librería Estándar: Ejemplos con `math`, `random`, `datetime`.
  - El bloque `if __name__ == "__main__":` para código de prueba dentro de módulos.
- **Paquetes (Introducción)**:
  - Concepto: Directorios con un archivo `__init__.py` que agrupan módulos.
  - Estructura básica y cómo importar desde paquetes.
- **Entornos Virtuales (`venv`)**:
  - Propósito: Aislar dependencias de proyectos para evitar conflictos.
  - Creación: `python -m venv nombre_entorno` (comúnmente `.venv` o `env`).
  - Activación/Desactivación: `source nombre_entorno/bin/activate` (Linux/Mac) o `nombre_entorno\Scripts\activate` (Windows). `deactivate`.
  - Gestión de Paquetes: `pip install paquete`, `pip freeze > requirements.txt`, `pip install -r requirements.txt`.
- **Manejo de Errores (Excepciones)**:
  - Bloque `try-except`: Para capturar y manejar errores en tiempo de ejecución.
  - `except TipoDeErrorEspecifico:`, `except Exception as e:`.
  - Bloque `else`: Código a ejecutar si no hubo excepciones en el `try`.
  - Bloque `finally`: Código que se ejecuta siempre (limpieza).
  - Tipos comunes: `ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`, `IndexError`.
- **Manejo de Archivos de Texto**:
  - Abrir archivos: `open(ruta, modo)`. Modos: `'r'` (leer), `'w'` (escribir - sobrescribe), `'a'` (añadir).
  - **Context Manager `with open(...) as f:` (Recomendado)**: Cierra el archivo automáticamente.
  - Escribir: `f.write("texto\n")`.
  - Leer: `f.read()` (todo), `f.readline()` (una línea), `f.readlines()` (lista de líneas), iterar `for linea in f:`.
  - Uso de `.strip()` para limpiar saltos de línea.

## 💻 Archivos de Código

- [`mis_operaciones.py`](./mis_operaciones.py): Módulo de ejemplo creado en clase con funciones de cálculo simples y el bloque `if __name__ == "__main__":`.
- [`clase7_modulos_ejemplos.py`](./clase7_modulos_ejemplos.py): Script que importa y utiliza `mis_operaciones.py` y módulos de la librería estándar (`math`, `random`, `datetime`).
- [`clase7_errores.py`](./clase7_errores.py): Demostraciones de manejo de excepciones con `try-except-else-finally`.
- [`clase7_archivos.py`](./clase7_archivos.py): Ejemplos de escritura y lectura de archivos de texto usando `with open()`.
- [`clase7_practica.py`](./clase7_practica.py): Soluciones a los ejercicios prácticos realizados en clase (uso de un módulo propio, división segura con `try-except`, y lista de tareas en archivo).

## 🎯 Tareas / Ejercicios Propuestos

1.  **Gestor de Notas Simple con Módulos y Persistencia Mejorada:**
    - Refactoriza el ejercicio del "Directorio Telefónico" o "Lista de Compras" de clases anteriores.
    - Separa la lógica de "negocio" (añadir, eliminar, buscar, listar) en funciones dentro de un **módulo** (ej. `mi_gestor_logica.py`).
    - El script principal importará y usará estas funciones para el menú interactivo.
    - Guarda los datos en un archivo. Considera usar el módulo **`json`** para guardar y cargar la lista de contactos/ítems (una lista de diccionarios) de forma más estructurada que texto plano.
    - Implementa un **manejo de errores** robusto para todas las operaciones de archivo y entradas del usuario.
2.  **Explorador Básico de Directorios con `os`:**
    - Crea un script que pida al usuario la ruta a un directorio.
    - Usa el módulo `os` (`os.listdir()`, `os.path.join()`, `os.path.isfile()`, `os.path.isdir()`) para listar el contenido de ese directorio, indicando si cada elemento es un archivo o un subdirectorio.
    - Maneja `FileNotFoundError` si la ruta no existe.
3.  **Analizador de Archivo de Texto:**
    - Crea una función que reciba la ruta a un archivo de texto.
    - La función debe leer el archivo y retornar un diccionario con estadísticas: número de líneas, número de palabras (aproximado, usando `split()`), y número de caracteres.
    - Maneja `FileNotFoundError` y otros `IOError` posibles.

---

_Puedes encontrar posibles soluciones a estos ejercicios propuestos en la carpeta `Soluciones/Clase_07/`._
