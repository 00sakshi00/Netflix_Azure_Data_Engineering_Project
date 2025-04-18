# Databricks notebook source
#creating patameter
dbutils.widgets.text("weekday", "7")

# COMMAND ----------

#variable
var int(dbutils.widgets.get("weekday"))
print(type(var))

# COMMAND ----------

dbutils.jobs.taskValues.set(key-"weekOutput", value=var)