# This will be replaced with your bucket name after running the `sed` command in the tutorial
BUCKET = "gs://neat-domain-341912-bucket"


from google.cloud import storage
import pandas as pd
import os
import glob
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import re


dataset_path = "https://storage.googleapis.com/io-vertex-codelab/auto-mpg.csv"
df = pd.read_csv(dataset_path, na_values = "?")
df.dropna(inplace= True, axis = 0)

df["brand"] = df["car name"].apply(lambda x: re.search(r'\A\w+' ,x).group(0) )

spell_check = {
        'chevroelt': 'chevrolet',
        'chevy': 'chevrolet',
        'maxda': 'mazda',
        'toyouta': 'toyota',
        'vw': 'volkswagen',
        'vokswagen': 'volkswagen',
        
    }

df["brand"] = df["brand"].replace(spell_check)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df.brand = le.fit_transform(df.brand)


train_y = df["mpg"]
train_x = df.drop(["mpg", "car name"], axis = 1)


X_train, X_test, y_train, y_test = train_test_split(train_x, train_y, test_size=0.3, random_state=1)

from sklearn.preprocessing import RobustScaler, StandardScaler


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# model_lr = LinearRegression()
# model_lr.fit(X_train, y_train)

from sklearn.ensemble import RandomForestRegressor

n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]


from sklearn.model_selection import RandomizedSearchCV

 #Randomized Search CV

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(5, 30, num = 6)]
# max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10, 15, 100]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 5, 10]


# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf}




rf = RandomForestRegressor()

model_rf = RandomizedSearchCV(estimator = rf, param_distributions = random_grid,scoring='neg_mean_squared_error', n_iter = 10, cv = 5, verbose=2, random_state=42, n_jobs = 1)

model_rf.fit(X_train,y_train)

import os
import pickle

artifact_filename_lr = 'model.pkl'

# Save model artifact to local filesystem (doesn't persist)
local_path = artifact_filename_lr
with open(local_path, 'wb') as model_file:
  pickle.dump(model_rf, model_file)

# Upload model artifact to Cloud Storage
model_directory = os.environ['AIP_MODEL_DIR']
storage_path = os.path.join(model_directory, artifact_filename_lr)
blob = storage.blob.Blob.from_string(storage_path, client=storage.Client())
blob.upload_from_filename(local_path)


# artifact_filename_rf = 'model_rf.pkl'

# # Save model artifact to local filesystem (doesn't persist)
# local_path = artifact_filename_rf
# with open(local_path, 'wb') as model_file:
#   pickle.dump(model_rf, model_file)

# # Upload model artifact to Cloud Storage
# model_directory = os.environ['AIP_MODEL_DIR']
# storage_path = os.path.join(model_directory, artifact_filename_rf)
# blob = storage.blob.Blob.from_string(storage_path, client=storage.Client())
# blob.upload_from_filename(local_path)