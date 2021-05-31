SELECT
    name AS "name",
    population AS "population",
    area AS "area"
FROM
    World
WHERE
    area > 3000000
    OR population > 25000000;
