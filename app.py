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


if __name__ == '__main__':
    app.run()
