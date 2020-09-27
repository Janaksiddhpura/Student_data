import pandas as pd
from collections import Counter
r=pd.read_csv("S:\Marwadi college\sem-4\Project\s1.csv")
j=r["gender"].value_counts()
l=dict(j)
s=""
for i in l.keys():
s=s+i+"   "
print("There are ",len(l)," Types of gender available in dataset::",s)


