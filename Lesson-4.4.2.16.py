import json

with open('food_services.json', encoding='utf-8') as file:
    services = json.load(file)
    services_by_type = {}
    for s in services:
        services_by_type.setdefault(s['TypeObject'], []).append(s)
    for service_type, service_data in sorted(services_by_type.items()):
        service_with_max_seats = max(service_data, key=lambda x: x["SeatsCount"])
        print(f"{service_type}: {service_with_max_seats['Name']}, {service_with_max_seats['SeatsCount']}")
