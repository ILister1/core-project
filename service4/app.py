from flask import Flask, Response, request, jsonify
import requests

app = Flask(__name__)

@app.route('/scene', methods=['GET', 'POST'])
def scene():

    combine = request.data.decode('utf-8')
    print(combine)
    #if combine == "Fortune found in a mysterious cavern":
        #story = "This would be a story about fortune being found in a mysterious cavern."
    #elif combine == "Fortune found in an intimidating room":
        #story = "Fortune is found in an intimidating room, with surprising results!"
    #elif combine == "Fortune found in a dreamlike headspace":
        #story = "Sometimes, the best luck you have is in your head."
    #elif combine == "Fears faced in a mysterious cavern":
        #story = "It's possibly spiders. Usually, anyway."
    #elif combine == "Fears faced in an intimidating room":
        #story = "I'm leaving you, you cow!"
    #elif combine == "Fears faced in a dreamlike headspace":
        #story = "Am I ever going to pass this project?"
    #elif combine == "Chance encounter in a mysterious cavern":
        #story = "Hoodlums up to no good down the salt mines"
    #elif combine == "Chance encounter in an intimidating room":
        #story = "I haven't seen you since I exculpated that bull."
    #else:
        #story = "The luckiest dreams are the ones you have in the daytime."
    if combine == "Love found in an empty room":
        story = "If you can't love yourself, how're you gonna love somebody else?"
    elif combine == "Love found in a perfect place":
        story = "Romance is only as perfect as the moment it exists in"
    elif combine == "Love found in a second chance":
        story = "Everybody makes mistakes. Not usually as many as you do."
    elif combine == "Desire sensed in an empty room":
        story = "Loneliness is sometimes a panacea."
    elif combine == "Desire sensed in a perfect place":
        story = "You want only the best all of the time"
    elif combine == "Desire sensed in a second chance":
        story = "I hope I get through the next assessment."
    elif combine == "Death experienced in an empty room":
        story = "Everybody dies alone."
    elif combine == "Death experienced in a perfect place":
        story = "If you could choose the way you go, you'd probably choose this."
    else:
       story = "You shouldn't have trusted him the first time."

    
    return jsonify({"data":story})

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)     
