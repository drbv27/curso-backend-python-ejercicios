# 🐙 Clase 8: Control de Versiones con Git y GitHub

En esta clase fundamental, aprendimos a usar Git, la herramienta esencial para el control de versiones que todo desarrollador debe dominar.

## ✅ Temas Cubiertos

- **Control de Versiones (VCS):** Entendimos por qué es crucial para el historial, la colaboración y la seguridad de nuestro código.
- **Git vs. GitHub:** Diferenciamos entre Git (el software local) y GitHub (la plataforma remota de colaboración).
- **Configuración Inicial:** `git config --global user.name "..."` y `user.email "..."`.
- **Repositorio Local:**
  - Creación con `git init`.
  - **Los Tres Estados de Git:** Directorio de Trabajo -> Área de Preparación (Staging) -> Repositorio.
  - **Flujo Básico:** `git add`, `git commit -m "mensaje"`.
  - Revisión del estado (`git status`) y del historial (`git log`).
- **Ramificación (Branching):**
  - Concepto de ramas para aislar trabajo.
  - Crear (`git branch nombre`), cambiar (`git checkout nombre` o `switch`), y atajo (`checkout -b nombre`).
- **Fusión (Merging):**
  - Integrar cambios de una rama a otra con `git merge`.
- **Repositorios Remotos (GitHub):**
  - Conectar un repositorio local: `git remote add origin <URL>`.
  - Subir cambios: `git push`.
  - Descargar cambios: `git pull`.
  - Clonar un proyecto existente: `git clone <URL>`.
- **Conflictos de Fusión:** Introducción a qué son y cómo se resuelven de forma básica.

## 🧰 Guía Rápida de Comandos

| Comando                       | Descripción                                                                    |
| :---------------------------- | :----------------------------------------------------------------------------- |
| `git init`                    | Inicializa un nuevo repositorio Git en la carpeta actual.                      |
| `git status`                  | Muestra el estado de los archivos en el repositorio.                           |
| `git add <archivo>`           | Añade los cambios de un archivo al Staging Area. `git add .` para añadir todo. |
| `git commit -m "msg"`         | Guarda los cambios del Staging Area en el repositorio con un mensaje.          |
| `git log --oneline`           | Muestra un historial compacto de commits.                                      |
| `git branch <nombre>`         | Crea una nueva rama.                                                           |
| `git checkout <nombre>`       | Cambia a la rama especificada. `git checkout -b <nombre>` crea y cambia.       |
| `git merge <rama>`            | Fusiona los cambios de `<rama>` en la rama actual.                             |
| `git remote add origin <URL>` | Conecta tu repositorio local a un repositorio remoto en GitHub.                |
| `git push -u origin <rama>`   | Sube los commits de tu rama local a la rama remota en GitHub.                  |
| `git pull`                    | Descarga y fusiona los cambios desde el repositorio remoto a tu rama local.    |
| `git clone <URL>`             | Crea una copia local de un repositorio remoto existente.                       |

## 🎯 Tareas / Ejercicios Propuestos

1.  **Versionar un Proyecto Anterior:**
    - Elige uno de los proyectos o prácticas que hiciste en las clases anteriores (ej: el de la calculadora de la Clase 2, o el gestor de notas de la Clase 7).
    - Crea un **nuevo repositorio vacío** en GitHub para ese proyecto.
    - En tu máquina local, navega a la carpeta de ese proyecto y ejecuta `git init`.
    - Realiza un primer commit con todos los archivos del proyecto.
    - Conecta tu repositorio local con el remoto que creaste en GitHub.
    - Sube tus cambios a GitHub usando `git push`.
2.  **Practicar el Flujo de Ramas:**
    - En el repositorio que acabas de subir, crea una nueva rama llamada `feature/mejorar-readme`.
    - En esa rama, edita el archivo `README.md` del proyecto, añadiendo una mejor descripción de lo que hace.
    - Haz un commit con ese cambio en la rama `feature`.
    - Vuelve a tu rama principal (`main`).
    - Fusiona la rama `feature/mejorar-readme` en `main`.
    - Sube los cambios de `main` a GitHub.

---

_Puedes encontrar una guía paso a paso de cómo resolver la Tarea 1 en la carpeta `Soluciones/Clase_08/`._
