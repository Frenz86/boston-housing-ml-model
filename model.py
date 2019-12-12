# import the scikit learn things 
from sklearn.datasets import load_boston
from sklearn.linear_model import  LinearRegression

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
split = int(len(shuffled_df) * .7)

train_df = shuffled_df[:split]

test_df = shuffled_df[split:]

# stock function for extracting X, Y columns from Dataframe since we are using RM to make the price predictions

def X_and_Y_from_df(df, y_column, X_columns = []):
    X = {}
    for feature in X_columns:
        X[feature] = df[feature].tolist()
    
    y = df[y_column].tolist()
    
    return X, y 

# extract X and y 

X_train, y_train = X_and_Y_from_df(train_df, 'label', ['RM'])

# reshape the extracted data using numpy 

X_train_arr = np.array(X_train['RM'])
X_train_arr = X_train_arr.reshape(X_train_arr.shape[0], 1)

X_test_arr = np.array(X_test['RM'])
X_test_arr = X_test_arr.reshape(X_test.arr.shape[0], 1)

# train the model, yaaayy!!, but first lets instantiate it 
model = LinearRegression()

# then we fit it 
model.fit(X_arr, y_train)

# predict results 
y_pred = model.predict(X_test_arr)





