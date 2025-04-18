# Databricks notebook source
#parameters
dbutils.widgets.text("sourcefolder", "netfils directors") 
dbutils.widgets.text("target folder", "netflix directors") 

# COMMAND ----------

# variables
var_src_folder = dbutils.widgets.get("sourcefolder")
var_trg_folder = dbutils.widgets.get("target folder")

display(var_src_folder)
display (var_trg_folder)

# COMMAND ----------

df = spark.read.format("csv")\
    .option("header", "true")\
    .option("InferSchema", "true")\
    .load("abfss://bronze@netflixitatalakel.dfs.core.windows.net/(var_src_folder)")

# COMMAND ----------

df.display()

# COMMAND ----------

df.write.format("Delta")\
    .mode("append")\
        .option("path", "abfss://silver@netflixdatalakel.dfs.core.windows.net/(var trg_folder)")\
            .save()