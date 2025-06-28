# Guía de Solución: Versionar un Proyecto Anterior en GitHub

Esta es una guía de los pasos y comandos que necesitarías para completar la Tarea 1 de la Clase 8. Asumiremos que quieres versionar un proyecto que está en una carpeta llamada `mi_proyecto_anterior`.

### Paso 1: Preparar el Repositorio Local

1.  **Navega a la carpeta de tu proyecto** usando la terminal.

    ```bash
    cd ruta/hacia/mi_proyecto_anterior
    ```

2.  **Inicializa el repositorio Git.** Esto crea la carpeta oculta `.git` y empieza a rastrear la carpeta actual.

    ```bash
    git init
    ```

3.  **Revisa el estado.** Verás que todos tus archivos aparecen como "Untracked files".

    ```bash
    git status
    ```

4.  **Añade todos los archivos al Staging Area.** El `.` es un comodín para "todo en esta carpeta".

    ```bash
    git add .
    ```

5.  **Realiza tu primer commit.** Este será el punto de partida de tu historial.
    ```bash
    git commit -m "Commit inicial: Añadir archivos del proyecto"
    ```

### Paso 2: Crear y Conectar el Repositorio Remoto

1.  **Ve a GitHub.com** e inicia sesión.
2.  **Crea un nuevo repositorio.**

    - Haz clic en el botón "New".
    - Dale un nombre (ej. `mi_proyecto_anterior`).
    - Asegúrate de que esté **vacío** (NO marques las casillas para añadir un README, .gitignore o licencia, ya que tu proyecto ya los podría tener, y si no, los puedes añadir localmente).
    - Copia la URL del repositorio que te proporciona GitHub (la que termina en `.git`).

3.  **Conecta tu repositorio local al remoto.** Vuelve a tu terminal y ejecuta el comando `git remote add`. Reemplaza la URL con la tuya.
    ```bash
    git remote add origin [https://github.com/TuUsuario/mi_proyecto_anterior.git](https://github.com/TuUsuario/mi_proyecto_anterior.git)
    ```

### Paso 3: Subir tu Código a GitHub

1.  **(Opcional, buena práctica)** Antes de subir, puedes renombrar tu rama principal a `main` si Git la creó como `master` (es la convención moderna).

    ```bash
    git branch -M main
    ```

2.  **Sube tus commits a GitHub.** El comando `push` envía tus commits locales al repositorio remoto (`origin`). La opción `-u` establece una relación de seguimiento para que en el futuro solo necesites escribir `git push`.
    ```bash
    git push -u origin main
    ```

¡Y listo! Si ahora refrescas la página de tu repositorio en GitHub, verás todos los archivos de tu proyecto allí.
