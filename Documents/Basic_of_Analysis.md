# Analysis.md
---


# 데이터 분석 준비 

- pandas(데이터처리, 분석), numpy(수학,과학용)등을 사용     
- 데이터의 품질을 향상시킨다 여기에 주안점    
  1. 데이터 정제 : 결측치, 이상치 처리        
  2. 데이터 통합 : 여러 군데서 가져온 데이터를 조합, 데이터구성    
  3. 데이터 변환 : 데이터를 모델(4-5단계)에서 적합하게 사용되도록 변경 처리        

1. **pandas**

- numpy를 기반으로 R에 대응하기 위해서 파이썬 진영에서 만든 데이터 분석용 라이브러리   

- 데이터 전처리(정제, 통합, 변환) 
  => 시각화 => 통찰!!   
  - pandsas는 R의 핵심 데이터 시리즈와 프레임을 파이썬에 추가한 것

  - > Series(시리즈), DataFrame(데이터프레임)          
    > DataFrame의 인덱싱 
      => Series의 인덱싱 
      => 값(스칼라), 수치, 문자, 블린, NaN 이 등장  > Series: 인덱스와 데이터만 존재하는, 컬럼이 없는 자료구조  
    > DataFrame: 인덱스와 컬럼이 존재하는 자료구조        
    > NaN : 데이터가 없다. (난, 넌), Not a Number => np.nan       

