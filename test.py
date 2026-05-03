from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("test").getOrCreate()
df=spark.createDataFrame([(1,"Himadri"),(2,"data")],["id","name"])
df.show()