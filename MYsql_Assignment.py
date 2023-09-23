#!/usr/bin/env python
# coding: utf-8

# Ans 1 : A **database** is an organized collection of structured information, or data, typically stored electronically in a computer system¹²⁴. A database is usually controlled by a database management system (DBMS). The data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and data querying efficient.
# 
# **SQL** (Structured Query Language) and **NoSQL** (Not only SQL) are two types of database systems that have some key differences:
# 
# 1. **Type of Database**: SQL databases are primarily called Relational Databases (RDBMS); whereas NoSQL databases are primarily called non-relational or distributed databases.
# 
# 2. **Schema**: SQL databases have fixed or static or predefined schema. NoSQL databases have dynamic schema.
# 
# 3. **Data Storage**: SQL databases display data in form of tables so it is known as table-based database. NoSQL databases display data as collection of key-value pair, documents, graph databases or wide-column stores.
# 
# 4. **Scalability**: SQL databases are vertically scalable, which means that you can increase the load on a single server by increasing things like RAM, CPU, or SSD. NoSQL databases are horizontally scalable, which means that you handle more traffic by sharding, or adding more servers in your NoSQL database.
# 
# 5. **Language**: SQL databases use a powerful language "Structured Query Language" to define and manipulate the data. In NoSQL databases, collection of documents are used to query the data.
# 
# 6. **Transactions**: SQL databases are best suited for complex queries and multi-row transactions. NoSQL databases are better for unstructured data like documents or JSON.
# 
# 7. **ACID vs CAP**: SQL databases follow ACID properties (Atomicity, Consistency, Isolation, and Durability) whereas the NoSQL database follows the Brewers CAP theorem (Consistency, Availability, and Partition tolerance).
# 
Ans 2 : **DDL**, or **Data Definition Language**, is a type of SQL command that is used to define the database schema¹⁴. It deals with descriptions of the database schema and is used to create and modify the structure of database objects in the database¹⁴. DDL includes commands like CREATE, DROP, ALTER, and TRUNCATE¹⁴.

1. **CREATE**: The `CREATE` command is used to create a new table in a database⁶⁷. For example, the following SQL creates a table called "Persons" that contains five columns: PersonID, LastName, FirstName, Address, and City⁶⁷:
    ```sql
    CREATE TABLE Persons (
        PersonID int,
        LastName varchar(255),
        FirstName varchar(255),
        Address varchar(255),
        City varchar(255)
    );
    ```

2. **DROP**: The `DROP` command is used to delete an existing table from the database⁸[^10^]. For example, the following SQL deletes the table "Shippers"⁸:
    ```sql
    DROP TABLE Shippers;
    ```

3. **ALTER**: The `ALTER` command is used to modify the structure of an existing table¹²¹³. It can be used to add, delete, or modify columns in an existing table¹²¹³. For example, the following SQL adds a column named "phone" to the "Customers" table¹²:
    ```sql
    ALTER TABLE Customers ADD phone varchar(10);
    ```

4. **TRUNCATE**: The `TRUNCATE` command is used to delete all rows from a table but keeps the structure unchangeable¹⁶¹⁷. It makes entries about it in a transaction log[^20^]. For example, the following SQL truncates the table "Categories"¹⁷:
    ```sql
    TRUNCATE TABLE Categories;Ans 3 : **DML**, or **Data Manipulation Language**, is a subset of SQL commands used for manipulating data within objects of a relational database¹²³⁴. DML includes commands like INSERT, UPDATE, and DELETE¹²³⁴.

1. **INSERT**: The `INSERT` command is used to insert new rows in a database table⁵. For example, the following SQL inserts a new row into the "Customers" table:
    ```sql
    INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) 
    VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
    ```
   This command inserts a new customer named 'Cardinal' into the "Customers" table.

2. **UPDATE**: The `UPDATE` command is used to modify existing records in a table⁹. For example, the following SQL updates the "Customers" table⁹:
    ```sql
    UPDATE Customers 
    SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' 
    WHERE CustomerID = 1;
    ```
   This command updates the contact name and city of the customer with CustomerID 1.

3. **DELETE**: The `DELETE` command is used to delete existing records from a table¹³. For example, the following SQL deletes a customer from the "Customers" table¹³:
    ```sql
    DELETE FROM Customers 
    WHERE CustomerName='Alfreds Futterkiste';
    ```
   This command deletes the customer named 'Alfreds Futterkiste' from the "Customers" table.

These commands are fundamental for managing and manipulating data within databases.Ans 4 : **DQL**, or **Data Query Language**, is a type of SQL command that is used to query or retrieve data from a database¹²³⁴. DQL includes the `SELECT` statement, as well as a variety of operators and functions that can be used to manipulate the retrieved data.

The `SELECT` statement is used to select data from a database⁵⁶. The data returned is stored in a result table, also called the result set. Here's an example:

```sql
SELECT CustomerName, City FROM Customers;
```

In this example, the `SELECT` statement retrieves data from the "Customers" table. Specifically, it retrieves the "CustomerName" and "City" for each record in the table. The result is a table of customer names and cities.

You can also use the `SELECT *` syntax to select all columns from a table. For example:

```sql
SELECT * FROM Customers;
```Ans 5 :  The two important concepts in database systems:

1. **Primary Key**: A primary key is a specific choice of a minimal set of attributes (columns) that uniquely specify a tuple (row) in a relation (table). In the world of databases, the primary key of a relational table uniquely identifies each record in the table¹. Databases use keys to compare, sort, and store records, and to create relationships between records. It can be a normal attribute that is guaranteed to be unique such as Social Security number on a table with no more than one record per person or — preferably — it can be generated by the database management system such as a globally unique identifier, or GUID, in Microsoft SQL Server. Primary keys may consist of a single attribute or multiple attributes in combination.

2. **Foreign Key**: A foreign key is a column or group of columns in a relational database table that provides a link between data in two tables. It acts as a cross-reference between tables because it references the primary key of another table, thereby establishing a link between them. The existence of a foreign key column establishes a foreign key constraint – a database rule that ensures that a value can be added or updated in column_a only if the same value already exists in column_b.

These keys are fundamental to understanding relational databases and are crucial for designing safe and efficient database systems.
# In[2]:


pip install mysql


# import mysql.connector
# 
# # Establish the connection
# cnx = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword",
#     database="yourdatabase"
# )
# 
# # Create a cursor object
# cursor = cnx.cursor()
# 
# # Close the connection
# cnx.close()
# 
# The cursor method of a connection object is used to create a new cursor object3. Cursors are what we use to execute SQL commands and fetch data from a MySQL database4.
# 
# The execute method of the cursor object is used to execute SQL queries5. For example, if you want to fetch all records from a table named “Customers”, 

# Ans 7 : The order of execution of SQL clauses in an SQL query is as follows:
# 
# 1. `FROM` clause (including joins: INNER JOIN, LEFT JOIN, RIGHT JOIN, OUTER JOIN, CROSS JOIN, etc.)
# 2. `ON` clause
# 3. `OUTER` clause
# 4. `WHERE` clause
# 5. `GROUP BY` clause
# 6. `HAVING` clause
# 7. `SELECT` clause
# 8. `DISTINCT` clause
# 9. `ORDER BY` clause
# 10. `TOP` clause
# 
# It's important to note that this is the logical order of execution, not the order in which you write the clauses in your SQL statement¹². Also, if your query includes sub-queries or Common Table Expressions (CTE), these will always be executed first before any action takes place on the main query¹.
# 

# In[ ]:




