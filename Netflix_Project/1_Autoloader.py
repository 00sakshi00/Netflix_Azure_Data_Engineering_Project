# Databricks notebook source
# MAGIC %sql
# MAGIC create schema netflix_adb1.net_schema

# COMMAND ----------

checkpoint Incation-"ahfss://silver@netflixdatalakel.dfs.core.windows.net/checkpoint"

# COMMAND ----------

df = spark.readstream.\
    format("cloudFiles")\
        .option("cloudfiles.format", "csv")\
            .option("cloudfiles.schemaLocation", checkpoint location)\
                .load("abfss://raw@netflixdatalakel.dfs.core.windows.net/netflix_titles")

# COMMAND ----------

display (df)

# COMMAND ----------


df.writestream\
    .option("checkpointLocation", checkpoint location)\
        .start("abfs://bronze@netflixdatalase1.dfs.core.windows.net/netflix titles")