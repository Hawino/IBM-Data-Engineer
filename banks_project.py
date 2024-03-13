'''Installing Libraries
python3.11 -m pip install pandas
python3.11 -m pip install numpy
python3.11 -m pip install bs4
'''

# Importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 
import re

# Defining known values
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './Largest_banks_data.csv'

# Logging progress
def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the 
    code execution to a log file. Function returns nothing.'''

    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')

# Extracting information
def extract(url, table_attribs):
    ''' The purpose of this function is to extract the required
    information from the website and save it to a dataframe. The
    function returns the dataframe for further processing. '''

    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
          name = col[1].text.strip()
          market_cap = col[2].text.strip()
          market_cap = re.sub('\[\d\]', '', market_cap)
          data_dict = {"Name": name,
                      "MC_USD_Billion": market_cap}
          df1 = pd.DataFrame(data_dict, index=[0])
          df = pd.concat([df,df1], ignore_index=True)
    return df
df = extract(url, table_attribs)

# Transform information
def transform(df):
    ''' This function converts the GDP information from Currency
    format to float value, transforms the information of margin capital from
    USD (Billions) to EUR, GBP, INR (Billions) rounding to 2 decimal places.
    The function returns the transformed dataframe.'''
    #Load exchange_rates
    exchange_rate = pd.read_csv('exchange_rate.csv')
    exchange_rate = exchange_rate.set_index('Currency').to_dict()['Rate']
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]
    return df

test = transform(df)
test
