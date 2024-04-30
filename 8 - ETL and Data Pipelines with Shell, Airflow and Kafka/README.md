# Creating ETL Data Pipelines using Apache Airflow

## Scenario 1
You are a data engineer at a data analytics consulting company. You have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with a different IT setup that uses different file formats. Your job is to collect data available in different formats and consolidate it into a single file.

## Objectives
- Extract data from a csv file
- Extract data from a tsv file
- Extract data from a fixed width file
- Transform the data
- Load the transformed data into the staging area

## Task 1.1 - Define DAG arguments
<img width="312" alt="1 1dag_args" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/5b7dd6f5-0892-4200-88a3-51f1f321ef05">


## Task 1.2 - Define the DAG
<img width="311" alt="1 2dag_definition" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/99d7237b-3bba-46d3-b436-f8761541c305">



## Task 1.3 - Create a task to unzip data
<img width="469" alt="1 3unzip_data" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/9d95d09a-e7be-4b52-a535-7df75613734d">


## Task 1.4 - Create a task to extract data from csv file
This task should extract the fields Rowid, Timestamp, Anonymized Vehicle number, and Vehicle type from the vehicle-data.csv file and save them into a file named csv_data.csv.\
<img width="471" alt="1 4csv_data" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/38f44bc3-c768-472b-9e74-113b016824bd">



## Task 1.5 - Create a task to extract data from tsv file
This task should extract the fields Number of axles, Tollplaza id, and Tollplaza code from the tollplaza-data.tsv file and save it into a file named tsv_data.csv.\
<img width="472" alt="1 5extract_data_from_tsv" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/cebe9884-5070-4750-95d7-ce0ae62f14f8">


## Task 1.6 - Create a task to extract data from fixed width file
This task should extract the fields Type of Payment code, and Vehicle Code from the fixed width file payment-data.txt and save it into a file named fixed_width_data.csv.\
<img width="467" alt="1 6extract_data_from_fixed_width" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/6181d103-928d-4114-b510-1e58d8ddc507">



## Task 1.7 - Create a task to consolidate data extracted from previous tasks
This task should create a single csv file named extracted_data.csv by combining data from the following files:
- csv_data.csv
- tsv_data.csv
- fixed_width_data.csv
The final csv file should use the fields in the order given below:\
Rowid, Timestamp, Anonymized Vehicle number, Vehicle type, Number of axles, Tollplaza id, Tollplaza code, Type of Payment code, and Vehicle Code\
<img width="467" alt="1 7consolidate_data" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/3010e6fc-5388-4ed0-bb7c-1bed7708909f">


## Task 1.8 - Transform and load the data
This task should transform the vehicle_type field in extracted_data.csv into capital letters and save it into a file named transformed_data.csv in the staging directory.\
<img width="469" alt="1 8transform" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/ccc81bd7-f9c3-4161-adb4-2498bccbeccd">



## Task 1.9 - Define the task pipeline
<img width="464" alt="1 9task_pipeline" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/4877f528-be1f-4ad3-bf0b-9561c2eea7a1">

## Task 1.10 - Submit the DAG
<img width="568" alt="1 10submit_dag" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/2d11e30b-c363-46c7-8578-bc633a5ac45a">


## Task 1.11 - Unpause the DAG
<img width="570" alt="1 11unpause_dag" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/5528acb1-eb0d-4012-8b87-8eab61a69817">


## Task 1.12 - Monitor the DAG
<img width="944" alt="1 12dag_runs" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/cb875a0c-aceb-4c5a-845d-8801211d8ddc">

# Creating Streaming Data Pipelines using Kafka

## Scenario 2
You are a data engineer at a data analytics consulting company. You have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. As a vehicle passes a toll plaza, the vehicle’s data like vehicle_id,vehicle_type,toll_plaza_id and timestamp are streamed to Kafka. Your job is to create a data pipe line that collects the streaming data and loads it into a database.

## Objectives
- Start a MySQL Database server.
- Create a table to hold the toll data.
- Start the Kafka server.
- Install the Kafka python driver.
- Install the MySQL python driver.
- Create a topic named toll in kafka.
- Download streaming data generator program.
- Customize the generator program to steam to toll topic.
- Download and customise streaming data consumer.
- Customize the consumer program to write into a MySQL database table.
- Verify that streamed data is being collected in the database table.

## Task 2.1 - Start Zookeeper
<img width="574" alt="2 1start_zookeeper" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/2d54b4da-6501-4400-8958-36a044a48496">


## Task 2.2 - Start Kafka server
<img width="575" alt="2 2start_kafka" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/eda974f5-1e80-4585-9103-161a055c00b1">


## Task 2.3 - Create a topic named toll
<img width="572" alt="2 3create_toll_topic" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/f1228c2f-62fd-4009-9a56-07aa2bcbe518">


## Task 2.4 - Download the Toll Traffic Simulator
<img width="520" alt="2 4download_simulator" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/39c459f8-a13c-42c2-b684-f18e04aa8262">


## Task 2.5 - Configure the Toll Traffic Simulator
<img width="476" alt="2 5configure_simulator" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/65c38d05-3e91-46c1-9ec6-18e209a43ac6">


## Task 2.6 - Run the Toll Traffic Simulator
<img width="563" alt="2 6simulator_output" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/0c31b003-40eb-4bf0-a245-f027572694fa">


## Task 2.7 - Configure streaming_data_reader.py
Open the streaming_data_reader.py and modify the following details so that the program can connect to your mysql server.\
<img width="509" alt="2 7streaming_reader_code" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/07ed80d0-ff72-4c7b-b6b3-ec2af58cfc8c">


## Task 2.8 - Run streaming_data_reader.py
<img width="551" alt="2 8data_reader_output" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/a4e77f32-ecca-473b-85df-220ab19922e9">


## Task 2.9 - Health check of the streaming data pipeline.
If you have done all the steps till here correctly, the streaming toll data would get stored in the table livetolldata. List the top 10 rows in the table livetolldata.\
<img width="568" alt="2 9output_rows" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/ff6d9bc3-e76e-4055-8fdc-876e06e84aef">
