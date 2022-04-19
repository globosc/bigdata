from pyspark.sql.functions import when, sum, avg, col
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from pyspark.sql.functions import col,desc
from pyspark.sql.types import IntegerType
from pyspark.sql.window import Window



conf = SparkConf().setAppName("test-magister")
sc = SparkContext(conf=conf)
hiveCtx = HiveContext(sc)
df = hiveCtx.sql("select * from mentions1")
#columnas = df.groupby('mentionsourcename').avg('confidence')
#columnas = df.groupby(('mentionsourcename').
#columnas2 = columnas.where(columnas['avg(confidence)'] < 40)
#columnas3 = columnas2.sort(desc('avg(confidence)'))
#columnas.show()


columnas = df.groupby('mentionsourcename').avg('confidence')
columnas2 = df.groupby('mentionsourcename').count()
resultado = columnas.join(columnas2, columnas.mentionsourcename == columnas2.mentionsourcename)
resultado2 = resultado.where(resultado['avg(confidence)'] < 40).sort(desc('count'))
resultado2.show()
