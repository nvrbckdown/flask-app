from flask import Flask, request, jsonify
import json
import os

app=Flask(__name__)

@app.route('/', methods=['GET'])
def default():
    postgres = os.environ.get("POSTGRES_HOST")
    city = os.environ.get("CITY")
    name = os.environ.get("MENTOR")
    node = os.environ.get("MY_NODE_NAME")
    pod = os.environ.get("MY_POD_NAME")
    res = {
		'string': 'Udevs DevOps Bootcamp',
        'postgres': postgres,
        'city': city,
        'mentor': name,
        'pod': pod,
        'node': node
	}
    return jsonify(res)

@app.route('/project', methods=['GET'])
def get_project():
    res = {
		'string': 'Udevs DevOps Bootcamp'
	}
    return jsonify(res)

@app.route('/practice', methods=['GET'])
def get_practice():
    res = {
		'string': 'Get Practice Message!'
	}
    return jsonify(res)

@app.route('/backend', methods=['GET'])
def get_backend():
    res = {
		'string': 'Back-End Rulezzz!'
	}
    return jsonify(res)