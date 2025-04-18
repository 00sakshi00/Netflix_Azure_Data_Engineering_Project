# Databricks notebook source
var = dbutils.jobs.taskValues.get(taskKey="Weekdaylookup",key="weekOutput")

# COMMAND ----------

print(var)