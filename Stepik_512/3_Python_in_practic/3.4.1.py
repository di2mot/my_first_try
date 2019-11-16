import requests
import re


pattern = r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)"

# url = str(input().strip())
url = 'http://pastebin.com/raw/hfMThaGb'
get_url = requests.get(url)
# get_url = requests.get('http://pastebin.com/raw/hfMThaGb')

href = re.findall(pattern, get_url.text)
href.sort()
for i in href:
    print(i[8])

