#Students who viewed announcement in comparison to their class of performance
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mp
r=pd.read_csv('S:\Marwadi college\sem-4\Project\s1.csv')

anc=sns.boxplot(x='Class',y='AnnouncementsView',data=r)
mp.show()
