import json
from urllib.request import urlopen

urlTest = "https://py4e-data.dr-chuck.net/comments_42.json" #Sum=2553
url = "https://py4e-data.dr-chuck.net/comments_2333714.json" #Sum ends with 49
#url = urlTest

jsonStr = urlopen(url).read().decode()
data = json.loads(jsonStr)

total = 0
for item in data['comments']:
    total += int(item['count'])

print('Count:', len(data['comments']))
print('Sum:', total)