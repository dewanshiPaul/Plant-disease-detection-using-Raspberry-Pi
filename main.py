#imports
import imghdr
import cv2
import os
import numpy as np
from keras.models import load_model
from keras_preprocessing.image import load_img, img_to_array
from keras.applications.resnet import preprocess_input
from mail import email_alert_disease

#define paths
path = 'C:/Users/thats/Desktop/IoT/datasets/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/'
path_train = path+'/train'
path_frame = 'C:/Users/thats/Desktop/IoT/frame/'

#load model
print('loading model......')
b_model = load_model('C:/Users/thats/Desktop/IoT/best_model.h5')
print('model loaded!!')

#labels
label = os.listdir(path_train)

#prediction function
def prediction(path):
    img = load_img(path, target_size=(224,224))
    i = img_to_array(img)

    im = preprocess_input(i)
    img = np.expand_dims(i, axis=0)

    pred = np.argmax(b_model.predict(img))

    return (label[pred])

#camera feed for prediction
vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    cv2.imwrite(path_frame+'/image.jpg',frame)
    result = prediction(path_frame+'/image.jpg')
    cv2.putText(frame,result,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow('Detection',frame)
    content = result.split('__')
    if 'healthy' not in content[-1]:
        title = 'ALERT!!! Your plant got affected :('
        body = '''
        Hi user, \n
        \t This is an email alert is to let you know that your 
        plants are getting affected with disease
        ''' + result

        with open(path_frame+'image.jpg','rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
        
        sender = "" #set
        email_alert_disease(title,body,sender,image_data,result,image_type)
    key = cv2.waitKey(1)
    if key == 27:
        print('esc is pressed, closing all windows')
        cv2.destroyAllWindows()
        break

vid.release()