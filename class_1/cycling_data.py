import pandas as pd
import numpy as np

step_data = [3620,7891,9761,3907,4338,5373]

#cycling distance
cycling_data = [10.7,0,None,2.4,15.3,10.9,0,None]
#created a tuple of data
joined_data = list(zip(step_data,cycling_data))
#The data frame
activity_df=pd.DataFrame(joined_data,index=pd.date_range('20150329'),periods=6),columns=['Walking','Cycling'])

print(activity_df)
