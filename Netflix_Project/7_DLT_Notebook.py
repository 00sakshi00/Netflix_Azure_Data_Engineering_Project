# Databricks notebook source
# MAGIC %md
# MAGIC #DLT Notebook for gold layer

# COMMAND ----------

looktables_rules={
"rulel":"show_id is NOT NULL"
}

# COMMAND ----------

@dlt.table(
    name="gold_netflixdirectors"
)

@dlt.expect_all_or_drop(looktables_rules)

def myfunc():
    df spark.readStream.format("delta").load("abfss://silver@netflixdatalakel.dfs.core.windows.net/netflix_directors")return df

# COMMAND ----------

@dlt.table(
    name="gold_netflixcast"
)

@dlt.expect_all_or_drop(looktables_rules)

def myfunc():
    df spark.readStream.format("delta").load("abfss://silver@netflixdatalakel.dfs.core.windows.net/netflix_cast")
    return df

# COMMAND ----------

@dlt.table(
    name="gold_netflixcountries"
)

@dlt.expect_all_or_drop(looktables_rules)

def myfunc():
    df spark.readStream.format("delta").load("abfss://silver@netflixdatalakel.dfs.core.windows.net/netflix_countries")
    return df

# COMMAND ----------

@dlt.table(
    name="gold_netflixcategory"
)

@expect_or drop("rules", "show_is is NOT NULL")

def myfunc():
    df=spark.readStream.format("delta").load("abfss://silver@netflixdatalake1.dfs.core.windows.net/netflix_category")return df

# COMMAND ----------

@dlt.table

def gold_stg_netflixtitles():
    df = spark.readstream\
        .format("delta")\
            .load("abfss://silver@net/netflixdatalake1.dfs.core.windows.net/netflix titles)
    return df

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

@dlt.table

def gold_trans_netflixtitles(): 
    df = spark.readstream.table("LIVE.gold_stg_netflixtities")
    df= df.withcolumn("newlfag",lit(1))
    return df

# COMMAND ----------

masterdata_rules={
    "rulel":"newflag is NOT NULL",
    "rule2":"show_id is NOT NULL"
}

# COMMAND ----------

@dlt.table

@dlt.expect_all_or_drop(masterdata_rules)

def gold_netflixtitles():
    df= spark.readStream.table("LIVE.gold_trns_netflixtitles")
    return df