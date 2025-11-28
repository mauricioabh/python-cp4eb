# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urlTest = "http://py4e-data.dr-chuck.net/comments_42.html" #sum = 2553
url = "http://py4e-data.dr-chuck.net/comments_2333711.html" #sum ends with 12

#url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
spans = soup('span')
total = 0
count = 0
for span in spans:
    # Look at the parts of a tag
    total += int(span.contents[0])
    count += 1

print('Enter -', url)
print('Count', count)
print('Sum', total)