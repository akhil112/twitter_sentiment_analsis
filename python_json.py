import json

file=json.open('json.json').open()
data = json.loads(file)
for item in data:
    print item