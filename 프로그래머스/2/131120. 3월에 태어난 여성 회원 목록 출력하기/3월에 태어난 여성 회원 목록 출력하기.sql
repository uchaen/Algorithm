-- 코드를 입력하세요
SELECT m.MEMBER_ID, m.MEMBER_NAME, m.GENDER, DATE_FORMAT(m.DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE m
where MONTH(m.DATE_OF_BIRTH)=3 AND m.TLNO IS NOT NULL AND m.GENDER="W"
order by m.MEMBER_ID