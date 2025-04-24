# Databricks notebook source
from pyspark.sql.functions import max

# access key token
spark.conf.set("fs.azure.account.key.formula1dl2025pro.dfs.core.windows.net", "40wTqDrI1SrXYZ4ZmQnlF6I2CcmoMiye21CqzUrpaiFW0Oj1UtePNjGtFHh9hqMa8c1H5fYPo7PF+AStDyxCCQ==")

# read data
df = spark.read.csv("abfss://demo@formula1dl2025pro.dfs.core.windows.net/Untitled.csv",header='True', inferSchema='True')

# sort the table by marks
df_Sorted = df.orderBy("marks")  
df_no_duplicates = df.dropDuplicates(["student_id"])

# finding the maximum marks obtained in each city
df_grouped = df.groupBy("city").agg(max("marks").alias("max_marks"))
