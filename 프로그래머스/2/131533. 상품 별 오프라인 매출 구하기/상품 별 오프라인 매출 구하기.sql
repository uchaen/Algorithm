-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, SUM(o.SALES_AMOUNT*p.PRICE) as SALES
from PRODUCT p, OFFLINE_SALE o
where p.PRODUCT_ID = o.PRODUCT_ID
group by p.PRODUCT_CODE
order by 2 DESC, 1