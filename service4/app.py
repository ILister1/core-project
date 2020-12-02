from flask import Flask, Response, request, jsonify
import requests

app = Flask(__name__)

@app.route('/scene', methods=['GET', 'POST'])
def scene():

    combine = request.data.decode('utf-8')
    print(combine)
    if combine == "Fortune found in a mysterious cavern":
        story = "This would be a story about fortune being found in a mysterious cavern."
    elif combine == "Fortune found in an intimidating room":
        story = "Fortune is found in an intimidating room, with surprising results!"
    elif combine == "Fortune found in a dreamlike headspace":
        story = "Sometimes, the best luck you have is in your head."
    elif combine == "Fears faced in a mysterious cavern":
        story = "It's possibly spiders. Usually, anyway."
    elif combine == "Fears faced in an intimidating room":
        story = "I'm leaving you, you cow!"
    elif combine == "Fears faced in a dreamlike headspace":
        story = "Am I ever going to pass this project?"
    elif combine == "Chance encounter in a mysterious cavern":
        story = "Hoodlums up to no good down the salt mines"
    elif combine == "Chance encounter in an intimidating room":
        story = "I haven't seen you since I exculpated that bull."
    else:
        story = "The luckiest dreams are the ones you have in the daytime."
    
    return jsonify({"data":story})

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)       
