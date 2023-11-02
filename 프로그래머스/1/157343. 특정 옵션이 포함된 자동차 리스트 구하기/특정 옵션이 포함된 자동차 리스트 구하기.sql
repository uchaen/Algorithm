-- 코드를 입력하세요
SELECT c.CAR_ID, c.CAR_TYPE, c.DAILY_FEE, c.OPTIONS
from CAR_RENTAL_COMPANY_CAR c
where c.options like "%네비게이션%"
order by c.car_id desc;