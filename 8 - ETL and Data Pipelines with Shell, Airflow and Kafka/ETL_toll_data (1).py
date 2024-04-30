# import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
    'owner': 'Hawino',
    'start_date': days_ago(0),
    'email': ['hawino@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# define the tasks
# Create a task to unzip data
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xvf /home/project/airflow/dags/finalassignment/tolldata.tgz',
    dag=dag,
)

# Create a task to extract data from csv file
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d "," -f 1-4 /home/project/airflow/dags/finalassignment/\
        vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data',
    dag=dag,
)

# Create a task to extract data from tsv file
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -d $"\t" -f 5-7 /home/project/airflow/dags/finalassignment/\
        tollplaza-data.tsv | tr $"\t" ",">\
        /home/project/airflow/dags/finalassignment/tsv_data.csv',
    dag=dag,
)

# Create a task to extract data from fixed width file
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command='cut -b 59-67 /home/project/airflow/dags/finalassignment/\
        payment-data.txt | tr " " "," > \
        /home/project/airflow/dags/finalassignment/fixed_width_data.csv',
    dag=dag,
)

# Create a task to consolidate data extracted from previous tasks
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command='paste /home/project/airflow/dags/finalassignment/csv_data.csv \
        /home/project/airflow/dags/finalassignment/tsv_data.tsv \
        /home/project/airflow/dags/finalassignment/fixed_width_data.csv \
        > /home/project/airflow/dags/finalassignment/extracted_data.csv',
    dag=dag,
)

# Create a task to Transform and load the data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='awk -F, "{print $1,$2,$3,toupper($4),$5,$6,$7,$8,$9}" \
        /home/project/airflow/dags/finalassignment/extracted_data.csv > \
        /home/project/airflow/dags/finalassignment/transformed_data.csv',
    dag=dag,
)

# task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> \
extract_data_from_fixed_width >> consolidate_data >> transform_data
