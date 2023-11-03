-- 코드를 입력하세요
# select DISTINCT 
# from PRODUCT pp;


SELECT LEFT(p.PRODUCT_CODE,2) as CATEGORY, COUNT(*) as PRODUCTS
from PRODUCT p
group by LEFT(p.PRODUCT_CODE,2)
