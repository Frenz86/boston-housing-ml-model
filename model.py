# import the boston dataset 
from sklearn.datasets import load_boston

# unleash pandas as well! 
import pandas as pd

# load the data 
data = load_boston()

# load the data into a dataframe
df = pd.DataFrame(data['data'], columns=data['feature_names'].tolist())

df['label'] = data['target']

# sample the dataframe
sample = df.head()

# print it out in the terminal 
print(sample)

