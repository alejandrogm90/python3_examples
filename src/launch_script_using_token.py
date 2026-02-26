import os
import sys
from pprint import pprint

import requests

from dotenv import load_dotenv


def obtener_token(url: str, datos: dict) -> str | None:
    """Realiza una petición para obtener un token."""
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=datos)

    if response.status_code == 200:
        return str(response.json().get('access'))  # Cambia 'token' por la clave correcta si es diferente
    else:
        print(f"Error al obtener token: {response.status_code}")
        #print(f"{response.text}")
        return None


def hacer_peticion_con_token(url: str, token: str, datos: dict):
    """Realiza una petición usando el token obtenido."""
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    response = requests.post(url, headers=headers, json=datos)

    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error en la petición: {response.status_code}")
        #print(f"{response.text}")
        return None


def get_last_launches(url: str, token: str):
    """Realiza una petición usando el token obtenido."""
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error en la petición: {response.status_code}")
        #print(f"{response.text}")
        return None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'ERROR: {sys.argv[0]} SCRIPT_NAME ARGUMENTS....')
        sys.exit(1)

    # Load ENV
    load_dotenv()

    host_name = os.getenv('MY_HOST_NAME', 'http://localhost:8000')
    url_token = f'{host_name}/api/token/'
    user_dict = {
        'username': 'user1',
        'password': 'user1user1'
    }

    token_str = obtener_token(url_token, user_dict)

    if token_str:
        if sys.argv[1] == "-l" or sys.argv[1] == "--list":
            datos_obtenidos = get_last_launches(f'{host_name}/api/list/', token_str)
        else:
            links_dict = {
                "nombre": sys.argv[1],
                "comandos": " ".join(sys.argv[2:])
            }
            datos_obtenidos = hacer_peticion_con_token(f'{host_name}/api/launch/', token_str, links_dict)
        pprint(datos_obtenidos)
