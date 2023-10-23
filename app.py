from flask import Flask, jsonify, request
import math

app = Flask(__name__)

# Variáveis iniciais
theta = 0.0
a = 0.5
b = 0.2
delta_theta = 0.1  # incremento em theta para cada atualização

@app.route('/position', methods=['GET'])
def position():
    global theta
    # Calcular a posição r baseado no ângulo atual
    r = a + b * theta
    # Converter coordenadas polares em cartesianas
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    # Incrementar o ângulo para a próxima chamada
    theta += delta_theta

    # Aqui, a posição em z é mantida constante, mas você pode modificá-la se quiser movimento vertical
    z = 0.0

    # Retornar posição atual
    return jsonify({"x": x, "y": y, "z": z}), 200

if __name__ == '__main__':
    app.run(debug=True)
