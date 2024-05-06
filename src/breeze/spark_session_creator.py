import findspark

findspark.init()
from pyspark.sql import SparkSession



class SparkSessionCreator:
    def __init__(self, app_name="breeze", master="local[*]", config=None):
        self.app_name = app_name
        self.master = master
        self.config = config or {}

    def create_spark_session(self):
        if self.master == "local[*]":
            findspark.init()
        spark = SparkSession.builder \
            .appName(self.app_name) \
            .master(self.master)

        for key, value in self.config.items():
            spark = spark.config(key, value)

        return spark.getOrCreate()
