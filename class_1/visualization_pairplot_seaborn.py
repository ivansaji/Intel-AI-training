import pandas as pd
import numpy as np
import seaborn as sns

filepath = '/home/ivan/study stuff/Intel/Intel-ML101_Class1/data/Iris_Data.csv'
data = pd.read_csv(filepath)

sns.pairplot(data,hue='species',size=3)