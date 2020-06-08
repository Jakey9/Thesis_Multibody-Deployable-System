import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np

#load saved model
model = load_model('yconnectorpredict_model.h5py',compile=False)


#loading data for predicting
Predictdata_path = 'CSV/YConnectorTestData.csv'
pdf = pd.read_csv(Predictdata_path)
Predict_data = pdf.iloc[:,1:6].values

predictions = model.predict(Predict_data)
#print(predictions)

output = []
for item in predictions:
    output.append(np.argmax(item))
#predictions = np.argmax(predictions)
print(output)

