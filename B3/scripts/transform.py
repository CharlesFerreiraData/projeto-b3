from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Inicializa a sessão Spark [cite: 83]
spark = SparkSession.builder \
    .appName("B3_Medallion_Pipeline") \
    .getOrCreate()

# --- CAMADA SILVER (Trusted) ---
print("Processando Camada Silver...")
# Lê os CSVs da bronze inferindo o esquema [cite: 89]
df_bronze = spark.read.option("header", "true").option("inferSchema", "true").csv("data/bronze/*.csv")

# Tipagem rigorosa e limpeza de datas [cite: 91, 92]
df_silver = df_bronze.withColumn("Close", F.col("Close").cast("double")) \
                     .withColumn("Date", F.col("Date").cast("date"))

# Salva em Parquet para alta performance analítica [cite: 93, 94, 16]
df_silver.write.mode("overwrite").parquet("data/silver/precos_limpos")

# --- CAMADA GOLD (Analytics) ---
print("Processando Camada Gold...")
# Agregação: Média de fechamento diária do mercado [cite: 98, 99]
df_gold = df_silver.groupBy("Date") \
    .agg(F.avg("Close").alias("media_mercado_dia")) \
    .orderBy("Date")

# Salva o produto final pronto para BI [cite: 102]
df_gold.write.mode("overwrite").parquet("data/gold/analise_mercado")
print("Pipeline PySpark finalizado!")