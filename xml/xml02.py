from xml.etree.ElementTree import parse
# import requests  # 안되고 
from urllib.request import urlopen


# url 호출
# url = "http://ihongss.com/xml/exam1.xml"
# str = requests.get(url)
# doc = parse(str.text)
# print(doc)


url = "http://ihongss.com/xml/exam1.xml"
str = urlopen(url)
doc1 = parse(str)
print(doc1)


for item in doc1.iterfind('items/item'):
    print(item.attrib)
    print(item.findtext('name')) # <name>a</name>



