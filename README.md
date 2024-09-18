# Proyecto de Automatización con Playwright

Este repositorio contiene un proyecto de automatización utilizando Playwright. A continuación, se detallan los pasos para configurar el entorno y ejecutar el script `login.py` que se utiliza para iniciar sesión.

## Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. **Crear y activar un entorno virtual:**

   En Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   En macOS y Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Instalar Playwright y los navegadores:**

   ```bash
   playwright install
   ```

## Uso

1. **Ejecutar el script `login.py`:**

   El script `login.py` se utiliza para iniciar sesión en la aplicación. Asegúrate de que el entorno virtual esté activado y ejecuta el siguiente comando:

   ```bash
   python login.py
   ```

   Este script abrirá un navegador, navegará a la página de inicio de sesión y realizará las acciones necesarias para iniciar sesión.

## Estructura del Proyecto

- `login.py`: Script para iniciar sesión.
- `requirements.txt`: Archivo con las dependencias del proyecto.
- `venv/`: Carpeta del entorno virtual (no incluida en el repositorio).

## Notas

- Asegúrate de tener configuradas las credenciales necesarias en el script `login.py`.
- Si encuentras algún problema, revisa la documentación de [Playwright](https://playwright.dev/python/docs/intro).

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.

---

¡Gracias por usar este proyecto! Si tienes alguna pregunta, no dudes en contactarme.
