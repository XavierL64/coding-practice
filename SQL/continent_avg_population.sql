-- Exercise: For each continent, compute the average city population (rounded down).
-- Join CITY and COUNTRY on matching country codes, then group by continent.
SELECT co.continent, FLOOR(AVG(ci.population))
FROM city AS ci
JOIN country AS co ON ci.countrycode = co.code
GROUP BY co.continent;
