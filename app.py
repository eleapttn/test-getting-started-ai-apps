from flask import Flask, request, jsonify
import flask
app = Flask(__name__)

@app.route('/', methods=['POST'])
def HelloWorld():

    #data = request.get_json()
    #response = 'Hello ' + data + '. Congratulations, you have launched your first AI App!'
    response = {
        'response': 'Hello world!'
    }
    return jsonify(response)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)