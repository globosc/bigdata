from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from pyspark.sql.functions import col,desc

conf = SparkConf().setAppName("test-magister")
sc = SparkContext(conf=conf)
hiveCtx = HiveContext(sc)
df = hiveCtx.sql("select * from mentions3")

query= df.filter(df.mentiontimedate.like("%202011%")).groupBy('globaleventid').count().select('globaleventid',col('count').alias('cnt')).sort(desc('cnt')).limit(10)
for x in query.collect():
    print(x)
