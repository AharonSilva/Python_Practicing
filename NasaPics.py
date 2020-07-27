import json
import requests

data = requests.get('http://epic.gsfc.nasa.gov/api/images.php')

data = json.loads(data.content)

for i in data:
    print('http://epic.gsfc.nasa.gov/epic-archive/jpg/' + i['image'] + '.jpg')
