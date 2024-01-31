import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/send', methods=['GET','POST'])
def send():
    print(request.json)
    data = request.json
    return jsonify({'message': data['message']})

@app.route('/api/match', methods=['GET','POST'])
def send():
    data = requests.get('https://practistics.live/getjson/F8265')
    print(data.json())
    return jsonify(data.json())




if __name__ == '__main__':
    app.run()
