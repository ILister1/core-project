from application import app, db
from flask import Flask, render_template
import requests
from application.models import Stories

@app.route('/', methods=['GET'])
def index():
    theme = requests.get("http://service2:5001/theme")
    setting = requests.post("http://service3:5002/setting", data=theme.text)
    combine = theme.text + ' ' + str(setting.text)
    response = requests.post('http://service4:5003/scene', data=combine)
    story = str(response.json()["data"])
    complete = Stories(scene=combine, story=story)
    db.session.add(complete)
    db.session.commit()
    return render_template('index.html', combine=combine, scene=response.json())
