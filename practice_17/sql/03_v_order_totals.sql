--sales_lh

CREATE OR ALTER VIEW dbo.v_order_totals AS
SELECT 
    SalesOrderNumber AS sales_order_number,
    OrderDate AS order_date,
    EmailAddress AS customer_email,
    COUNT(*) AS lines_cnt,
    ROUND(SUM(Quantity*UnitPrice), 2) AS amount,
    ROUND(SUM(TaxAmount), 2) AS tax,
    ROUND(SUM(Quantity*UnitPrice)+SUM(TaxAmount), 2) AS total
FROM dbo.sales
GROUP BY SalesOrderNumber, OrderDate, EmailAddress;

GO

SELECT 
    sales_order_number, 
    order_date, 
    customer_email,
    lines_cnt,
    amount,
    tax,
    total 
FROM dbo.v_order_totals
WHERE lines_cnt >= 5
ORDER BY total DESC, sales_order_number ASC;