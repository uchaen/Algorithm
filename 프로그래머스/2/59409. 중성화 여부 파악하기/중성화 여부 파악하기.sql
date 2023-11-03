-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.NAME, case 
    when a.SEX_UPON_INTAKE like "Neutered%" then "O"
    when a.SEX_UPON_INTAKE like "Spayed%" then "O"
    else "X"
    end as "중성화"
from ANIMAL_INS a