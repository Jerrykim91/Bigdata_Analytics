# bs01.py

from bs4 import BeautifulSoup

with open('./resources/exam01.html',encoding="utf-8") as fp :
    # 복잡한 HTML 문서를 복잡한 Python 객체 트리로 변환
    # fp = url 같은 개념
    soup = BeautifulSoup(fp, 'html.parser')

    # div 태그 전체 찾기 
    all_divs = soup.find_all("div")
    # 이유 ?? 
    soup.find_all("div",{"class":"first"})
    # print(all_divs)

    # div 태그 첫번째 찾기 
    first_div = soup.find("div")
    #print(first_div)


# print('-'*30)
# for i in first_div : 
#     print(i) # 하나씩 출력 
# 데이터 확인 
# for i in all_divs : 
#     print(i)
# print('-'*30)

print('-'*30)
for tmp in all_divs:
    # print(tmp) # 전부를 보고 
    all_p = tmp.find_all("p") # p만 찾을거야 
    for tmp1 in all_p : 
        print(tmp1) # p만 출력된 것을 확인 
        print(tmp1.text) # 그 중에 텍스트만 출력 
print('-'*30)