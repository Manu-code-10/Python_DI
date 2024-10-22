# -*- coding: utf-8 -*-
"""
Código para subir de forma automática a github
"""

import subprocess
from datetime import datetime

# Define los comandos de git
def git_push(repo_path):
    try:
        # Obtener la fecha actual en formato dd/mm/aaaa
        fecha_actual = datetime.now().strftime("%d/%m/%Y")

        # Definir el mensaje del commit
        commit_message = f"Actualización {fecha_actual} desde Python"

        # Agregar todos los archivos modificados
        subprocess.run(["git", "add", "."], check=True, cwd=repo_path)

        # Hacer el commit con el mensaje que incluye la fecha
        subprocess.run(["git", "commit", "-m", commit_message], check=True,
                       cwd=repo_path)

        # Subir los cambios a la rama principal (main)
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True,
                       cwd=repo_path)

        print(f"Commit realizado con el mensaje: '{commit_message}'")
        print("Archivos subidos a GitHub correctamente.")

    except subprocess.CalledProcessError as e:
        print(f"Error durante la ejecución de Git: {e}")

# Ruta a tu repositorio local
repo_path = "C:/Programacion/Python/"  

# Llamar a la función para hacer el push
git_push(repo_path)

