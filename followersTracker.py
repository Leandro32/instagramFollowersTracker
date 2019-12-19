from bs4 import BeautifulSoup
import requests
import json

instagram = 'https://www.instagram.com'

# usuario = input('Ingrese el usuario: ')
# url = instagram + '/' + usuario
# print('Usuario : ', usuario)

url = instagram + '/' + 'leomessi'  # prueba con Lionel Messi
print('Usuario : leomessi')
print("URL del perfil: " + url)

response = requests.get(url)

if response.ok:
    while response.ok:
        response = requests.get(url)
        html = response.text
        bs_html = BeautifulSoup(html, features="html.parser")

        scripts = bs_html.select('script[type="application/ld+json"]')  # Extrae el script que contiene la cantidad de seguidores
        datos_json = json.loads(scripts[0].text.strip())  # Transforma a json
        mainEntityofPage = datos_json['mainEntityofPage']
        interactionStatistic = mainEntityofPage['interactionStatistic']
        userInteractionCount = interactionStatistic['userInteractionCount']

        print('Numero de seguidores: '+ userInteractionCount)
