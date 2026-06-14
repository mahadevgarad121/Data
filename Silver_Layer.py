# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *


# COMMAND ----------

# MAGIC %md
# MAGIC #Silver Layer Script

# COMMAND ----------

# MAGIC %md
# MAGIC ####Data access using APP

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.<storage-account>.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.<storage-account>.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.<storage-account>.dfs.core.windows.net", "<application-id>")
spark.conf.set("fs.azure.account.oauth2.client.secret.<storage-account>.dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.<storage-account>.dfs.core.windows.net", "https://login.microsoftonline.com/<directory-id>/oauth2/token")

# COMMAND ----------

# MAGIC %md
# MAGIC ##Data loading

# COMMAND ----------

# MAGIC %md
# MAGIC ### Reading data

# COMMAND ----------

df_cal = spark.read.format("csv")\
.option("header", "true")\
.option("inferSchema", "true")\
.load("abfss://bronze@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Calendar")
df_cal.display()

# COMMAND ----------

df_cus = spark.read.format("csv")\
.option("header", "true")\
.option("inferSchema", "true")\
.load("abfss://bronze@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Customers")
df_cus.display()

# COMMAND ----------

df_procat = spark.read.format("csv")\
.option("header", "true")\
.option("inferSchema", "true")\
.load("abfss://bronze@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Product_Categories")
df_procat.display()

# COMMAND ----------

df_pro = spark.read.format("csv")\
.option("header", "true")\
.option("inferSchema", "true")\
.load("abfss://bronze@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Products")
df_pro.display()

# COMMAND ----------

df_ret = spark.read.format("csv")\
.option("header", "true")\
.option("inferSchema", "true")\
.load("abfss://bronze@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Returns")


# COMMAND ----------

df_ret.display()

# COMMAND ----------

df_sales = spark.read.format("csv")\
.option("header", "true")\
.option("inferSchema", "true")\
.load("abfss://bronze@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Sales_*")
df_sales.display()

# COMMAND ----------

df_terri = spark.read.format("csv")\
.option("header", "true")\
.option("inferSchema", "true")\
.load("abfss://bronze@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Territories")
df_terri.display()

# COMMAND ----------

df_subcat = spark.read.format("csv")\
.option("header", "true")\
.option("inferSchema", "true")\
.load("abfss://bronze@usstoragedatalake.dfs.core.windows.net/Product_Subcategories")
df_subcat.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ##Transformations
# MAGIC

# COMMAND ----------

df_cal=df_cal.withColumn('Month',month(col('Date')))\
    .withColumn('Year',year(col('Date')))
df_cal.display()



# COMMAND ----------

# MAGIC %md
# MAGIC ###Customerdata

# COMMAND ----------

# DBTITLE 1,Cell 19
df_cus.withColumn("FullName",concat(col("FirstName"),lit(" "),col("LastName"))).display()

# COMMAND ----------

df_cus = df_cus.withColumn('fullName',concat_ws('',col('FirstName'),lit(' '),col('LastName')))
df_cus.display()

# COMMAND ----------

df_cus.write.format("parquet").\
    mode("overwrite")\
        .save("abfss://silver@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Customers")

# COMMAND ----------

# MAGIC %md
# MAGIC ###Sub catagories

# COMMAND ----------

df_subcat.display()

# COMMAND ----------

df_subcat.write.format("parquet").\
    mode("overwrite")\
        .save("abfss://silver@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Product_Subcategories")

# COMMAND ----------

# MAGIC %md
# MAGIC ###Products

# COMMAND ----------

df_pro.display()

# COMMAND ----------

df_pro = df_pro.withColumn('ProductSKU',split(col('ProductSKU'),"_")[0])\
    .withColumn('ProductName',split(col('ProductName'),' ')[0])
df_pro.display()

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

df_pro.write.format("parquet").\
    mode("overwrite")\
        .save("abfss://silver@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Products")

# COMMAND ----------

df_ret.display()

# COMMAND ----------

df_ret.write.format("parquet").\
    mode("overwrite")\
        .save("abfss://silver@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Returns")



# COMMAND ----------

# MAGIC %md
# MAGIC ####Territories
# MAGIC

# COMMAND ----------

df_terri.display()

# COMMAND ----------

df_terri.write.format("parquet").\
    mode("overwrite")\
        .save("abfss://silver@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Territories")

# COMMAND ----------

# MAGIC %md
# MAGIC ####Sales

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales = df_sales.withColumn('StockDate',to_timestamp('Stockdate'))

# COMMAND ----------

df_sales = df_sales.withColumn('OrderNumber',regexp_replace(col('OrderNumber'),'S','T'))


# COMMAND ----------

df_sales = df_sales.withColumn('multiply',col('OrderLineItem')*col('OrderQuantity'))

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales.groupBy('OrderDate').agg(count("OrderNumber").alias('Total_order')).display()

# COMMAND ----------

# DBTITLE 1,Cell 43
df_procat.display()

# COMMAND ----------

df_terri.display()

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

df_sales.write.format("parquet").\
    mode("overwrite")\
        .save("abfss://silver@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Sales")

# COMMAND ----------

df_cal.write.format("parquet").\
    mode("overwrite")\
        .save("abfss://silver@usstoragedatalake.dfs.core.windows.net/AdventureWorks_Calendar1")