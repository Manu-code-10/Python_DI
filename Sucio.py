# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:40:40 2024

@author: Usuario
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, mundo!"

if __name__ == '__main__':
    app.run(debug=True)




