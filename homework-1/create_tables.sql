-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	title text,
	birth_date DATE,
	notes text
);

CREATE TABLE customers
(
	customer_id VARCHAR(100),
	company_name VARCHAR(100),
	contact_name VARCHAR(100)
);

CREATE TABLE orders
(
	order_id int,
	customer_id VARCHAR(100),
	employee_id int,
	order_date DATE,
	ship_city VARCHAR(50)
);