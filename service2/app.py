from flask import Flask, request, Response
import random
    
app = Flask(__name__)

@app.route('/theme', methods=['GET', 'POST'])
def theme():

    themes = ["Fortune found in", "Fears faced in", "Chance encounter in"]
    return  Response(random.choice(themes), mimetype="text/plain")

     #themes = ["Love found in", "Desire sensed in", "Death experienced in"]
     #return  Response(random.choice(themes), mimetype="text/plain")
        
 

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)        
