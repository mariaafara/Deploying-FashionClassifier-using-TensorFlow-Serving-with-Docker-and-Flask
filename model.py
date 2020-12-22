import tensorflow as tf
import numpy as np
import json
import requests
# sudo docker run -v $(pwd)/my_fashion_model:/models/fashion_model/1 -e MODEL_NAME=fashion_model -p 9501:8501 tensorflow/serving
SIZE=28
MODEL_URI='http://localhost:9501/v1/models/fashion_model:predict'
CLASSES = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# load, pre-process and encode the image in JSON object
# make a post request to the model server using MODEL_URI and perform post-processing on the model prediction.
def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(SIZE, SIZE), color_mode="grayscale")
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    print(image.shape)
    data = json.dumps({
        'instances': image.tolist()
    })
    response = requests.post(MODEL_URI, data=data.encode('utf-8'))
    result = json.loads(response.text)
    print("result ",result)
    prediction = np.squeeze(result['predictions'][0])
    print("prediction ",prediction)
    print("max ",np.argmax(prediction))
    class_name = CLASSES[np.argmax(prediction)]
    return class_name
