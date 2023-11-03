-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.NAME, DATE_FORMAT(a.datetime,"%Y-%m-%d") as 날짜
from ANIMAL_INS a
order by ANIMAL_ID
