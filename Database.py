"""
Data Management

01/16/2020
David Rivers
Oil Pump (OP147-0623)
1 x 69.90

In data base will be like:
__________________________________________________________________
Order # |    Date    |    Customer  |  Product |    S/N    | Qty |
--------|------------|--------------|----------|-----------|---- |
00315   | 01/16/2020 | David Rivers | Oil Pump | OP147-063 |  1  |
------------------------------------------------------------------


Databases

A database is an organized collection of related information
-It imposes rules on the contained data
-Access to data is usually provided by a database management system(DBMS)
-Relational storage first proposed by Edgar Codd in 1970


RDBMS(Relational Data Base Management System)
Database management
It parses requests from the use and takes the appropriate action
The user doesn't have direct access to the stored data
Data is presented by relations - collection of tables related by common fields
PostgreSQL, SQLite, Oracle and MySQL


Structured Query Language

Programming language designed for managing data in a relational database
Developed at IBM in the early 1970s
To communicate with the Engine we use SQL

Subdivided into several language element
-Queries
-Clauses
-Expressions
-Predicates
-Statements

UPDATE employees SET  salary = salary * 0.1 WHERE job_title = "Cashier";
   |              |                  |                    |
Update clause  Statement        Expression             Predicate


Logically divided in four sections
-Data Definition - describe the structure of out data
-Data Manipulation - store and retrieve data
-Data Control - define who can access the data
-Transaction Control - bundle operations and allow rollback
"""

"""
SQL vs NoSQL

         SQL               |         NoSQL
---------------------------------------------------------
-RDBMS                     | -Non-relational database system
-Predefined Schema         | -Dynamic Schema
-Suited for Complex queries| -Suited for hierarchical data storage
-Vertically scalable       | -Horizontally scalable 


Data Types

INT - stores whole numbers
VARCHAR / NVARCHAR - variable length character
DECIMAL / FLOAT - stores decimal values
DATETIME - store the data and time (example: 1972-11-05 00:00:00.000)
BIT - Boolean data type


Table Relations
(Relational Database Model in Action)

Relationships
Relationships between tables ate based on interconnections PRIMARY KEY/ FOREIGN KEY

id | name | country_id | ----> id | name    |
---|------|------------|       1  |Bulgaria |
1  |Sofia | 1          |       2  |Germany  | 
2  |Varna | 1          |
3  |Berlin| 2          |
4  |Munich| 2          |

The foreign key is an identifier of a record located in another table (usually its primary key)
By using relationships we avoid repeating data in the database
Relationships have multiplicity:
-One-to-many - e.g., mountains/ peaks
-Many-to-many - e.g., student/ course
-One-to-one - e.g., example driver/car

            Relation One-to-one:
          Cars:          |          Drivers
___________________________________________________
car_id | driver_id| ---> | driver_id | driver_name|
1      | 166      |      |  166      |  .....     |
2      | 102      |      |  102      |  .....     |
----------------------------------------------------
Cars:                     |   Drivers: 
car_id = Primary key     |   driver_id = Primary_key
driver_id = Foreign key  |




            Relation Many-to-one:
          Mountains:          |          Peaks
___________________________________________________
mountain_id | driver_id| ---> | peak_id   | mountain_id |
1           | Causasus |      |  61       |  1          |
                              |  66       |  1          |
----------------------------------------------------
Mountains:                    | Peaks:
mountain_id = Primary key     | peak_id = Primary key
                              | mountain_id = Foreign key   
                              
                    
                                  Relation Many-to-many:                                  
          Employees:          |          Projects         employees_projects(Mapping)
______________________________________________________    _________________________    
employees_id | name     | ---> | project_id   | name |    employee_id | project_id
1            | ........ |      |  4           |  ... |    1           | 4
40           | ........ |      |  24          |  ... |    40          | 24
---------------------------------------------------- 



                                             Junction Tables
students:                   classrooms:                            student_classroom(Combination of the 2 ids)
______________________   ______________________________  _____________________________________________________________
student_id  |  name |        classroom_id |  number|        student_id |    classroom_id  |     pk_student_class_room
1           | Petter|        1            | 10     |        1          |    1             |     11
2           | George|        2            | 20     |        2          |    2             |     22
                                                            1          |    2             |     12
-----------------------  ------------------------------  -------------------------------------------------------------
"""

