-- 코드를 입력하세요
SELECT u.BOARD_ID, u.WRITER_ID, u.TITLE, u.PRICE,
CASE when u.STATus = "SALE" then "판매중"
when  u.STATus = "RESERVED" then "예약중"
else "거래완료"
end as STATUS
FROM USED_GOODS_BOARD u
where u.CREATED_DATE = "2022-10-05"
order by u.BOARD_ID desc;