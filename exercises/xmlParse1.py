import urllib.request
import xml.etree.ElementTree as ET

urlTest="http://py4e-data.dr-chuck.net/comments_42.xml" #Sum=2553
url="http://py4e-data.dr-chuck.net/comments_2333713.xml" #Sum ends with 7
#url = urlTest

#url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    # print(result.text)
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))

