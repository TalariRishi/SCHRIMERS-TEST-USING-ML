
# Importing essential libraries
from flask import Flask, render_template, request, url_for
import pickle
import numpy as np
# Load the Random Forest CLassifier model
import os, pickle

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "schirmers-test-results-model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)
@app.route('/')
def home():
    image_urls = {
        'image1': url_for('static', filename='images/mini.jpg'),
        'image2': url_for('static', filename='images/mini2.jpg'),
        'image3': url_for('static', filename='images/mini3.jpg')
    }
    return render_template('miniproject.html', image_urls=image_urls)
@app.route('/predict', methods=['GET','POST'])
def predict():
    result_url = {
        'image4': url_for('static', filename='images/mini-canva.jpg')
    }
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        wearables = int(request.form['wearables'])
        duration = int(request.form['duration'])
        onlineplatforms = int(request.form['onlineplatforms'])
        nature = int(request.form['nature'])
        screenillumination = int(request.form['screenillumination'])
        workingyears = int(request.form['workingyears'])
        hoursspentdailycurricular = int(request.form['hoursspentdailycurricular'])
        hoursspentdailynoncurricular = int(request.form['hoursspentdailynoncurricular'])
        gadgetsused = int(request.form['gadgetsused'])
        levelofgadjetwithrespecttoeyes = int(request.form['levelofgadjetwithrespecttoeyes'])
        distancebetweeneyesandgadget = int(request.form['distancebetweeneyesandgadget'])
        avgnighttimeusageperday = int(request.form['avgnighttimeusageperday'])
        blinkingduringscreenusage = int(request.form['blinkingduringscreenusage'])
        difficultyinfocusing = int(request.form['difficultyinfocusing'])
        frequencyofcomplaints = int(request.form['frequencyofcomplaints'])
        severityofcomplaints = int(request.form['severityofcomplaints'])
        rvis = int(request.form['rvis'])
        ocularsymptoms = int(request.form['ocularsymptoms'])
        symptomsatleasthalf = int(request.form['symptomsatleasthalf'])
        frequencyofdryeyes = int(request.form['frequencyofdryeyes'])
    
        data = np.array([[age, sex, wearables, duration, onlineplatforms, nature, screenillumination,
                      workingyears, hoursspentdailycurricular, hoursspentdailynoncurricular, gadgetsused,
                      levelofgadjetwithrespecttoeyes, distancebetweeneyesandgadget, avgnighttimeusageperday,
                      blinkingduringscreenusage, difficultyinfocusing, frequencyofcomplaints, severityofcomplaints,
                      rvis, ocularsymptoms, symptomsatleasthalf, frequencyofcomplaints, frequencyofdryeyes]])
        my_prediction = model.predict(data)
        return render_template('result.html', prediction=my_prediction, result_url=result_url)
# Additional routes for other pages
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/userlogin')
def userlogin():
    return render_template('userlogin.html')

if __name__ == '__main__':
    app.run()

