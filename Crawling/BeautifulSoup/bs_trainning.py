# bs_trainning.py 
# import = BeautifulSoup
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 네이버 금융 -> 고시 환율 정보 수집 
url = "https://finance.naver.com/marketindex/exchangeList.nhn"
# 요청 응답 get 
# urllib.request.urlopen( url , data = None , [ timeout , ] * , cafile = None , capath = None , cadefault = False , context = None ) 
# 문자열 또는 객체 일수 있는 URL을 연다 
str = urlopen(url) 
soup = BeautifulSoup( str, 'html.parser')
print(str)



data = soup.find_all('td','tit')
data_m = soup.find_all('td','sale')

# 리스트 내포형 
# tmp_tit_list = [td.a.string.strip() for td in soup.find_all('td','tit')]
# print(tmp_tit_list)


tmp_tit = [] 
for td in data : 
    tmp_tit.append(td.a.string.strip())
print(tmp_tit[:5])

# 리스트 내포형 
# tmp_sale_list = [td.string.strip() for td in soup.find_all('td','sale')]
# print(tmp_sale_list)

tmp_sale = [] 
for td in data_m:
    tmp_sale.append(td.string.strip())
print(tmp_sale[:5])

# 만약 대상 페이지에 table이 n개 존재하면 특정해서 찾야함 
# table.tbl_exchange > tbody > tr
# body > div > table > tbody > tr:nth-child(1) > td:nth-child(4)

sec = soup.select('table.tbl_exchange > tbody > tr')
# 원하는 데이터를 검사하는 tr을 찾아서 그밑에서 자식들을 탐색 후 거기서 데이터를 추출 
for tr in sec : 
    # 데이터 한줄 한줄 뽑아서 => tr에서 탐색하여 세부 데이터 추출 

    # 나라 
    print(tr.select_one('td.tit').string.strip())
    # 매매기준율 
    print(tr.select_one('td.sale').string.strip())
    # 팔떄
    print(tr.select('td')[3].string.strip())



# 이걸를 json 형식으로 변경 
results = [] 
for tr in soup.select('table.tbl_exchange > tbody > tr'):
    if tr.select_one('td.tit').a.string.strip().count('JPY') == 0:
        tmp = dict()
        # 나라 이름 
        tmp['Name'] = tr.select_one('td.tit').a.string.strip()
        # 나라 코드(..USD)
        tmp['Code'] = tr.select_one('td.tit').a['href'][-6:-3]
        # 매매기준율 
        tmp['Buy_std_rate'] = tr.select_one('td.sale').string.strip()
        # 팔떄
        tmp['Cash_sell'] = tr.select('td')[3].string.strip()
        results.append(tmp)

print(results)



# 리스트 내포 
results_list = [{
    'name': tr.select_one('td.tit').a.string.strip(),
    'Code': tr.select_one('td.tit').a['href'][-6:-3],
    'Buy_std_rate': tr.select_one('td.sale').string.strip(),
    'Cash_sell' : tr.select('td')[3].string.strip()
    } 
    for tr in soup.select('table.tbl_exchange > tbody > tr') 
    if tr.select_one('td.tit').a.string.strip().count('JPY')==0
    ]

print(results_list[:2])



# 'html5lib' parser는 html 양이 크거나, 정교한 파싱을 할때 
# 즉, 아래 parser가 정상적으로 결과를 내지 못하면 이 parser로 교체

# 파싱(Parsing)
# 언어학에서 Parsing은 데이터를 조립해 원하는 데이터를 빼 내는 프로그램하는것 
# parsing은 일련의 문자열을 의미있는 token으로 분해하고 그것들로 이루어진 Parse_tree를 만드는 과정
# 특정 문서를 읽어들여 다른 프로그햄이나 서브루틴이 사용할수있는 내부의 표현식으로 변환시켜주는 것
# 입력받은 데이터의 구문을 해석할 수있는 단위로 분할 해주는 역활
  
# Parsing 기법으로 XMl 파싱 기법인 DOM과 SAX / JSON 파싱 기법


# 파서(Parser)
# 파싱을 하는 프로세서 = 파서가 파씽한다
# raw 데이터를 읽어드려 문장구조를 알아내는 구문 분석을 하는 프로그램 
