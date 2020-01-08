import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = '/home/ivan/study stuff/Intel/Intel-ML101_Class1/data/Iris_Data.csv'

data = pd.read_csv(filepath)

plt.plot(data.sepal_length,data.sepal_width,ls='',marker='o')
