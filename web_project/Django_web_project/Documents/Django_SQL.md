
# 정리중



```
SELECT
    NULL(MAX(NO),0)
FROM
    board_table1
WHERE
    NO <%s      <=13
    
    -- SQL문을 짤때 NULL(0) 처리 해줘야한다. 
    -- 있으면 그숫자 없으면 '0'이 넘어옴
    
```


```
SELECT
    NULL(MAX(NO),0)
FROM
    board_table1
WHERE
    NO <%s      <=13
    
    -- SQL문을 짤때 NULL(0) 처리 해줘야한다. 
    -- 있으면 그숫자 없으면 '0'이 넘어옴
    
```


-- 새 글 추가 
INSERT INTO board_table1
    (TITLE, CONTENT, WRITER, HIT, REGDATE)
VALUES
    ('SQL에서 TEST', '내용임','관리자',1004,SYSDATE);
COMMIT;
-- 27번 글 삭제
DELETE FROM board_table1 WHERE NO = 27;
COMMIT;

-- 글 수정 
UPDATE board_table1 SET TITLE='관리자임', CONTENT=' 관리자 뿡뿡이? 그러시면 안됩니다. ' WHERE NO =29;
COMMIT;

-- 조회
-- 모든정보
SELECT * FROM board_table1;
-- 내림차순
SELECT * FROM board_table1 ORDER BY TITLE DESC;

-- 정렬
SELECT * FROM board_table1 WHERE NO =3;
