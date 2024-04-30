# Hands-on Lab: Acquiring and Processing Information on the World's Largest Banks

## Project tasks

Task 1:
Write a function log_progress() to log the progress of the code at different stages in a file code_log.txt. Use the list of log points provided to create log entries as every stage of the code.\
<img width="380" alt="Task_1_log_function" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/1277f496-be3c-454a-8208-f9a135d1d044">


Task 2:
Extract the tabular information from the given URL under the heading 'By market capitalization' and save it to a dataframe.
a. Inspect the webpage and identify the position and pattern of the tabular information in the HTML code\
<img width="957" alt="Task_2a_extract" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/3152c53d-f1a8-4bd8-b333-98d7289f537f">

b. Write the code for a function extract() to perform the required data extraction.\
<img width="519" alt="Task_2b_extract" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/6bd819d9-effa-41e5-9fc5-dd05e7da248d">

c. Execute a function call to extract() to verify the output.\
<img width="345" alt="Task_2c_extract" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/907ca42f-55ae-42ef-aa86-2b813d1b502b">


Task 3:
Transform the dataframe by adding columns for Market Capitalization in GBP, EUR and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
a. Write the code for a function transform() to perform the said task.\
<img width="601" alt="Task_3a_transform" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/0f07f26f-0f64-4036-9b08-88bacc10102c">

b. Execute a function call to transform() and verify the output.
<img width="621" alt="Task_3b_tranform" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/23d203ac-5551-4a5a-9aed-d80116c07d04">


Task 4:
Load the transformed dataframe to an output CSV file. Write a function load_to_csv(), execute a function call and verify the output.\
<img width="630" alt="Task_4_CSV" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/04d7e957-1cf1-485d-b6a3-a9c95d9b3b70">


Task 5:
Load the transformed dataframe to an SQL database server as a table. Write a function load_to_db(), execute a function call and verify the output.\
<img width="468" alt="Task_4_5_save_file" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/b0afea70-135f-4bd1-a81f-b1c111df31d5">


Task 6:
Run queries on the database table. Write a function load_to_db(), execute a given set of queries and verify the output.\
<img width="720" alt="Task_6_SQL" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/ae4b9560-f989-4bf9-9b40-1c59b13fc124">


Task 7:
Verify that the log entries have been completed at all stages by checking the contents of the file code_log.txt.\
<img width="686" alt="Task_7_log_content" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/114408ef-f87f-46c6-8cad-b164342dfe12">
