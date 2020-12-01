from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    theme = requests.get("http://localhost:5001/theme")
    setting = requests.post("http://localhost:5002/setting", data=theme.text)
    combine = theme.text + setting.text
    scene = requests.post('http://localhost:5003/scene', data=combine)


    return render_template('index.html', scene=scene, story=story.text)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    