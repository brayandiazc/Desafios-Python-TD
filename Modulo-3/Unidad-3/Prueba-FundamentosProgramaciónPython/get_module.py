# Importa
import requests
import json

# Paso 3: Función para realizar una solicitud GET y cargar la respuesta JSON
def request_get(url):
    return json.loads(requests.get(url).text)

if __name__ == '__main__':
    response = request_get('https://aves.ninjas.cl/api/birds')
    len(response)
    print(response)
