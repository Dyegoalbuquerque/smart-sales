from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts import etl_sales

default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

with DAG("sales_dag", schedule_interval="@daily", catchup=False, default_args=default_args, tags=["sales"]) as dag:
    
    run_etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=etl_sales.run_etl
    )

    run_etl_task
