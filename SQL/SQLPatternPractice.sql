-- Create DATABASE DataAnalyticsPrep;
-- Go

-- USE DataAnalyticsPrep; 
-- GO

-- CREATE Table Orders(
--     order_id int Primary key,
--     user_id Int,
--     order_date Date,
--     order_status VARCHAR(20)
-- )

-- INSERT INTO orders (order_id, user_id, order_date, order_status) VALUES
-- (101, 1, '2024-01-05', 'completed'),
-- (102, 1, '2024-01-10', 'cancelled'),
-- (103, 2, '2024-01-07', 'completed'),
-- (104, 2, '2024-01-08', 'completed'),
-- (105, 3, '2024-01-15', 'cancelled'),
-- (106, 4, '2024-01-20', 'completed'),
-- (107, 4, '2024-01-25', 'completed'),
-- (108, 4, '2024-01-28', 'completed');

-- select * from dbo.[Orders];

-- count unique users who placed at least one order
-- select count(distinct(user_id)) as total_users from orders;

-- select count(user_id) from orders group by user_id having count(order_id)>=1

-- select count(*) FROM(
--     select user_id
--     from orders group by user_id having count(*)>1
-- )as t;
-- )t; iska output is 3

-- using CTE
-- with cte as 
-- (
--     select user_id, count(*) as total_users 
--     from Orders 
--     group by user_id 
-- )
-- select count(*) from cte where total_users>=3

-- INSERT INTO orders (order_id, user_id, order_date, order_status) VALUES
-- (109, 1, '2024-02-05', 'completed'),
-- (110, 1, '2024-02-18', 'completed'),
-- (111, 3, '2024-02-10', 'completed'),
-- (112, 5, '2024-02-02', 'completed');

-- verifying
-- SELECT * 
-- FROM orders
-- ORDER BY user_id, order_date;

-- Q3. Count users who placed orders in both january and february
-- with cte as (
--     select user_id, count(distinct Month(order_date)) as monthc
--     from orders
--     where month(order_date)in (1,2) 
--     group by user_id
-- )
-- select count(*) from cte where monthc=2

-- SELECT COUNT(*)
-- FROM (
--     SELECT user_id
--     FROM orders
--     GROUP BY user_id
--     HAVING 
--         SUM(CASE WHEN MONTH(order_date) = 1 THEN 1 ELSE 0 END) > 0
--     AND SUM(CASE WHEN MONTH(order_date) = 2 THEN 1 ELSE 0 END) > 0
-- ) t;

-- use DataAnalyticsPrep;
-- GO
--Q4. Count Customer who has placed only one order ever
-- select count(*) from(
--     select user_id from Orders group by user_id having count(*)=1
-- ) as t;

--using CTE

-- with cte as(
--     select user_id, count(*) as totalo from orders group by user_id
-- )
-- select count(*) from cte where totalo=1

-- ALTER TABLE dbo.Orders
-- ADD 
--     order_amount INT,
--     seller_id INT;
-- GO
-- CREATE TABLE dbo.Users (
--     user_id INT PRIMARY KEY,
--     signup_date DATE
-- );

-- SELECT * 
-- FROM INFORMATION_SCHEMA.TABLES
-- WHERE TABLE_NAME = 'Orders';

-- CREATE TABLE dbo.Sellers (
--     seller_id INT PRIMARY KEY,
--     seller_name VARCHAR(50)
-- );

-- CREATE TABLE dbo.Order_Items (
--     order_item_id INT PRIMARY KEY,
--     order_id INT,
--     product_id INT,
--     quantity INT
-- );

-- UPDATE dbo.Orders
-- SET order_amount = CASE order_id
--     WHEN 101 THEN 500
--     WHEN 102 THEN 700
--     WHEN 103 THEN 1200
--     WHEN 104 THEN 800
--     WHEN 105 THEN 400
--     WHEN 106 THEN 20000
--     WHEN 107 THEN 18000
--     WHEN 108 THEN 22000
--     WHEN 109 THEN 15000
--     WHEN 110 THEN 17000
--     WHEN 111 THEN 9000
--     WHEN 112 THEN 3000
-- END,
-- seller_id = CASE 
--     WHEN order_id IN (101,102,103,104) THEN 1
--     WHEN order_id IN (105,106,107) THEN 2
--     ELSE 3
-- END;

-- INSERT INTO dbo.Users VALUES
-- (1, '2023-12-25'),
-- (2, '2024-01-01'),
-- (3, '2024-01-05'),
-- (4, '2024-01-10'),
-- (5, '2024-01-28');

-- INSERT INTO dbo.Sellers VALUES
-- (1, 'Seller A'),
-- (2, 'Seller B'),
-- (3, 'Seller C');

-- INSERT INTO dbo.Order_Items VALUES
-- (1, 106, 1, 1),
-- (2, 106, 2, 1),
-- (3, 106, 3, 1),
-- (4, 106, 4, 1),
-- (5, 106, 5, 1),
-- (6, 106, 6, 1),   -- order 106 has 6 items

-- (7, 107, 1, 1),
-- (8, 107, 2, 1),

-- (9, 108, 1, 1),
-- (10,108, 2, 1),
-- (11,108, 3, 1),
-- (12,108, 4, 1),
-- (13,108, 5, 1),
-- (14,108, 6, 1),
-- (15,108, 7, 1);   -- order 108 has 7 items

-- 

-- Q.5. 