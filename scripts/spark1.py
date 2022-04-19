from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from pyspark.sql.functions import col,desc

conf = SparkConf().setAppName("test-magister")
sc = SparkContext(conf=conf)
hiveCtx = HiveContext(sc)
df = hiveCtx.sql("select * from mentions1")

query= df.filter(df.mentiontimedate.like("%20201006%")).groupBy('mentionsourcename').count().select('mentionsourcename',col('count').alias('cnt')).sort(desc('cnt')).limit(10)
for x in query.collect():
    print(x)
