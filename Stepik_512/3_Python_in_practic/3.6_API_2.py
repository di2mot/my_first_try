import requests
import json
from operator import itemgetter

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsInN1YmplY3RfYXBwbGljYXRpb24iOiI1ZTBjYzhkNGIyMDQyMTAwMGU3YWM3MjkiLCJleHAiOjE1NzkzNzA3MDEsImlhdCI6MTU3ODc2NTkwMSwiYXVkIjoiNWUwY2M4ZDRiMjA0MjEwMDBlN2FjNzI5IiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjVlMWEwZTRkNTgzYmIzMDAwZWZlOTFiNSJ9.gMWvsNNkbLzY84Zt0xKJC6Gj00OAD6qDCsmULVUrJRw'

url = 'https://api.artsy.net/api/artists/'
dict = {}

client_id = '95e1d3c19b3c6a87e0fa'
client_secret = '3ff623b3be9dad033d346f72f114015a'

# # инициируем запрос на получение токена
# r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                   data={
#                       "client_id": client_id,
#                       "client_secret": client_secret
#                   })
#
# # разбираем ответ сервера
# j = json.loads(r.text)
#
# # достаем токен
# token = j["token"]
# print(token)


def api(id):
    url_art = url + id.rstrip()
    # создаем заголовок, содержащий наш токен
    headers = {'X-Xapp-Token': token}
    # инициируем запрос с заголовком
    r = requests.get(str(url_art), headers=headers)
    r.encoding = 'utf-8'
    # разбираем ответ сервера
    j = json.loads(r.text)
    # print(j)
    name = j['sortable_name']
    date = j['birthday']
    return name, date


with open('api_test.txt', 'r', newline="") as file:
    line = file.readlines()
    for line in line:
        line = line.rstrip()
        # print(line)
        ART = api(line)
        # print(ART)
        dict[ART[0]] = ART[1]

print(dict)

artist = sorted(dict.items(), key=itemgetter(1,0))
# print(artist)
for i in artist:
    print(i[0])

