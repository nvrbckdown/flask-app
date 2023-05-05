from flask import Flask, request, jsonify
import json
import os

app=Flask(__name__)

env = os.environ.get("ENV")
http_port = os.environ.get("HTTP_PORT")
token = os.environ.get("TOKEN"),
address = os.environ.get("ADDRESS")
pod = os.environ.get("MY_POD_NAME")
node = os.environ.get("MY_NODE_NAME")

@app.route('/', methods=['GET'])
def default():
    env = os.environ.get("ENV")
    http_port = os.environ.get("HTTP_PORT")
    res = {
	    'string': 'Deployment',
        'env': env,
        'http_port': http_port,
        
	}
    return jsonify(res)

@app.route('/payme', methods=['GET'])
def get_address():
    res = {
		'string': 'Payme',
        'token': token,
        'address': address
	  }
    with open('data.json', 'w') as outfile:
    json.dump(res, outfile)
    return jsonify(res)

@app.route('/pod', methods=['GET'])
def get_pod():
    res = {
		'string': 'Pod',
        'pod': pod,
        'node': node
	  }
    return jsonify(res)
