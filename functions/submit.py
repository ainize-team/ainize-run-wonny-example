
######## header #########

from model import *

weights_file = '/workspace/functions/weights_mobilenet_aesthetic_0.07.hdf5'

def evaluate(image):
    ## TODO : you have only model_path and image_path for parameters
    # # build model and load weights
    base_model_name = 'MobileNet'
    model = MyModel(base_model_name, weights=None)
    model.build()
    model.my_model.load_weights(weights_file)

    # initialize data generator
    resize_image = load_image(image, (224,224))

    # get predictions
    prediction = predict(model.my_model, resize_image)
    output = calc_mean_score(prediction)
    K.clear_session()
    return output

