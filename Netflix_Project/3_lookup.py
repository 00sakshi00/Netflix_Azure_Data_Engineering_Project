# Databricks notebook source
# MAGIC %md
# MAGIC #Array Parameter files

# COMMAND ----------

files = [
    {
        "sourcefolder": "netflix directors", 
        "target folder": "netflix directors"
    },
    { 
        "sourcefolder": "netflix_cast", 
        "targetfolder": "netflix cast"
    },
    { 
        "sourcefolder":"netflix countries",
        "targetfolder": "netflix_countries"
    }
    {
        "sourcefolder": "netflix category",
        "target folder": "netflix_category" 
    }
]

# COMMAND ----------

# MAGIC %md
# MAGIC ##Job Utility to return Array 

# COMMAND ----------

dbutils.jobs.taskValues.set(key="myArray", value=files)