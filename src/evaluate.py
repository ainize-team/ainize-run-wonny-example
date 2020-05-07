
######## header #########

from model import *
import numpy

script_path = os.path.dirname(os.path.realpath(__file__))
weights_file = script_path + "/weights_mobilenet_aesthetic_0.07.hdf5"
model = MyModel('MobileNet', weights=None)
model.build()
model.my_model.load_weights(weights_file)
model.my_model._make_predict_function()

def evaluate(images):
    # initialize data generator
    inputList = load_image(images[0], (224,224))
    for image in images[1:]:
        inputList = numpy.vstack((inputList, load_image(image, (224,224))))
    # get predictions
    prediction = predict(model.my_model, inputList)
    output = calc_mean_score(prediction)
    return output

