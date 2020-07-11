from keras.callbacks.callbacks import ModelCheckpoint
import numpy as np
from model import get_model
import os


WIDTH = 80
HEIGHT = 94
NUMBER_OF_CHANNELS = 3
LR = 1e-3
NUMBER_OF_LABELS = 9
EPOCHS = 9
TRAIN_DATA_PATH = '../process_data/combined_data-v2.npy'
MODEL_CHECKPOINT_PATH = "./model_checkpoint.h5"
MODEL_NAME = 'th-xception-{}-epochs-model'.format(EPOCHS)

model = get_model()

data = np.load(TRAIN_DATA_PATH, allow_pickle=True)

train_size = int(len(data)*80/100)

train = data[:train_size]
test = data[train_size:]


X_train = np.array([i[0] for i in train]).reshape(-1, WIDTH,
                                                  HEIGHT, NUMBER_OF_CHANNELS)
y_train = np.array([i[1] for i in train])


X_test = np.array([i[0] for i in test]).reshape(-1, WIDTH,
                                                HEIGHT, NUMBER_OF_CHANNELS)
y_test = np.array([i[1] for i in test])


if os.path.exists(MODEL_CHECKPOINT_PATH):
    model.load_weights(MODEL_CHECKPOINT_PATH)

checkpoint = ModelCheckpoint(MODEL_CHECKPOINT_PATH, verbose=1);

model.fit(X_train, y_train, epochs=EPOCHS, validation_data=(X_test, y_test),
          callbacks=[checkpoint])

model.save('./' + MODEL_NAME)
