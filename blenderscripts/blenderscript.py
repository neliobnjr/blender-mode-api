import bpy
import requests
import time

def update_position_from_api():
    # Defina o endereço do servidor
    url = "http://localhost:5000/position"
    
    while True:
        try:
            # Faça uma requisição para obter a posição atual
            response = requests.get(url)
            data = response.json()

            # Atualizar a posição do objeto no Blender
            obj = bpy.data.objects["Cube"]  # Supondo que você esteja controlando um objeto chamado "Cube"
            obj.location.x = data['x']
            obj.location.y = data['y']
            obj.location.z = data['z']

            time.sleep(2)  # Faça uma pausa de 2 segundos entre cada consulta

        except Exception as e:
            print("Erro:", e)
            time.sleep(10)  # Se ocorrer um erro, espere um pouco mais antes de tentar novamente

# Execute a função em um novo thread para que não bloqueie a UI do Blender
import threading
thread = threading.Thread(target=update_position_from_api)
thread.start()
