from pyspark.sql import Row, SparkSession
from random import randint


def main():
    spark = (
        SparkSession.builder.master("local[1]")
        .appName("test-spark-metrics")
        .getOrCreate()
    )
    print(spark.sparkContext._jsc.sc().applicationId())

    for _ in range(3):
        df = spark.createDataFrame(
            [Row(id=randint(100, 10000)) for _ in range(1000000)]
        )
        df = df.repartition(10)
        print(df.groupBy("id").agg({"id": "count"}).head())


if __name__ == "__main__":
    main()
