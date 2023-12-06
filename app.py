import json
from flask import Flask, jsonify

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

@app.route('/endpoint', methods=['GET'])
def get_json():
    data = read_json_file('volumes/data/response.json')
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
