-- 코드를 입력하세요
SELECT i.INGREDIENT_TYPE, SUM(f.total_order) as TOTAL_ORDER
from ICECREAM_INFO i, first_half f
where i.flavor=f.flavor
group by i.INGREDIENT_TYPE