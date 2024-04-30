# Introduction to Data Warehousing

## Scenario
You are a data engineer hired by a solid waste management company. The company collects and recycles solid waste across major cities in the country of Brazil. The company operates hundreds of trucks of different types to collect and transport solid waste. The company would like to create a data warehouse so that it can create reports like
- total waste collected per year per city
- total waste collected per month per city
- total waste collected per quarter per city
- total waste collected per year per trucktype
- total waste collected per trucktype per city
- total waste collected per trucktype per station per city

## Objectives
- Design a Data Warehouse
- Load data into Data Warehouse
- Write aggregation queries
- Create MQTs
- Create a Dashboard

## Task 1 - Design the dimension table MyDimDate
Write down the fields in the MyDimDate table in any text editor one field per line. The company is looking at a granularity of day. Which means they would like to have the ability to generate the report on yearly, monthly, daily, and weekday basis.\
<img width="232" alt="1-MyDimDate" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/f733d44f-04c1-4b74-9abc-fb028c9e2ff5">



## Task 2 - Design the dimension table MyDimWaste
Write down the fields in the MyDimWaste table in any text editor one field per line.\
<img width="229" alt="2-MyDimWaste" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/0b1a5890-51ad-476b-8307-11953dd606cf">



## Task 3 - Design the dimension table MyDimZone
Write down the fields in the MyDimZone table in any text editor one field per line.\
<img width="232" alt="3-MyDimZone" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/2c6744e0-d2e4-420b-8c0c-8046a0ab861a">



## Task 4 - Design the fact table MyFactTrips
Write down the fields in the MyFactTrips table in any text editor one field per line.\
<img width="230" alt="4-MyFactTrips" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/9c493760-1b5a-43ae-8c98-30027da27ccf">

## Task 5 - Create the dimension table MyDimDate
<img width="506" alt="5-MyDimDate" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/188166fe-3aaa-4f59-aa22-f6e286e6b59a">


## Task 6 - Create the dimension table MyDimWaste
<img width="503" alt="6-MyDimWaste" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/04d3a3e7-f594-4149-8d30-7423d4f454e8">


## Task 7 - Create the dimension table MyDimZone
<img width="508" alt="7-MyDimZone" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/e170068c-b6ee-418c-924c-fd1e38c85074">


## Task 8 - Create the fact table MyFactTrips
<img width="680" alt="8-MyFactTrips" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/e67cade2-429f-42ed-ac05-d4d34ec7bb9b">

## Task 9 - Load data into the dimension table DimDate
<img width="899" alt="9-DimDate" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/d8b4d51d-7b18-45dd-8faa-b4f27bd7a411">


## Task 10 - Load data into the dimension table DimTruck
<img width="890" alt="10-DimTruck" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/fa122ada-5a35-4f19-8892-0742055b9663">


## Task 11 - Load data into the dimension table DimStation
<img width="890" alt="11-DimStation" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/05917556-0b73-4b97-9252-201ef5428d0d">


## Task 12 - Load data into the fact table FactTrips
<img width="907" alt="12-FactTrips" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/ff83c427-918b-4930-b837-f87e236ea806">

## Task 13 - Create a grouping sets query
Create a grouping sets query using the columns stationid, trucktype, total waste collected.
<img width="915" alt="13-groupingsets" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/1a7553a2-b313-415b-bf7b-edbf006e6619">


## Task 14 - Create a rollup query
Create a rollup query using the columns year, city, stationid, and total waste collected.
<img width="914" alt="14-rollup" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/65da5b82-0be4-48f2-9c51-637b9fd02e72">


## Task 15 - Create a cube query
Create a cube query using the columns year, city, stationid, and average waste collected.
<img width="913" alt="15-cube" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/cea1cbfd-1366-463f-9f41-d39f37f2863b">


## Task 16 - Create an MQT
Create an MQT named max_waste_stats using the columns city, stationid, trucktype, and max waste collected.
<img width="912" alt="16-mqt" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/a53fd1ce-7230-49d7-bc5c-e5e13d82366b">


## Task 17 - Create a pie chart in the dashboard
Create a pie chart that shows the waste collected by truck type.
<img width="321" alt="17-pie" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/cfafe0dc-dd7d-4198-993b-0711b3a9129f">


## Task 18 - Create a bar chart in the dashboard
Create a bar chart that shows the waste collected station wise.
<img width="638" alt="18-bar" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/63727681-4b7e-49f6-a771-086652217d80">


## Task 19 - Create a line chart in the dashboard
Create a line chart that shows the waste collected by month wise.
<img width="630" alt="19-line" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/b6b0dcfe-14c9-4bc5-a688-bb94e8216a57">


## Task 20 - Create a pie chart in the dashboard
Create a pie chart that shows the waste collected by city.
<img width="644" alt="20-pie" src="https://github.com/Hawino/IBM-Data-Engineer/assets/160495569/a03b3b19-3f2c-43cd-ba2a-d75180a76016">


