1. Install MySQL connector module
# Use the pip command to install MySQL connector Python.
pip install mysql-connector-python

2. Import MySQL connector module
Import using a import mysql.connector statement so you can use this module’s methods to communicate with the MySQL database.

3. Use the connect() method
Use the connect() method of the MySQL Connector class with the required arguments to connect MySQL. It would return a MySQLConnection object if the connection established successfully

4. Use the cursor() method
Use the cursor() method of a MySQLConnection object to create a cursor object to perform various SQL operations.

5. Use the execute() method
The execute() methods run the SQL query and return the result.

6. Extract result using fetchall()
Use cursor.fetchall() or fetchone() or fetchmany() to read query result.

7. Close cursor and connection objects
use cursor.clsoe() and connection.clsoe() method to close open connections after your work completes
