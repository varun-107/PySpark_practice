# Databricks notebook source
spark.conf.set("fs.azure.account.key.formula1dl2025pro.dfs.core.windows.net", "40wTqDrI1SrXYZ4ZmQnlF6I2CcmoMiye21CqzUrpaiFW0Oj1UtePNjGtFHh9hqMa8c1H5fYPo7PF+AStDyxCCQ==")

# read data from csv and json
df_owners = spark.read.csv("abfss://demo@formula1dl2025pro.dfs.core.windows.net/owners.csv",header=True,inferSchema=True)
df_pets = spark.read.json("abfss://demo@formula1dl2025pro.dfs.core.windows.net/pet.json")

# remove null and unnecessary columns
df_pets = df_pets.drop("_corrupt_record")
df_pets = df_pets.na.drop()

# join pet and owner data
df_joined = df_owners.join(df_pets, on="owner_id", how="inner")
df_joined = df_joined.withColumnRenamed("age","pet_age")
df_joined = df_joined.select("owner_id","owner_name","pet_name","pet_type","pet_age","city")
