# 🗄️ Supermart Airflow, dbt & Databricks Lakehouse Pipeline

Welcome to the Supermart Airflow, dbt & Databricks Lakehouse Pipeline repository! 🚀

This project presents a comprehensive, end-to-end data lakehouse solution engineered to ingest, transform, and model high-volume retail datasets. Covering the complete data lifecycle—from raw data extraction out of PostgreSQL (utilizing Ghost DB database backends) and landing zones, through robust PySpark and modular dbt transformations, to automated orchestration via Apache Airflow—this project demonstrates modern data engineering best practices in cloud lakehouse architecture, data modeling, and workflow automation.



## 📌 Project Overview
The **Supermart Airflow, dbt & Databricks Lakehouse Pipeline** simulates a real-world enterprise data engineering workflow. Modern organizations face challenges handling siloed, raw operational data across relational databases and cloud environments. This project solves that problem by building a fully automated, end-to-end data platform that moves raw data from relational sources through robust processing tiers, ensuring high data quality, seamless orchestration, and lightning-fast analytics.

This project involves:
1. **Data Architecture:** Designing a modern cloud data lakehouse using a 3-tier Medallion Architecture (Bronze, Silver, and Gold layers).
2. **ETL Pipelines:** Extracting raw data from PostgreSQL (Ghost DB) source instances, transforming via PySpark and dbt, and loading into structured targets.
3. **Workflow Orchestration:** Automating, scheduling, and managing pipeline dependencies using Apache Airflow TaskFlow workflows.
4. **Data Modeling & Analytics:** Developing optimized star-schema dimensional models and modular data models for high-performance analytics.

🎯 This repository is an excellent resource for professionals and students looking to showcase expertise in:
- Data Engineering
- Cloud Data Lakehouse
- Apache Airflow
- Databricks & PySpark
- dbt (Data Build Tool)
- PostgreSQL / Ghost DB
