import matplotlib
from keras.models import load_model
import matplotlib.image as processimage
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
from PIL import Image
%matplotlib inline

class DogPrediction(object):
    def __init__(self,ModelFile,PredictFile,Width=100, Height=100):
        self.modelfile = ModelFile
        self.predict_file = PredictFile
        self.DogType = ["中国沙皮犬","哈士奇", "德国牧羊犬", "拉布拉多", "柯基", "秋田犬", "英国牧羊犬", "萨摩耶犬", "藏獒", "博美"]
        self.Width = Width
        self.Height = Height

    #预测
    def Predict(self):
        model = load_model(self.modelfile)
        img_open = Image.open(self.predict_file)
        conv_RGB = img_open.convert("RGB")
        new_img = conv_RGB.resize((self.Width, self.Height), Image.BILINEAR)
        new_img.save(self.predict_file)
        image = processimage.imread(self.predict_file)
        image_to_array = np.array(image)/255.0 #转出float
        image_to_array = image_to_array.reshape(-1,100,100,3)
        prediction = model.predict(image_to_array)
        Final_Pred = [result.argmax() for result in prediction][0]
        count = 0
        for i in prediction[0]:
            percent = "%.2f%%"%(i*100)
            print(self.DogType[count], "概率", percent)
            count += 1

    查看图片
    def ShowPredImg(self):
        img = Image.open(self.predict_file)
        plt.imshow(img)

Pred = DogPrediction(PredictFile = "Pred_img/1.jpg", ModelFile = "dogfinder.h5")
Pred.ShowPredImg()
Pred.predict()