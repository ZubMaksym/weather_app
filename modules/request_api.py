import requests
#імпортуємо функцію read_json, що дозволяє читати json файли 
from .read_json import read_json
#імпортуємо сам модуль json
import json
#створюємо змінну data_api та зчитуємо json файл config_api.json
data_api = read_json(name_file= 'config_api.json')
#створюємо константу API_KEY тa передаємо туди ключ "api_key" у якому зберігається хеш-ключ
API_KEY = data_api['api_key']
#створюємо константу CITY_NAME тa передаємо туди ключ "city_name" у якому зберігається назва міста
CITY_NAME = data_api['city_name']
#створюємо константу URL, куди вказуємо посилання, для отримання даних про погоду в місті
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#створюємо змінну response та застосовуємо функцію get(), яка отримує дані за вказаним посиланням 
response = requests.get(URL)
#Створюємо умову, якщо статус-код == 200, все працює коректно 
if response.status_code == 200:
    #створюємо змінну data_dict та застосовуємо функцію loads, яка перетворює байт-код в словник. 
    data_dict = json.loads(response.content)
    #Викликаємо функцію dumps, яка перетворює словники в str та робить текст більш читабельним, встановлює 4 пробіли
    print(json.dumps(data_dict, indent= 4))