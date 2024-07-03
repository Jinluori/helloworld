import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('D:/spider/ftx_xian1.csv')
df.info()
len(df.titie.unique())