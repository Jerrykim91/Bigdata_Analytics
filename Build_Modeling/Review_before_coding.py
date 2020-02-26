# 코드정리

sample = '''
https://ko.wikipedia.org/wiki/방탄소년단
https://en.wikipedia.org/wiki/BTS_(band)
https://fr.wikipedia.org/wiki/BTS_(groupe)
참고자료 => https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 

'''

# import
import urllib.request as rq 
from bs4 import BeautifulSoup
import re


target_url = 'https://en.wikipedia.org/wiki/BTS_(band)'
res = rq.urlopen(target_url)
soup = BeautifulSoup(res,'html5lib')

ps = soup.select('#mw-content-text p')
tmp = [ p.text.strip() for p in ps]
src_text = ' '.join(tmp)

p = re.compile('[a-zA-Z ]*') 
tmp = p.sub( '' ,  src_text )
tmp.lower()[:100]

