# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense, Activation  
from keras.optimizers import RMSprop  
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)
# load pima indians dataset
dataset = numpy.loadtxt("antigen-score.txt", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:600]
# Y = dataset[:,600]
Y = dataset[:,600:]
print(Y[0])
# create model
model = Sequential([  
    Dense(128, input_dim=600),  
    Activation('tanh'),  
    Dense(128),  
    Activation('tanh'),  
    Dense(67),  
    Activation('softmax'),  
])
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0) 
# Compile model
model.compile(loss='binary_crossentropy', optimizer=rmsprop, metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=300, batch_size=128)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
model.save("antigen.h5")