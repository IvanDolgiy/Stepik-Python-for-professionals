import json
from collections import defaultdict

with open('food_services.json', encoding='utf-8') as file:
    services = json.load(file)
    service_groups = defaultdict(list)
    for s in services:
        service_groups[s["TypeObject"]].append(s)
    for service_type, service_data in sorted(service_groups.items()):
        max_item = max(service_data, key=lambda item: item["SeatsCount"])
        print(f"{service_type}: {max_item['Name']}, {max_item['SeatsCount']}")
