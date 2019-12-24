import pandas as pd
import numpy as np

step_data = [3620,7891,9761,3907,4338,5373]
step_counts = pd.Series(step_data,name='steps')

step_counts.index = pd.date_range('20191129',periods=6)
#print(step_counts)
#print(step_counts['2019-12-23'])
#print(step_counts[3])
#print(step_counts['2019-12'])
#print(step_counts.dtypes)
step_counts = step_counts.astype(np.float)
print(step_counts.dtypes)

