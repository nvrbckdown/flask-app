from flask import Flask, request, jsonify
import json
import os

app=Flask(__name__)

env = os.environ.get("ENV")
http_port = os.environ.get("HTTP_PORT")
pod = os.environ.get("MY_POD_NAME")
node = os.environ.get("MY_NODE_NAME")
token = os.environ.get("TOKEN")
address = os.environ.get("ADDRESS")

@app.route('/', methods=['GET'])
def default():
    data = request.get_data()
    print(data)
    res = {
	    'string': 'Deployment',
        'env': env,
        'http_port': http_port
	}
    return jsonify(res)

@app.route('/payme', methods=['GET'])
def get_payme():
    res = {
	    'string': 'Payme',
        'token': token,
        'address': address
	}
    return jsonify(res)

@app.route('/create-pod', methods=['GET'])
def create_pod():
    name = request.args.get("name")
    surname = request.args.get("surname")
    creator = {
        'name': name,
        'surname': surname,
    }
    res = {
		'env': env,
        'pod': pod,
        'node': node,
        'creator': creator
	}
    with open('/mnt/data.json', 'w+') as outfile:
        json.dump(res, outfile)
    outfile.close()
    return jsonify(res)

@app.route('/get-pod', methods=['GET'])
def get_pod():
    with open('/mnt/data.json', 'r') as outfile:
        data = json.loads(outfile.read())
    print(data)
    return jsonify(data)

