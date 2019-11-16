import requests
import re

url_1 = 'https://stepic.org/media/attachments/lesson/24472/sample.html'
url_2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'


pattern = r'<a href=\"(.*)\"'

# url_1, url_2 = input(), input()

def status(url):
    get = requests.get(url)
    href = re.findall(pattern, get.text)
    return href

def url_cheker(url, url_2):
    for i in url:
        if str(i) in url_2:
            return 'Yes'


get = status(url_1)
while True:
    if not get:
        print("No")
        break
    else:
        try:
            for url in get:
                get_1 = status(url)
                if url_cheker(get_1, url_2) is "Yes":
                    print('Yes')
                    print(a)
            print('No')
            break
        except: break