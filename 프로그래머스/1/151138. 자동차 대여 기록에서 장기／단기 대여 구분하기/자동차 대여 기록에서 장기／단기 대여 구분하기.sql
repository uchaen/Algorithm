SELECT c.HISTORY_ID,c.CAR_ID,DATE_FORMAT(c.START_DATE, "%Y-%m-%d") as START_DATE, DATE_FORMAT(c.END_DATE, "%Y-%m-%d") as END_DATE, 
CASE WHEN DATEDIFF(END_DATE, START_DATE) < 29 then '단기 대여' 
            ELSE '장기 대여' 
            END AS  RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY c
where month(c.start_date) = 9
order by c.history_id desc;
