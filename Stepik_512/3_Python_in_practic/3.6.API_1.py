import requests
import json

number = ['932', '934','924','909','976','915','980','979','916','917','920','985','954','956','922']

for i in number:

    url = f'http://numbersapi.com/{i}/math?json=true'

    res = requests.get(url)

    data = res.json()

    if data['found'] is not False:
        print('Interesting')
    else:
        print('Boring')

