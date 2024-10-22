# -*- coding: utf-8 -*-
"""
Código para subir de forma automática a github
"""

import subprocess as git
from datetime import datetime

# Define los comandos de git
def git_push(repo_path):
    try:
        # Obtener la fecha actual en formato dd/mm/aaaa
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")

        # Definir el mensaje del commit (mensaje de subida)
        commit_message = f"Actualización {fecha_actual} desde Python"

        # Agregar todos los archivos modificados (solo agregamos archivos
        # modificados después del anterior commit)
        git.run(["git", "add", "."], check=True, cwd=repo_path)

        # Hacer el commit con el mensaje que incluye la fecha
        git.run(["git", "commit", "-m", commit_message], check=True,
                       cwd=repo_path)

        # Subir los cambios a la rama principal (main)
        git.run(["git", "push", "-u", "origin", "main"], check=True,
                       cwd=repo_path)

        print(f"Commit realizado con el mensaje: '{commit_message}'")
        print("Archivos subidos a GitHub correctamente.")

    except git.CalledProcessError as e:
        print(f"Error durante la ejecución de Git: {e}")

# Ruta a tu repositorio local (¡DEL ORDENADOR!)
repo_path = "C:/Programacion/Python/"  

# Llamada a la función para subir los archivos
git_push(repo_path)

