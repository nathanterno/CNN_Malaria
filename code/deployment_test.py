# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:15:47 2020

@author: NQM-Laptop
"""
import numpy as np
from tensorflow.keras.models import load_model as loadModel
import joblib
from flask import Flask, render_template, redirect, url_for, session, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet
from PIL import Image

#----------------------------------------------

#define prediction function
def return_prediction(model, target_size, saveLocation, sample_json):
    imgLoc = sample_json["imgLoc"]
    
    imgData = np.expand_dims(np.asarray( \
           Image.open(imgLoc).resize(target_size)
           ).astype(np.float32), axis = 0)
    
    classes = np.array(['parasitized', 'uninfected'])
    
    class_ind = model.predict_classes(imgData)
    
    return classes[class_ind][0][0]

#-----------------------------------------------

saveLocation = '../uploads/images'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeetYeetSupreme'
app.config['UPLOADED_IMAGES_DEST'] = saveLocation

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

#-------------------------------------

class MalariaForm(FlaskForm):

    imgFile = FileField('Image File')

#---------------------------------------

@app.route("/", methods = ['GET', 'POST'])
def index():
    form = MalariaForm()
    if form.validate_on_submit():
        filename = images.save(form.imgFile.data)
        session['imgFile'] = filename
        session['imgLoc'] = saveLocation + '/' + filename
        return redirect(url_for("malaria_prediction"))
    return render_template('home.html', form = form)
    
#load NN model and target image size
model = loadModel('malaria_detectorNQM.h5')
target_size = joblib.load("target_size.pkl")

@app.route('/malaria_prediction')
def malaria_prediction():
    content = {}
    content['imgLoc'] = session['imgLoc']
    results = return_prediction(model, target_size, saveLocation, content)
    return render_template('malaria_prediction.html', results = results, filename = session['imgFile'])

@app.route('/malaria_prediction/<filename>')
def send_image(filename):
    return send_from_directory("../uploads/images", filename)

if __name__ == '__main__':
    app.run()