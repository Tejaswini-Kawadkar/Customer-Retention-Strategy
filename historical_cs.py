from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("ExportHistoricalToS3") \
        .enableHiveSupport() \
        .getOrCreate()
    
    tables = {
        "cases_json": "s3a://bucket1/Historical_Files/case/",
        "surveys_json": "s3a://bucket1/Historical_Files/survey/"
    }
    
    for table, path in tables.items():
        print(f"Exporting {table} to {path} ...")
        df = spark.sql(f"SELECT * FROM {table}")
        df.write.mode("overwrite").parquet(path)
        print(f"Exported {table} successfully.")

    spark.stop()

if __name__ == "__main__":
    main()
