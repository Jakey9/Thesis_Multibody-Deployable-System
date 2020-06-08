import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#loading data
data_path = 'CSV/YConnectorDataset.csv'
df = pd.read_csv(data_path)

#Changing pandas dataframe to numpy array
target = df.iloc[:,0:1].values
features = df.iloc[:,1:6].values

#split dataframe into training and testing dataset
xTrain, xTest, yTrain, yTest = train_test_split(features, target, test_size = 0.2, shuffle= True, random_state = 28)
#print(xTrain)

#neural network
def get_compiled_model():
      model = tf.keras.Sequential([
        tf.keras.layers.Dense(20, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(2)
      ])

      model.compile(optimizer='adam',
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                    metrics=['accuracy'])
      return model

#run neural networkS
model = get_compiled_model()
history = model.fit(xTrain, yTrain, epochs=10, batch_size=10)


test_loss, test_accuracy = model.evaluate(xTest, yTest)
print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))


model.save('yconnectorpredict_model.h5py')


#loading data for predicting
Predictdata_path = 'CSV/YConnectorTestData.csv'
pdf = pd.read_csv(Predictdata_path)
Predict_data = pdf.iloc[:,1:6].values

predictions = model.predict(Predict_data)
output = []
for item in predictions:
    output.append(np.argmax(item))
#predictions = np.argmax(predictions)
print(output)

