from xml.etree.ElementTree import parse


doc = parse('./resources/exam01.xml')
# ?
a = doc.findall("student")
print(a)





for tmp in a : 
    print(tmp)
    print('='*30)
    print(tmp.findtext("name")) # <name>a</name>
    print('='*30)
    print(tmp.findtext("age"))# <age>a</age>
    print('='*30)
    print(tmp.find("addr").attrib) # <addr id='a'>a</age>
    print('done')
