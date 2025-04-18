# Databricks notebook source
from pyspark.sql. functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ##Silver Data Transformation

# COMMAND ----------

df= spark.read.format("delta")\
    .option("header", "true")\
        .load("abfss://bronze@netflixdatalakel.dfs.core.windows.net/netflix_titles") 

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.fillna(("duration minutes": 0, "duration seasons": 1))
df.display()

# COMMAND ----------

df.withColumn("duration minutes", col('duration minutes').cast(IntegerType()))\
    .withColumn("duration_seasons", col('duration_seasons').cast(IntegerType()))

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df=df.withColumn("ShortTtitle", split(col("title"), ":")[0])
df.display()

# COMMAND ----------

df-df.withColumn("rating", split(col("rating"),"-")[0]) df.display()

# COMMAND ----------

df=df.withColumn("type flag", when(col("type") == "TV Show", 1)\
    .when(col("type") == "Movie", 2))\
        .otherwise(0))

# COMMAND ----------

from pyspark.sql.window import Window

# COMMAND ----------

df= df.withColumn("duration ranking", dense_rank().over(window.orderBy(col("duration minutes"))).desc())

# COMMAND ----------

df.display()

# COMMAND ----------

df.createOrReplaceTempView("temp_view")

# COMMAND ----------

# can be viewed outside nb
df.createOrReplaceGlobalTempview("global view")

# COMMAND ----------

display(df)

# COMMAND ----------

df= spark.sql("""select * from temp_view""")
display(df)

# COMMAND ----------

df= spark.sql("""select * from global_temp.temp_view""")
display(df)

# COMMAND ----------

df_vis = df.groupBy("type").agg(count(*).alias("total_count"))
display(df_vis)

# COMMAND ----------

df.write.format("delta")\
    .mode("overwrite")\
        .option("path","abfss://silver@netflixdatalakel.dfs.core.windows.net/netflix_titles")\
            .save()