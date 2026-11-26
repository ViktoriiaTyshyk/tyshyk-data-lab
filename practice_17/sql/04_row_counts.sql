--sales_wh

SELECT 'DimCustomer' AS table_name, COUNT(*) AS rows_cnt FROM dbo.DimCustomer
UNION ALL
SELECT 'DimDate' AS table_name, COUNT(*) AS rows_cnt FROM dbo.DimDate
UNION ALL
SELECT 'DimProduct' AS table_name, COUNT(*) AS rows_cnt FROM dbo.DimProduct
UNION ALL
SELECT 'FactSalesOrder' AS table_name, COUNT(*) AS rows_cnt FROM dbo.FactSalesOrder
ORDER BY table_name;