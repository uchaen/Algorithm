-- 코드를 입력하세요
SELECT DISTINCT h.CAR_ID
from CAR_RENTAL_COMPANY_CAR c, CAR_RENTAL_COMPANY_RENTAL_HISTORY h
where MONTH(h.START_DATE)=10 
    and h.CAR_ID = c.CAR_ID
    and c.CAR_TYPE = "세단"
order by h.CAR_ID desc