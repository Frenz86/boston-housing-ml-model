# import the boston dataset 
from sklearn.datasets import load_boston

# unleash pandas and the rest of the gang as well! 
import pandas as pd
import numpy as np



# load the data 
data = load_boston()

# load the data into a dataframe
df = pd.DataFrame(data['data'], columns=data['feature_names'].tolist())

df['label'] = data['target']

# sample the dataframe
sample = df.head()

# print it out in the terminal 
print(sample)

# shuffle the data 
shuffled_df = df.sample(frac=1)

# split the data 
split = 

