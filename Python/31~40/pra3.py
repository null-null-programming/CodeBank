import json
age = {'ken': 12, 'ryu': 30}
with open('31~40/write.json', 'w') as f:
    json.dump(age, f)

with open('31~40/write.json', 'r') as f:
    print(json.load(f))
    