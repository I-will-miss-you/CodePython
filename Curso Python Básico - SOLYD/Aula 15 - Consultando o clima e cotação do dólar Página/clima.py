#############################
#       OpenWeatherMap      #
#############################
import requests
from json import loads


key = 'APPID=your_key'

city_name = input('Cidade: ')
country_code = input('Codigo Pais: ')

str = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&{key}'
req = requests.get(str)

tempo = loads(req.text)

print('Condição: ', tempo['weather'][0]['main'])
print(f"Temperatura: {(float(tempo['main']['temp']) - 273.15):.2f}ºC")
