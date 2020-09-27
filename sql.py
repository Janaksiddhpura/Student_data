import pandas as pd
import pandasql as ps
import pylab as p

df=pd.read_csv("S:\Marwadi college\sem-4\Project/s1.csv")
ans=ps.sqldf("select topic,class from df")
             
p.bar(ans['Class'],ans['Topic'])
p.show()
