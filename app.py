from flask import Flask, jsonify, request
import math

app = Flask(__name__)

# Variáveis iniciais
theta = 0.0
a = 0.5
b = 0.2
delta_theta = 0.1 

@app.route('/position', methods=['GET'])
def position():
    global theta
    
    r = a + b * theta
    
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    theta += delta_theta

    
    z = 0.0

    
    return jsonify({"x": x, "y": y, "z": z}), 200

if __name__ == '__main__':
    app.run(debug=True)
