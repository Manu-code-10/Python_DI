
"""
Mi primera API
"""
# %% 1. Importación de módulos
from flask import Flask, jsonify

#%% 2. Código
app = Flask(__name__)
# Ruta principal con respuesta en formato JSON
@app.route('/api', methods=['GET'])
def obtener_datos():
    # Datos en formato JSON
    datos = {
        "nombre": "Javi",
        "edad": 19,
        "ciudad": "Seseña"
    }
    return jsonify(datos)

# Ruta para obtener una lista de datos
@app.route('/api/lista', methods=['GET'])
def obtener_lista():
    lista_datos = [
        {"nombre": "Sebastián", "edad": 19, "ciudad": "Seseña"},
        {"nombre": "Javier", "edad": 19, "ciudad": "Seseña"},
        {"nombre": "Manu", "edad": 26, "ciudad": "Illescas"}
    ]
    return jsonify(lista_datos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)