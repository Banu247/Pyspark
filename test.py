import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


from pyspark.sql import SparkSession
from pyspark.sql.functions import udf ,col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


#connection to spark
spark = SparkSession.builder.appName("Myapp").getOrCreate()

#creation of structType and structField
schema =StructType([

    StructField("name",StringType(),True),
    StructField("age",IntegerType(),True),

])

data =([

    ("Alice",12),
    ("Bob",42),
    ("john",18),
    ("john",18),
    ("john",18)
])


df =spark.createDataFrame(data, schema)
df.show()
df.printSchema()


# To remove duplications of rows
distintct_df =df.dropDuplicates()
distintct_df.show()


#orderby
df_order =df.orderBy("age")
df_order.show()

#groupby
df.groupBy("name").sum("age").show()


#udf function 


def upper(str):
    new_str=""
    for i in str:
        new_str =new_str+i.upper()
    return new_str

converttoudf = udf(lambda z:upper(z))


df.select(col("age"),\
    converttoudf(col("name")).alias("NAME")).show()