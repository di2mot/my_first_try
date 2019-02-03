import requests
with open('D:\\1.txt') as inf:
    r = requests.get(inf.readline().strip()).text
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
print(url + r)
coin = 0
while 'We' not in r:
    r = requests.get(url + r).text
    print(r)
    coin += 1
print(coin)

