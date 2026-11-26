--sales_wh

SELECT TOP (10)
    c.CustomerKey AS customer_key,
    CONCAT(c.FirstName, ' ', c.LastName) AS customer_name,
    c.City AS city,
    c.CountryRegion AS country_region,
    COUNT(*) AS orders_cnt,
    MIN(d.DateAltKey) AS first_order_date,
    MAX(d.DateAltKey) AS last_order_date,
    SUM(f.SalesTotal) AS total_spent
FROM dbo.FactSalesOrder AS f
INNER JOIN dbo.DimCustomer AS c
    ON c.CustomerKey = f.CustomerKey
INNER JOIN dbo.DimDate AS d
    ON d.DateKey = f.SalesOrderDateKey
GROUP BY
    c.CustomerKey,
    c.FirstName,
    c.LastName,
    c.City,
    c.CountryRegion
ORDER BY
    total_spent DESC,
    customer_key;