from flask import Flask, request, Response
import random
    
app = Flask(__name__)

@app.route('/theme', methods=['GET'])
def theme():

    themes = ["Fortune found in", "Fears faced in", "Chance encounter in"]
    return  Response(random.choice(themes), mimetype="text/plain")
        
 # implement a change here, alternate choice of themes?

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)    