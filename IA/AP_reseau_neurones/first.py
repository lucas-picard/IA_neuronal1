from keras import *
import numpy as np

model = Sequential()

# entrer
model.add(layers.Dense(units=3, input_shape=[1]))

# couche cacher
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=1))

# donne une valeur d'entré
entre = np.array([[1], [2], [3], [4], [5]])
# donné valeur sorti
sortie = np.array([[2], [4], [6], [8], [10]])

# sortie
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x=entre, y=sortie, epochs=1000)


while True:
    x = int(input('Nombre: '))
    print(model.predict(np.array([[x]]), verbose=0))
 