import json

# data = [{"name": "DH", "parents": ["D", "BF", "DE", "AE"]}, {"name": "D", "parents": ["AE"]}, {"name": "B", "parents": []}, {"name": "AE", "parents": ["F"]}, {"name": "BG", "parents": ["H", "CH"]}, {"name": "H", "parents": []}, {"name": "E", "parents": ["CG", "B"]}, {"name": "BH", "parents": ["CG"]}, {"name": "CE", "parents": []}, {"name": "CH", "parents": ["E"]}, {"name": "C", "parents": ["CE"]}, {"name": "A", "parents": []}, {"name": "DE", "parents": ["BH"]}, {"name": "F", "parents": []}, {"name": "CG", "parents": ["C", "G"]}, {"name": "G", "parents": []}, {"name": "BF", "parents": ["F"]}]
# data_json = json.dumps(data, indent=4, sort_keys=True)
# data_again = json.loads(data_json)

data = input()
data_again = json.loads(data)

data_dict = dict()
temple_dict = {}
fin_dict = {}

''' превращаю в словарь нужного мне вида, где ключ'key' =  значение ключа'name' '''

for i in data_again:
    temple_dict[i['name']] = list()

''' 
Тут перебираю изначальный словарь, и перебираю ключи словаря "temple_name",
если ключ из "temple_name", находится в data_name['parents'], 
то я добавляю в ключу "temple_name", имя ключа ata_name['name']

Т.о. создаю словарь типа "родитель" : "потомки",  вместо "предок" : "родители" 
'''

for data_name in data_again:
    for temple_name in temple_dict:
        if temple_name in data_name['parents']:
            temple_dict[temple_name].append(data_name['name'])



def iteractive_dfs(graph, start, path=None):
    """iterative depth first search from start"""
    if path is None:
        path = []
    q = [start]
    while q:
        v = q.pop()
        if v not in path:
            path = path + [v]
            q += graph[v]
    return path

for key in sorted(temple_dict.keys()):
    print(key, ':', len(iteractive_dfs(temple_dict, key)))