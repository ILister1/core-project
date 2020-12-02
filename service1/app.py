from flask import Flask, render_template
import requests
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
db = SQLAlchemy(app)

class Stories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scene = db.Column(db.String(255), nullable=False)
    story = db.Column(db.String(255), nullable=False)

db.create_all()





@app.route('/', methods=['GET'])
def index():
    theme = requests.get("http://localhost:5001/theme")
    setting = requests.post("http://localhost:5002/setting", data=theme.text)
    combine = theme.text + ' ' + str(setting.text)
    response = requests.post('http://localhost:5003/scene', data=combine)
    story = str(response.json()["data"])
    complete = Stories(scene=combine, story=story)
    db.session.add(complete)
    db.session.commit()
    return render_template('index.html', combine=combine, scene=response.json())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    