from flask import Flask, request, Response
import random
    
app = Flask(__name__)

@app.route('/setting', methods=['GET', 'POST'])
def setting():

    settings = ["a mysterious cavern", "an intimidating room", "a dreamlike headspace"]
    return  Response(random.choice(settings), mimetype="text/plain")

   # settings = ["an empty room", "a perfect place", "a second chance"]
   # return  Response(random.choice(settings), mimetype="text/plain")
        
    #settings = ["an empty room", "a perfect place", "a second chance"]
    #return  Response(random.choice(settings), mimetype="text/plain")

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)    
