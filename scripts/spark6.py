from pyspark.sql.functions import when, sum, avg, col
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from pyspark.sql.functions import col,desc
from pyspark.sql.types import IntegerType
from pyspark.sql.window import Window
from pyspark.sql.functions import broadcast	
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test-magister").config("spark.sql.broadcastTimeout", 36000)
conf = SparkConf().setAppName("test-magister")
sc = SparkContext(conf=conf)
hiveCtx = HiveContext(sc)
#df = hiveCtx.sql("select * from mentions4")
df = hiveCtx.sql("select * from exports4")
columnas = df.groupby('Actor2Geo_CountryCode').count()
#columnas2 = df.groupby('mentionsourcename').count()
#resultado = columnas.join(columnas2, columnas.mentionsourcename == columnas2.mentionsourcename).persist()
#resultado2 = resultado.where(resultado['avg(confidence)'] > 80).sort(desc('count'))
#resultado2.show()
#columnas = df.filter(df.actor2geo_countrycode == "US")
columnas.show()
