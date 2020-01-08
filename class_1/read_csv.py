import pandas as pd
import numpy as np

filepath = '/home/ivan/study stuff/Intel/Intel-ML101_Class1/data/Iris_Data.csv'

data = pd.read_csv(filepath)
print(data.iloc[:10])