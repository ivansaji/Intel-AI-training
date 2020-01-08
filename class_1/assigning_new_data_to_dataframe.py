import pandas as pd
import numpy as np

filepath = '/home/ivan/study stuff/Intel/Intel-ML101_Class1/data/Iris_Data.csv'

data = pd.read_csv(filepath)
data['sepal_area'] = data.sepal_length*data.sepal_width

print(data.iloc[:5, -3:])