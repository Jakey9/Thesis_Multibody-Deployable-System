import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#loading data
data_path = 'CSV/YConnectorDataset.csv'
df = pd.read_csv(data_path)

#take target out as separate tensor
target = df.pop('LABEL')

#split array into training and testing dataset
xTrain, xTest, yTrain, yTest = train_test_split(df, target, test_size = 0.2, shuffle= True, random_state = 28)

print(xTrain.shape, yTrain.shape)
print(xTest.shape, yTest.shape)

TrainingSet = tf.data.Dataset.from_tensor_slices((xTrain.values, yTrain.values))
TestingSet = tf.data.Dataset.from_tensor_slices((xTest.values, yTest.values))
print(len(TrainingSet))

#see dataframe
#for feat, targ in TestingSet.take(5):
    #print("Features: {}, Target: {}".format(feat, targ))


train_data = TrainingSet.shuffle(len(xTrain)).batch(1)
test_data = TestingSet.shuffle(len(xTest)).batch(1)



#neural network
def get_compiled_model():
      model = tf.keras.Sequential([
        #tf.keras.layers.Flatten(input_shape=(0, 5)),
        #tf.keras.layers.InputLayer(input_shape=(1,5,1)),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1)
      ])

      model.compile(optimizer='adam',
                    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                    metrics=['accuracy'])
      return model

#run neural network
model = get_compiled_model()
model.fit(train_data, epochs=10)


test_loss, test_accuracy = model.evaluate(test_data)
print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))

#model.predict(test_data)
