# Data Engineering for a Consulting Firm

## Scenario
You are a data engineer at a data analytics consulting company. Your company prides itself in being able to efficiently handle data in any format on any database on any platform. Analysts in your office need to work with data on different databases, and data in different formats. While these analysts are good at analyzing data, they count on you to be able to move data from external sources into various databases, to be able to move data from one type of database to another, and be able to run basic queries on various databases.

## Objectives
- Import data into a MongoDB database.
- Query data in a MongoDB database.
- Export data from MongoDB.
- Import data into a Cassandra database.
- Query data in a Cassandra database.

## Task 1: Import movies.json into mongodb server into a database named entertainment and a collection named movies.
<img width="392" alt="01-mongo-import" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/6661bf9c-c722-4b8e-b110-27afacee789a">


## Task 2: Write a mongodb query to find the year in which most number of movies were released
<img width="395" alt="02-most-movies-year" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/8672780d-ebd4-49a4-95bf-61a172dec46e">


## Task 3: Write a mongodb query to find the count of movies released after the year 1999
<img width="394" alt="03-movies-count-1999" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/d454df6b-053b-4edc-a578-320f9023f9ce">


## Task 4: Write a query to find out the average votes for movies released in 2007
<img width="392" alt="04-average-votes" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/1ad749ce-c0a3-4923-b6b3-68ee7db8dcd1">


## Task 5: Export the fields _id, title, year, rating and director from the movies collection into a file named partial_data.csv
<img width="572" alt="05-mongo-export" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/cf959323-927e-4077-84ad-74eaad450515">


## Task 6 - Create a keyspace named entertainment
<img width="452" alt="06-describe-keyspaces" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/055379b0-805d-4a39-8fe1-ea0d63ad1356">


## Task 7 - Import partial_data.csv into cassandra server into a keyspace named entertainment and a table named movies
<img width="452" alt="07-movies-imported" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/af77e350-f664-4de0-8584-0270d0522917">


## Task 8 - Write a cql query to count the number of rows in the movies table
<img width="452" alt="08-movies-count" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/f6782b52-97b4-4d38-8fd5-4ad4fa625a17">


## Task 9 - Create an index for the rating column in the movies table using cql
<img width="520" alt="09-movies-rating-index" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/52e1071d-7714-459e-9095-3806a16010a2">


## Task 10 - Write a cql query to count the number of movies that are rated 'G'.
<img width="517" alt="10-g-rated-movies" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/03f0941a-79a9-409c-9321-d5d1fe97ec28">
