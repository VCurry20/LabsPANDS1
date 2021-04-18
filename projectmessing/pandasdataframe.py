#messing with pandas

import pandas as pd 
import numpy as np 

filename = 'kaggleIrisSet.csv'
df = pd.read_csv(filename)

df.to_csv("Dataprintout.csv")
