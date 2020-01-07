import pandas as pd
import numpy as np

step_data = [3620,7891,9761,3907,4338,5373]
step_counts = pd.Series(step_data,name='steps')
step_counts = step_counts.astype(np.float)
step_counts = step_counts.fillna(0.,inplace=True)
print(step_counts[1:3])