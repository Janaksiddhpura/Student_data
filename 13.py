#Count the student absence days
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mp
r=pd.read_csv('S:\Marwadi college\sem-4\Project\s1.csv')

sns.countplot(x='StudentAbsenceDays',hue='Class',data=r)
mp.show()
