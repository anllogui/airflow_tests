```
conda create -n airflow_tests python=3.10
conda activate airflow_tests

pip install apache-airflow
airflow db init
airflow users create --username admin --firstname angel --lastname llogui --role Admin --email anllogui@gmail.com
airflow webserver -p 8080

```