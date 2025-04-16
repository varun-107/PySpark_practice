# Databricks notebook source
spark.conf.set("fs.azure.account.key.formula1dl2025pro.dfs.core.windows.net", "40wTqDrI1SrXYZ4ZmQnlF6I2CcmoMiye21CqzUrpaiFW0Oj1UtePNjGtFHh9hqMa8c1H5fYPo7PF+AStDyxCCQ==")

df_owners = spark.read.csv("abfss://demo@formula1dl2025pro.dfs.core.windows.net/owners.csv",header=True,inferSchema=True)

df_pets = spark.read.json("abfss://demo@formula1dl2025pro.dfs.core.windows.net/pet.json")

df_pets = df_pets.drop("_corrupt_record")
df_pets = df_pets.na.drop()
df_Joined = df_owners.join(df_pets, on="owner_id", how="inner")
df_Joined = df_Joined.withColumnRenamed("age","pet_age")
df_Joined = df_Joined.select("owner_id","owner_name","pet_name","pet_type","pet_age","city")
