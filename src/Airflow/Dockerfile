FROM apache/airflow:2.7.1

USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --user -r /requirements.txt

COPY dags/ /opt/airflow/dags/

ENTRYPOINT [ "bash", "-c", "\
    airflow db upgrade && \
    airflow connections create-default-connections && \
    airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin || echo 'User admin already exists' && \
    airflow scheduler & \
    exec airflow webserver --port 8080 \
"]
