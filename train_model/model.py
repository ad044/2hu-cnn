import keras
from keras.applications.xception import Xception
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D


def get_model():
    # create the base pre-trained model
    base_model = Xception(weights='imagenet', include_top=False, input_shape=(80, 94, 3))

    # add a global spatial average pooling layer
    x = base_model.output
    x = GlobalAveragePooling2D()(x)

    # add a fully-connected layer
    x = Dense(1024, activation='relu')(x)

    # output layer
    output = Dense(9, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=output)

    lr = 0.001
    opt = keras.optimizers.Adam(lr=lr, decay=1e-5)

    model.compile(loss='categorical_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])

    return model
