from __future__ import division, print_function
import sys
import os
from io import BytesIO
import base64
import requests

from fastai import *
from fastai.vision import *

from flask import Flask, render_template, request
from PIL import Image as PILImage

import config 
#variables

app = Flask(__name__)

def setup_model_pth(path_to_file, to_load, classes):
    data = ImageDataBunch.single_from_classes(
        path_to_file, classes, ds_tfms=get_transforms(), size=224).normalize(imagenet_stats)
    learn = cnn_learner(data, models.densenet169, model_dir='models')
    learn.load(to_load, device=torch.device('cpu'))
    return learn

learn = setup_model_pth(config.path_to_model, config.name_model, config.classes)

def encode(img):
    img = (image2np(img.data) * 255).astype('uint8')
    pil_img = PILImage.fromarray(img)
    buff = BytesIO()
    pil_img.save(buff, format="JPEG")
    return base64.b64encode(buff.getvalue()).decode("utf-8")
	
def model_predict(img):
    img = open_image(BytesIO(img))
    pred_class,pred_idx,outputs = learn.predict(img)
    formatted_outputs = ["{:.1f}%".format(value) for value in [x * 100 for x in torch.nn.functional.softmax(outputs, dim=0)]]
    pred_probs = sorted(
            zip(learn.data.classes, map(str, formatted_outputs)),
            key=lambda p: p[1],
            reverse=True
        )
	
    img_data = encode(img)
    result = {"class":pred_class, "probs":pred_probs, "image":img_data}
    return render_template('result.html', result=result)
   

@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')


@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        img = request.files['file'].read()
        if img != None:
            preds = model_predict(img)
            return preds
    return 'OK'
	
@app.route("/classify-url", methods=["POST", "GET"])
def classify_url():
    if request.method == 'POST':
        url = request.form["url"]
        if url != None:
            response = requests.get(url)
            preds = model_predict(response.content)
            return preds
    return 'OK'
    

if __name__ == '__main__':
    port = os.environ.get('PORT', config.port)

    if "prepare" not in sys.argv:
        app.run(debug=False, host='0.0.0.0', port=port)
