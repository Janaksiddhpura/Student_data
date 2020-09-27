#Checking for the Empty set in dataset
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mp

r=pd.read_csv('e:/p/Student_original.csv')

print(r.shape)

df=r.isnull().sum()
print(df)
