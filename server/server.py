from werkzeug.wrappers import response
from util import classify_image, load_saved_artifacts
from flask import Flask, jsonify
import util 

app = Flask(__name__)

@app.route('/classify_image',methods=['GET','POST'])
def classify_image(): 
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin','*')

    return  response

if __name__ == "__main__":
    print("Starting Python Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)