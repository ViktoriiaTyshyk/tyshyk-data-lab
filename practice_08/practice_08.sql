--Завдання 1 
SELECT country, COUNT(*) AS user_count
FROM `bigquery-public-data.thelook_ecommerce.users` 
GROUP BY country 
ORDER BY user_count DESC
LIMIT 10;

--Завдання 2
SELECT category, COUNT(*) AS items_sold, ROUND(SUM(sale_price), 2) AS revenue
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS o
INNER JOIN `bigquery-public-data.thelook_ecommerce.products` AS p 
ON o.product_id=p.id
GROUP BY category
ORDER BY revenue DESC;

--Завдання 3
SELECT status, COUNT(*) AS orders_count
FROM `bigquery-public-data.thelook_ecommerce.orders`
WHERE status IN ("Complete", "Shipped")
GROUP BY status;

--Завдання 4
SELECT FORMAT_DATE('%Y-%m', DATE(created_at)) AS month, COUNT(*) AS items_sold, ROUND(AVG(sale_price), 2) AS avg_price
FROM `bigquery-public-data.thelook_ecommerce.order_items`
WHERE EXTRACT(YEAR FROM created_at) IN (2024, 2025)
GROUP BY month
ORDER BY month;

--Завдання 5
SELECT category, ROUND(SUM(sale_price), 2) AS revenue
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS o
INNER JOIN `bigquery-public-data.thelook_ecommerce.products` AS p 
ON o.product_id=p.id
GROUP BY category
HAVING revenue>100000
ORDER BY revenue DESC;

--Завдання 6
SELECT p.name AS product_name, p.brand, COUNT(*) AS times_sold, ROUND(SUM(sale_price), 2) AS revenue
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS o
INNER JOIN `bigquery-public-data.thelook_ecommerce.products` AS p 
ON o.product_id=p.id
GROUP BY p.name, p.brand
ORDER BY revenue DESC
LIMIT 10;

--Завдання 7
SELECT p.category, COUNT(*) AS total_items, COUNTIF(returned_at IS NOT NULL) AS returned_items, ROUND(COUNTIF(returned_at IS NOT NULL)/COUNT(*)*100, 1) AS return_rate_pct
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS o
INNER JOIN `bigquery-public-data.thelook_ecommerce.products` AS p 
ON o.product_id=p.id
GROUP BY p.category
ORDER BY return_rate_pct DESC;

--Завдання 8
WITH buyers_data AS (
  SELECT p.category, o.user_id, u.age
  FROM `bigquery-public-data.thelook_ecommerce.order_items` AS o
  JOIN `bigquery-public-data.thelook_ecommerce.products` AS p
  ON o.product_id = p.id
  JOIN `bigquery-public-data.thelook_ecommerce.users` AS u
  ON o.user_id=u.id
)
SELECT category, COUNT(DISTINCT(user_id)) AS buyers, ROUND(AVG(age), 2) AS avg_age
FROM buyers_data
GROUP BY category
ORDER BY avg_age DESC;

--Завдання 9
SELECT FORMAT_DATE('%Y-%m', DATE(created_at)) AS month, ROUND(SUM(sale_price), 2) AS revenue, RANK() OVER (ORDER BY SUM(sale_price) DESC) AS revenue_rank
FROM `bigquery-public-data.thelook_ecommerce.order_items` 
WHERE EXTRACT(YEAR FROM created_at)=2025
GROUP BY month
ORDER BY revenue_rank;

--Завдання 10
WITH month_revenue AS (
  SELECT FORMAT_DATE('%Y-%m', DATE(created_at)) AS month, SUM(sale_price) AS revenue
  FROM `bigquery-public-data.thelook_ecommerce.order_items` 
  WHERE EXTRACT(YEAR FROM created_at)=2025
  GROUP BY month
)
SELECT month, revenue, ROUND(LAG(revenue) OVER (ORDER BY month), 2) AS prev_month_revenue, ROUND((revenue-LAG(revenue) OVER (ORDER BY month))/LAG(revenue) OVER (ORDER BY month)*100, 1) AS growth_pct
FROM month_revenue
ORDER BY month;

--Завдання 11
SELECT p.category, p.name AS product_name, ROUND(SUM(o.sale_price), 2) AS revenue, ROW_NUMBER() OVER (PARTITION BY p.category ORDER BY SUM(o.sale_price) DESC) AS rank_in_category
FROM `bigquery-public-data.thelook_ecommerce.order_items` AS o
INNER JOIN `bigquery-public-data.thelook_ecommerce.products` AS p 
ON o.product_id=p.id
GROUP BY p.category, product_name
QUALIFY rank_in_category <= 3
ORDER BY p.category, rank_in_category;

