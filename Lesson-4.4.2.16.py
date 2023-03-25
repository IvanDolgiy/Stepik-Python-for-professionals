import json

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)
    d = {}
    lst = []
    for item in data:
        d.setdefault(item['TypeObject'],[]).append((item['Name'], item['SeatsCount']))
    for key, value in d.items():
        name = sorted(value, key=lambda x: x[1], reverse=True)[0]
        lst.append((key, name[0], str(name[1])))
    lst = sorted(lst, key= lambda x: x[0])
    for item in lst:
        print(item[0]+': '+item[1]+', '+item[2])