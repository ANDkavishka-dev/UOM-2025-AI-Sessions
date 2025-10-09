%matplotlib inline

import numpy as np                   
import matplotlib.pyplot as plt      
import random                        

from keras.datasets import mnist     
from keras.models import Sequential  

from keras.layers import Dense, Dropout, Activation # Types of layers to be used in our model
import keras.utils as np_utils        
from IPython.display import Image, HTML

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("X_train shape", X_train.shape)
print("y_train shape", y_train.shape)
print("X_test shape", X_test.shape)
print("y_test shape", y_test.shape)

Image('https://i.ibb.co/7CmXmXZ/Training-Data.png')

plt.rcParams['figure.figsize'] = (9,9) # Make the figures a bit bigger

for i in range(9):
    plt.subplot(3,3,i+1)
    num = random.randint(0, len(X_train))
    plt.imshow(X_train[num], cmap='gray', interpolation='none')
    plt.title("Class {}".format(y_train[num]))

plt.tight_layout()

def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")

# now print!
num = random.randint(0, len(X_train))
matprint(X_train[num])



X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)  

X_train = X_train.astype('float32')  
X_test = X_test.astype('float32')

X_train /= 255                       
X_test /= 255

print("Training matrix shape", X_train.shape)
print("Testing matrix shape", X_test.shape)



nb_classes = 10 # number of unique digits

Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()

# The first hidden layer is a set of 512 nodes (artificial neurons).

model.add(Dense(512, input_shape=(784,))) #(784,) is not a typo -- that represents a 784 length vector!

model.add(Activation('relu'))


model.add(Dropout(0.2))


model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))


model.add(Dense(10))

model.add(Activation('softmax'))

# Summarize the built model

model.summary()

# Let's use the Adam optimizer for learning
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

Image('https://i.ibb.co/xfz09bb/Training-Neural-Network.png')

def plot_loss(history):
  plt.plot(history.history['loss'])
  plt.title('Error or Loss')
  plt.xlabel('Number of Iterations')
  plt.ylabel('Error or Loss')
  plt.show()

if __name__ == '__main__':
  history = model.fit(X_train, Y_train,
          batch_size=32, epochs=10,
          verbose=1)
  plot_loss(history)

Image('https://i.ibb.co/D7WDbcr/Training-Model.png')


score = model.evaluate(X_test, Y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# The predict_classes function outputs the highest probability class
# according to the trained classifier for each input example.
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions,axis=1)

# Check which items we got right / wrong
correct_indices = np.nonzero(predicted_classes == y_test)[0]

incorrect_indices = np.nonzero(predicted_classes != y_test)[0]

plt.figure()
for i, correct in enumerate(correct_indices[:9]):
    plt.subplot(3,3,i+1)
    plt.imshow(X_test[correct].reshape(28,28), cmap='gray', interpolation='none')
    plt.title("Predicted {}, Class {}".format(predicted_classes[correct], y_test[correct]))

plt.tight_layout()

plt.figure()
for i, incorrect in enumerate(incorrect_indices[:9]):
    plt.subplot(3,3,i+1)
    plt.imshow(X_test[incorrect].reshape(28,28), cmap='gray', interpolation='none')
    plt.title("Predicted {}, Class {}".format(predicted_classes[incorrect], y_test[incorrect]))

plt.tight_layout()


