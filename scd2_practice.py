# databricks notebook source
from pyspark.sql.functions import current_date, lit, col, to_date
from pyspark.sql.functions import sha2, concat_ws

# set up access key for Azure Data Lake
spark.conf.set("fs.azure.account.key.formula1dl2025pro.dfs.core.windows.net", "40wTqDrI1SrXYZ4ZmQnlF6I2CcmoMiye21CqzUrpaiFW0Oj1UtePNjGtFHh9hqMa8c1H5fYPo7PF+AStDyxCCQ==")

# read data
df_owners = spark.read.csv("abfss://demo@formula1dl2025pro.dfs.core.windows.net/owners.csv",header=True,inferSchema=True)

df_pets = spark.read.json("abfss://demo@formula1dl2025pro.dfs.core.windows.net/pet.json")

# remove null values and unneccessary columns
df_pets = df_pets.drop("_corrupt_record")
df_pets = df_pets.na.drop()

# join owner and pet data
df_joined = df_owners.join(df_pets, on="owner_id", how="inner")

# select and rename columns 
df_joined = df_joined.withColumnRenamed("age","pet_age")
df_joined = df_joined.select("owner_id","owner_name","pet_name","pet_type","pet_age","city")

# add SCD Type 2 metadata columns
df_joined = df_joined \
    .withColumn("start_date", to_date(lit("2019-01-01"), "yyyy-MM-dd")) \
    .withColumn("end_date", lit(None).cast("date")) \
    .withColumn("is_current", lit("Y"))

# write initial combined dataset as Delta table
df_joined.write.format("delta").mode("overwrite").saveAsTable("pets_owners_combined")

# read new data
df_updated_owners = spark.read.csv("abfss://demo@formula1dl2025pro.dfs.core.windows.net/updated_owners.csv",header=True,inferSchema=True)

df_updated_pets = spark.read.json("abfss://demo@formula1dl2025pro.dfs.core.windows.net/updated_pets.json")

# remove null values and unneccessary columns of new data
df_updated_pets = df_updated_pets.drop("_corrupt_record") 
df_updated_pets = df_updated_pets.na.drop()

# join owner and pet data 
df_source = df_updated_owners.join(df_updated_pets, on="owner_id", how="inner")
df_source = df_source.withColumnRenamed("age","pet_age")
df_source = df_source.select("owner_id","owner_name","pet_name","pet_type","pet_age","city")

# add SCD Type 2 metadata columns
df_source = df_source \
    .withColumn("start_date", current_date()) \
    .withColumn("end_date", lit(None).cast("date"))

# COMMAND ----------

# fetch old data from existing Delta table
df_old = spark.table("pets_owners_combined")
df_new = df_source

# join to compare old and new records by hash
joined_df = df_new.alias("new").join(
    df_old.alias("old"),
    on="owner_id",
    how="left"
)

columns_to_track = ["owner_id", "owner_name", "pet_name","pet_type", "pet_age", "city"]

# generate hashes for change detection
joined_df = joined_df.withColumn(
    "hash_new", sha2(concat_ws("||", *[col(f"new.{c}") for c in columns_to_track]), 256)
).withColumn(
    "hash_old", sha2(concat_ws("||", *[col(f"old.{c}") for c in columns_to_track]), 256)
)

# identify new/changed records
changed_new = joined_df.filter(
    (col("hash_old").isNull()) | (col("hash_new") != col("hash_old"))
)

# prepare new records for insert

new_records = changed_new.select([col(f"new.{c}").alias(c) for c in columns_to_track])

new_records = new_records.withColumn("start_date", current_date()).withColumn("end_date", lit(None).cast("date")).withColumn("is_current", lit("Y"))


# expire old matching records (SCD2 logic)
expired_records = df_old.join(
    new_records.select("owner_id").distinct(),
    on="owner_id",
    how="inner"
).filter(col("is_current") == "Y") \
 .withColumn("end_date", current_date()) \
 .withColumn("is_current", lit("N"))

# keep unchanged records as is_current = Y
unchanged_records = df_old.join(
    new_records.select(new_records.owner_id),
    on="owner_id",  # clear and safe
    how="left_anti"
).filter("is_current = 'Y'")

# final union of new, unchanged, and expired records
final_df = unchanged_records.unionByName(expired_records, allowMissingColumns=True).unionByName(new_records, allowMissingColumns=True)
final_df = final_df.sort("owner_id")

# save back to Delta table
final_df.write.format("delta").mode("overwrite").saveAsTable("pets_owners_combined")


# COMMAND ----------

# MAGIC %sql
# MAGIC select * from pets_owners_combined
