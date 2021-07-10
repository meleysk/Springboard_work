from pyspark import SparkContext
from pyspark import SQLContext
from pyspark.sql import Row

sc = SparkContext()
sqlContext = SQLContext(sc)


#How to create a dataframe
# can be created from different data formats(json, csv) , from existing RDD 
# or by programatically specifiying schema

#creating Dataframes from RDDs
l = [('Ankit',25),('Jalfaizy',22),('saurabh',20),('Bala',26)]
rdd = sc.parallelize(l)
people = rdd.map(lambda x: Row(name=x[0], age=int(x[1])))
schemaPeople = sqlContext.createDataFrame(people)
type(schemaPeople)