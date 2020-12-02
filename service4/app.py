from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/scene', methods=['GET', 'POST'])
def scene():

    combine = request.data.decode('utf-8')

    if combine == "Fortune found in a mysterious cavern":
        story = "test1"
    elif combine == "Fortune found in an intimidating room":
        story = "test2"
    elif combine == "Fortune found in a dreamlike headspace":
        story = "test3"
    elif combine == "Fears faced in a mysterious cavern":
        story = "test4"
    elif combine == "Fears faced in an intimidating room":
        story = "test5"
    elif combine == "Fears faced in a dreamlike headspace":
        story = "test6"
    elif combine == "Chance encounter in a mysterious cavern":
        story = "test7"
    elif combine == "Chance encounter in an intimidating room":
        story = "test8"
    else:
        story = "test9"
    
    return Response(story, mimetype="text/plain")

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)       
