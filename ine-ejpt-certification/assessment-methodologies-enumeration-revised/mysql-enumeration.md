# MySQL  Enumeration

## MySQL Enumeration

* MySQL is an open-source relational database management system based on SQL.
* It is typically used to store records, customer data and is most commonly deployed to store web application data.
* MyQSL utilizes TCP port 3306 by default, however like any service it can be hosted on any open TCP port.

## Auxiliary Modules

* <mark style="color:yellow;">**`auxiliary/scanner/mysql/mysql_version`**</mark>: Retrives the MySQL server version.
* <mark style="color:yellow;">**`auxiliary/scanner/mysql/mysql_login`**</mark>: Attempts to brute force login credentials for MySQL.
* <mark style="color:yellow;">**`auxiliary/admin/mysql/mysql_enum`**</mark>: Enumerates MySQL user privileges, databases, and other information.
* <mark style="color:yellow;">**`auxiliary/admin/mysql/mysql_sql`**</mark>: Executes custom SQL queries on the MySQL server.
* <mark style="color:yellow;">**`auxiliary/scanner/mysql/mysql_file_enum`**</mark>: Enumerates files on the MySQL server using specific file-related functions.
* <mark style="color:yellow;">**`auxiliary/scanner/mysql/mysql_hashdump`**</mark>: Extracts password hashes from the MySQL server.
* <mark style="color:yellow;">**`auxiliary/scanner/mysql/mysql_schemadump`**</mark>: Dumps the schema of the MySQL databases.
* <mark style="color:yellow;">**`auxiliary/scanner/mysql/mysql_writable_dirs`**</mark>: Scans for directories on the MySQL server that are writable.
