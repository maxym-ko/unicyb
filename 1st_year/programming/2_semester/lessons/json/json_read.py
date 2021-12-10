import json

with open('good.json') as f:
    json_dict = json.load(f)

print(json_dict)
