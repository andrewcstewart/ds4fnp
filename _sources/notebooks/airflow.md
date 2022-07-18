# Airflow

[Apache Airflow](https://airflow.apache.org/) is a great open-source orchestration engine for your data engineering needs.  

Airflow is actually the default native [orchestration engine for Meltano](https://hub.meltano.com/orchestrators/airflow).

There are many ways to host your own Airflow instance.  [Astronomer.io](https://www.astronomer.io/) is an excellent commercial offering, with reasonable pricing model that can scale with your computational needs.  For most projects you only need Airflow to perform very light weight computation, with most heavy work being remotely executed elsewhere.