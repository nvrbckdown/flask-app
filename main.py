from flask import Flask, request, jsonify
import json
import os

app=Flask(__name__)

env = os.environ.get("ENV")
http_port = os.environ.get("HTTP_PORT")
postgres = os.environ.get("POSTGRES_HOST")
postgres_port = os.environ.get("POSTGRES_PORT")
postgres_db = os.environ.get("POSTGRES_DB")
postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")
mongo_host = os.environ.get("MONGO_HOST")
mongo_db = os.environ.get("MONGO_DB")
mongo_user = os.environ.get("MONGO_USER")
mongo_password = os.environ.get("MONGO_PORT")
mongo_port = os.environ.get("MONGO_PASSWORD")
token = os.environ.get("TOKEN"),
address = os.environ.get("ADDRESS")
pod = os.environ.get("MY_POD_NAME")
node = os.environ.get("MY_NODE_NAME")
ns = os.environ.get("MY_POD_NAMESPACE")

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

@app.route('/psql', methods=['GET'])
def get_psql():
    res = {
		'string': 'PSQL',
        'postgres': postgres,
        'postgres_port': postgres_port,
        'postgres_user': postgres_user,
        'postgres_db': postgres_db,
        'postgres_password': postgres_password,
	}
    return jsonify(res)

@app.route('/mongo', methods=['GET'])
def get_mongo():
    res = {
		'string': 'Mongo',
        'mongo': mongo_host,
        'mongo_port': mongo_port,
        'mongo_user': mongo_user,
        'mongo_db': mongo_db,
        'mongo_password': mongo_password,
	}
    return jsonify(res)

@app.route('/payme', methods=['GET'])
def get_address():
    res = {
		'string': 'Payme',
        'token': token,
        'address': address
	}
    return jsonify(res)

@app.route('/pod', methods=['GET'])
def get_pod():
    res = {
		'string': 'Pod',
        'pod': pod,
        'node': node,
        'namespace': ns
	}
    return jsonify(res)
