-- Oracle에서 나머지 연산은 MOD()로 구해야 함! (%는 안 됨!)
-- 그러나 몫은 그냥 / 하면 나옴!

SELECT *
FROM cinema
WHERE
    MOD(id ,2) = 1
    AND description != 'boring'
ORDER BY rating DESC;
