"""
PostgreSQL

ORDBMS(object relational database management system)
Open-source descendant of the original Berkeley code
Cross platform
Companies using PostgreSQL:
-Netflix
-Spotify
-Instagram
-Reddit

PostgreSQL stand out:
First DBMS that implements multi-version concurrency control feature
Able to add custom functions
Designed to be extensible
Defining custom data types, plugins, ext.\
Very active community


Retrieving Data (Using SQL SELECT)

Projection
Take a subset of the columns
_   _
_   _
_   _

Selection
Take a subset of the rows
_ _ _ _ _
_ _ _ _ _

Join
Combine tables be some column


SELECT - EXAMPLES

SELECT * FROM employees: ----> Table name
       |
(List of columns(* - for all))


Concatenation

You can concatenate column names or string using the concat() function
concat() - returns the string that results from concatenating the arguments
String literals are enclosed in [''](single quotes)
Table and column names containing special symbols use [`]

SELECT concat(`first_name`', `last_name`) AS
    'full_name', `job_title` as 'Job Title', `id` AS 'No.'
        FROM `employees`;

Another function of concatenation is concat_ws() - stand for concatenate with separator and is a special form
of CONCAT().

SELECT concat_ws(' ', `first_name`, `last_name`, `job_title`)
    AS 'full_name', `job_title` AS 'Job Title', `id` AS 'No.'
    FROM `employees`;

Skip any NULL values after the separator argument.


Filtering the Selected Rows

Use DISTINCT to eliminate duplicate results

SELECT DISTINCT `department_id` FROM `employees`;

You can filter rows by specific conditions using the WHERE clause

SELECT `last_name`, `department_id` FROM `employees`
WHERE `department_id` = 1;

Other logical operators can be used for better control

SELECT `last_name`, `salary`
FROM 'employees` WHERE `salary` <= 20000;



Other Comparison Conditions

Conditions can be combined using NOT, OR, AND and brackets

SELECT `last_name` FROM `employees`
WHERE NOT (`manager_id` = 3 OR `manager_id` = 4);

Using BETWEEN operator to specify a range:

SELECT `last_name`, `salary` FROM `employees`
WHERE `salary` BETWEEN 20000 AND 22000;

Using IN / NOT IN to specify a set of values:

SELECT `first_name`, `last_name`, `manager_id`
FROM `employees`,
WHERE `manager_id` IN (109, 3, 16);


Comparing with NULL

NULL is a special value that means missing value
-Not the same as 0 or a blank space
Checking for NULL values


SELECT `last_name`, manager_id`
FORM `employees`                   ------> This is always false
WHERE `manager_id` = NULL;

SELECT `last_name`, `manager_id`
FROM `employees`
WHERE `manager_id` IS_NULL;

SELECT `last_name`, `manager_id`
FROM `employees`
WHERE `manager_id` IS NOT_NULL;


Sorting with ORDER BY

Sort rows with the ORDER_BY clause
-ASC: ascending order, default
-DESC; descending order

SELECT `last_name`, `hire_date`
FROM `employees`
ORDER_BY `hire_date`;

SELECT `last_name`, `hire_date`
FROM `employees`
ORDER_BY `hire_date` DESC;


Views - Example

Get employee names and salaries by department

CREATE VIEW `v_hr_result_set` AS
SELECT CONCAT(`first_name`, ' ', `last_name`) AS 'Full Name', `salary`
FROM `employees` ORDER_BY `department_id`;

SELECT * FROM `v_hr_result_set`;
"""

"""
Writing Data in Tables (Using SQL INSERT)

The SQL INSERT command

INSERT INTO `towns` VALUES (33, 'Paris'); ---> Values for all columns

INSERT INTO projects(`name`, `start_date`) ---> Specify columns
VALUES ('Reflective Jacket', NOW());
 
Bulk data can be recorded in a single query separated by comma

INSERT INTO 'employees_projects' VALUES (229, 1), (229, 2), (229, 3), ....

You can use existing records to create a new table

CREATE TABLE `customer_contacts` ---> New table name
AS SELECT `customer_id`, `first_name`, `email`, 'phone` --> Existing source
FROM `customers`;

Or into an existing table

INSERT INTO projects(name, start_date)
SELECT CONCAT(name, ' ', 'Restructuring'), NOW()
FROM departments;

"""

"""
Modifying Existing Records(Using SQL UPDATE and DELETE)

The SQL UPDATE command

UPDATE `employees`
SET `last_name` = 'Brown' ---> New value
WHERE `employee_id` = 1;

UPDATE `employees`
SET `salary` = `salary` * 1.10, `job_title` = CONCAT('Senior', ' ', `job_title`)
WHERE 'department_id` = 3;

Note: Don't forget the WHERE clause!

Deleting specific rows from a table

DELETE FROM `employees`
WHERE `employee_id` = 1; --> condition

Note: Don't forget WHERE clause!

Delete all rows from a table (TRUNCATE works faster than DELETE)

TRUNCATE TABLE users;
"""

"""
Retrieving Related Data

Table relations are useful when combined with JOINS

With JOINS we can get data from two tables simultaneously

JOINS require at least two tables and a "join condition"

SELECT * FROM table_a ----> Select form table
    JOIN table_b ON table_b_.common_column = table_a.common_column ---> Join Condition
"""

"""
Writing SQL in pgAdmin 4 (Demo)

In pgAdmin left section Browser select folder Servers/PostgreSQL/Databases and right click the hover on Create 
then click Database..
that will show you window (Create - Database)
in General put name on Database section like "psql_exercise" then Save
After that in left Browser select created database Servers/PostgreSQL/Databases/psql_exercise 
and right click then select Query Tool that will show you Query Editor where you can type Sql
Example (Creating a tables):

CRATE TABLE department(
    dep_id INTEGER NOT NULL PRIMARY KEY,
    dep_name VARCHAR (20),
    dep_location VARCHAR (15)
);

CREATE TABLE manager (
    man_id INTEGER NOT NULL PRIMARY KEY,
    man_name VARCHAR(15)
);

CREATE TABLE employees(
    emp_id INTEGER NOT NULL PRIMARY KEY,
    emp_name VARCHAR(15),
    job_name VARCHAR(10),
    manager_id INTEGER,
    hire_date DATE,
    salary DECIMAL(10, 2),
    commission DECIMAL(7, 2),
    dep_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES manager(man_id),
    FOREIGN KEY (dep_id) REFERENCES department(dep_id)
);

In left Browser psql_exercise/Schemas/Tables will see the 3 tables that created

In QUERY Editor can see a table

SELECT * FROM department;

"""