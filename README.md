# Customer-Retention-Strategy

````markdown
# Customer Retention Strategy - Real-Time & Batch Analytics Pipeline

## Project Overview
This project implements a **Customer Retention Analytics Pipeline** using a Lambda architecture to process CRM data in both **batch** and **real-time**. The pipeline enables ingestion, transformation, and visualization of customer cases and survey data, providing actionable insights into customer behavior and retention metrics.

Key features:
- Batch ingestion from MySQL to Hive tables for static dimensions.
- Real-time ingestion using AWS Kinesis, processed with Spark on EMR.
- Storage in Amazon S3 (historical & dimension data) and Redshift (fact tables).
- ETL automation using Python, Spark, and AWS services.
- KPI reporting and dashboards using Amazon QuickSight.

---

## Architecture & Data Flow
1. **Data Sources**:
   - CRM transactional data stored in MySQL.
   - Case and survey data generated daily (historical & real-time).

2. **Batch Processing**:
   - Hive tables store historical and dimension datasets.
   - Data exported from Hive to S3 as Parquet/CSV files using Spark.
   - S3 data loaded into Redshift for analytics.

3. **Real-Time Processing**:
   - New case and survey events streamed to **AWS Kinesis**.
   - Spark Streaming (on EMR) consumes Kinesis streams.
   - Data written into Redshift fact tables (`case_table` & `survey_table`) with schema validation.

4. **Visualization & Reporting**:
   - Redshift queried to compute KPIs such as:
     - Total cases, open/closed cases, priority cases.
     - Positive/negative survey responses.
     - Daily aggregates for cases and surveys.
   - Dashboards created in **QuickSight** for interactive insights.

---

## Tech Stack
- Data Storage & Warehousing</b>: MySQL, Hive, S3, Redshift
- **Streaming & ETL**: AWS Kinesis, Spark, EMR, Python
- **Orchestration**: Python scripts, Spark jobs
- **Visualization**: Amazon QuickSight
- **File Formats**: JSON, CSV, Parquet

---

## Setup & Execution

### 1. EC2 & MySQL Setup
```bash
sudo yum update -y
sudo yum install -y mysql-community-server
sudo systemctl start mysqld
sudo systemctl enable mysqld
````

* Create database and dimension tables in MySQL.
* Load initial datasets from S3 using `LOAD DATA INFILE`.

### 2. Batch Processing

* Import dimension tables from MySQL to Hive using **Sqoop**.
* Generate historical case/survey data using `generate_historical_data.py`.
* Load data into Hive external tables (`cases_json`, `surveys_json`).
* Export Hive tables to S3 as Parquet/CSV using `s3locate.py` & `historical_cs.py`.

### 3. Real-Time Processing

* Launch EMR cluster with Spark & Hadoop.
* Stream new cases/surveys to **Kinesis** using `stream_to_kinesis.py`.
* Process streams with `kinesis_to_redshift.py` and write to Redshift.

### 4. Redshift Setup

* Create fact and dimension tables in Redshift (`case_table`, `survey_table`, etc.).
* Load historical & dimension data from S3 using `COPY` commands.

### 5. Analytics & KPIs

* Run analytical queries to compute metrics:
  * Total/priority/open/closed cases.
  * Positive/negative survey responses.
  * Daily aggregations.

---

## Folder Structure

```
├── generate_historical_data.py   # Historical data generator
├── stream_to_kinesis.py          # Real-time data generator
├── kinesis_to_redshift.py        # Spark Streaming job
├── s3locate.py                   # Hive-to-S3 export
├── historical_cs.py              # Historical data export
├── SQL                          # Redshift table creation & analytical queries
└── README.md
```

---

## Outcome

* Real-time and batch customer insights available in minutes instead of hours.
* Automated ETL pipelines reduce manual intervention.
* Improved monitoring of customer retention, case handling, and survey responses.

---
