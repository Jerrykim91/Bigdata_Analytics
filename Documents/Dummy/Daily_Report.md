# Crawling
---

---

### 차이 

- 크롤링

  - **데이터를 수집하고 분류하는 것**
  - 일종의 스크래핑 기술,조직적, 자동화된 방법 

- 파싱 

  - 내가 원하는 데이터를 **특정 패턴이나 순서로 추출하여 정보를 가공**하는 것 -> 일련의 문자열을 의미있는 토큰으로 분해하고 이들로 만들어진 파스 트리를 만드는 과정을 말한다. 

-  스크레핑 

  - **웹사이트의 데이터를 수집하는 모든 작업**




### 2020.01.16
 
- SQL에서 새 테이블 생성(MEMBER1)
    - NO(PK - NUMBER - NO NULL)    
    - ID(VARCHAR2 - 20)       
    - AGE(NUMBER)       
    - NAME(VARCHAR2 - 20)    


- SQL에서 새 테이블 생성(ITEM1)
    - NO_(PK - NO NULL)    :물품번호
    - NAME_(VARCHAR2 - 20) : 물품명
    - CONTENT(CLOB)        : 물품설명
    - PRICE(NUMBER)        : 가격
    - REGDATE(DATE)        : 등록일자

- 편집     
    => DATA_DEFAULT( PK인 아이들만 - SEQ_테이블이름_NO.nextval )

```SQL
-- 
CREATE SEQUENCE SEQ_ITEM1_NO
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCACHE;
COMMIT;

--SEQ_ITEM1_NO.nextval 기본값으로 설정 
-- DATA_DEFAULT(PK인 아이들만 - SEQ_테이블이름_NO.nextval )
INSERT INTO ITEM1( NO, NAME, CONTENT, PRICE, REGDATE )
VALUES ( SEQ_ITEM1_NO.nextval, 'a', 'b', 1200, SYSDATE );
COMMIT;
```
- SQL에서 새 테이블 생성(ORDER1)     
    - NO_(PK - NO NULL)        
    - MEN_NO(NUMBER)           
    - ITM_NO(NUMBER)          
    - REGDATE(DATE)       
** SEQ_ITEM1_NO.nextval



```SQL
-- 
INSERT INTO ITEM1(NAME,CONTENT, PRICE, REGDATE) 
VALUES('c','내용들', 5200, SYSDATE);
COMMIT;

```

### 테이블 편집 ( ORDER1 만 )   
    - 제약조건     
    - (+) 연결하려면 새 외래키 제약조건

        스키마 : ADMIN   
        이름   : ORDER1
        테이블 : 해당 테이블      
        - 복제를 안하기위해서 유기적으로 연동해서 사용하려고 

        >> 참조된 제약 조건 <<
        ITEM1   => ITM_NO
        MEMBER1 => MEN_NO     

```SQL
SELECT * FROM TABLE1 t1
INNER JOIN ORDER1 t2
ON t1.no = t2.men_no;
```

- 외래키 
---
### 2020.01.15
[크롬 버전별](https://chromedriver.chromium.org/downloads)




참고 : https://apscheduler.readthedocs.io/en/v2.1.2/cronschedule.html
---
### 2020.01.14

- CSV 
- 스크래핑 

---
### 2020.01.13
실습 1 - http://ihongss.com/json/exam2.json     
실습 2 - http://ihongss.com/json/exam3.json     
실습 3 - http://ihongss.com/json/exam3.json    
실습 4 - http://ihongss.com/json/exam4.json    
---


