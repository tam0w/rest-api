from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/send/<string:msg>', methods=['GET','POST'])
def send(msg):
    return jsonify({'message': msg})


if __name__ == '__main__':
    app.run()
