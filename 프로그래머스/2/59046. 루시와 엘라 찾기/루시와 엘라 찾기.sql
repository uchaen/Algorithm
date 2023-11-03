-- 코드를 입력하세요
SELECT a.ANIMAL_ID,a.NAME,a.SEX_UPON_INTAKE
from ANIMAL_INS a
where a.name = "Lucy" 
    or a.name = "Ella" 
    or a.name = "Pickle" 
    or a.name = "Rogan" 
    or a.name = "Sabrina" 
    or a.name = "Mitty"
order by animal_id