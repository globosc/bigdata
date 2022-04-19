import pyspark.sql.functions as F
from pyspark.sql.functions import when, sum, avg, col
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from pyspark.sql.functions import col,desc
from pyspark.sql.types import IntegerType
from pyspark.sql.window import Window



conf = SparkConf().setAppName("test-magister")
sc = SparkContext(conf=conf)
hiveCtx = HiveContext(sc)
df = hiveCtx.sql("select * from mentions4")
#columnas = df.select('mentionsourcename', 'confidence')
#columnas.filter(df['confidence'] < 40).groupBy().avg('confidence')
columnas = df.groupby('mentionsourcename').avg('confidence')
columnas2 = columnas.where(columnas['avg(confidence)'] < 40)
#columnas2 = columnas.filter(columnas.avg(['confidence']) < 40)
#columnas2 = columnas.filter(columnas["confidence"] < 40)
columnas2.show()
