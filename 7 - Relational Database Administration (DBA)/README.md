# Final Assignment - Database Administration

## Scenario 1
You have assumed the role of database administrator for the PostgreSQL server and you will perform the User Management tasks and handle the backup of the databases.\


## Task 1.1 - Find the settings in PostgreSQL
What is the maximum number of connections allowed for the postgres server on theia lab?\
<img width="455" alt="1 1max-connections" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/88d34871-1432-4eb6-a368-086d891a1b13">


## Task 1.2 - Create a User
Create a user named backup_operator.\
<img width="494" alt="1 2create-user" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/fe2795a7-f11f-4dbb-842f-54d318f83314">


## Task 1.3 - Create a Role
Create a role named backup.\
<img width="568" alt="1 3create-role" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/d034f178-4cad-44f7-9bfe-8a5b8443c778">



## Task 1.4 - Grant privileges to the role
Grant the following privileges to the backup role.\
<img width="565" alt="1 4grant-privs-to-role" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/d9392e4b-3e48-46e5-8deb-612f66a5a982">



## Task 1.5 - Grant role to an user
Grant the role backup to backup_operator\
<img width="569" alt="1 5grant-role" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/38f924d6-3211-4f08-8150-1fd30e293aba">



## Task 1.6 - Backup a database on PostgreSQL server
Backup the database tolldata using PGADMIN GUI.
Backup the database tolldata into a file named tolldatabackup.tar, select the backup format as Tar\
<img width="944" alt="1 6backup-database" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/f2382c2e-fab9-4932-a7c4-8a80b7874a82">

# Scenario 2
You have assumed the role of database administrator for the MySQL server and will perform the tasks like configuration check, recovery of data. You will use indexing to improve the database performance. You will identify which storage engines are supported by the server and which table uses which storage engine. Optionally You will also automate backup tasks.

## Task 2.1 - Restore MySQL server using a previous backup
Restore file onto MySQL server. List the tables in the billing database.\
<img width="520" alt="2 1database-restore" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/4feb0bbc-5ce4-485a-aabc-2006b2790bf1">


## Task 2.2 - Find the table data size
Find the data size of the table billdata.\
<img width="742" alt="2 2table-data-size" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/ed86e450-aa76-4b45-9a3e-20ba997e4e1f">


## Task 2.3 - Baseline query performance
Write a query to select all rows with a billedamount > 19999 in table billdata.\
<img width="570" alt="2 3query-base-line" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/08eacf24-17cb-4afd-80fd-9d73d9daef43">



## Task 2.4 - Create an index
Your customer wants to improve the execution time of the query you wrote in Task 2.3. Create an appropriate index to make it run faster.\
<img width="566" alt="2 4index-creation" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/42b9c90a-3056-4008-b1bf-d186fe55efff">



## Task 2.5 - Document the improvement in query performance
Find out if the index has any impact on query performance.Re-run the baseline query of Task 2.3 after creating the index.\
<img width="571" alt="2 5query-indexed" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/a117f74d-0531-44c7-b9b3-ea3d28be08b7">



## Task 2.6 - Find supported storage engines
Run a command to find out if your MySQL server supports the MyISAM storage engine.\
<img width="818" alt="2 6 storage-engines" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/f2f87542-a057-418e-80a5-cc76134633be">



## Task 2.7 - Find the storage engine of a table
Find the storage engine of the table billdata.\
<img width="567" alt="2 7 storage-engine-type" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/83c6b2f0-b3f3-42b4-8b9e-87ff6ecb8ef8">

# Scenario 3
You have been assigned the work to provison a cloud instance of IBM DB2 server and perform the tasks like restoration of data, index creation to improve the query performance. You will create views to make queries easier to write. Optionally You will also connect to the cloud instance of IBM DB2 server and from command line.

## Task 3.1 - Restore the table billing
Use the billing.csv you have downloaded earlier, restore the csv file into a table named billing.\
<img width="939" alt="3 1 restore-table" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/5524258a-4d6a-49aa-a977-30ba487d24a5">


## Task 3.2 - Create a view named basicbilldetailswith the columns customerid, month, billedamount
<img width="894" alt="3 2 create-view" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/8eda8f79-383f-4e0c-9d42-91603d99fa6f">


## Task 3.3 - Baseline query performance
Write a query to find out all the rows with a billing amount of 19929.\
<img width="634" alt="3 3 query-base-line-db2" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/0704d907-0945-4d0c-b64a-5f8260a027b1">



## Task 3.4 - Create an index
Create an index that can make the query in the previous task faster. Name the index as billingamount.\
<img width="625" alt="3 4 index-creation-db2" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/8f07881c-a8cc-4f15-8739-3b987b427574">



## Task 3.5 - Document the improvement in query performance
Find out if the index has any impact on query performance.\
<img width="627" alt="3 5 query-after-index" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/ef75f449-ed3e-4922-a275-e612e2877025">






