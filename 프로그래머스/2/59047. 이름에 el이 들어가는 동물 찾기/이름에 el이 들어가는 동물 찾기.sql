-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.NAME
from ANIMAL_INS a
where a.name like "%el%" and a.animal_type = "Dog"
order by name
