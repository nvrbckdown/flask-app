from flask import Flask, request, jsonify, render_template
import json
import os
import psycopg2

app=Flask(__name__)

env = os.environ.get("ENV", "staging")
http_port = os.environ.get("HTTP_PORT", "80")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")

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


@app.route('/get-pod', methods=['GET'])
def get_pod():
    with open('/mnt/data.json', 'r') as outfile:
        data = json.loads(outfile.read())
    print(data)
    return jsonify(data)

def postgres():
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=db_port)
    if conn():
        print("Connection to database is successful")
    return conn

@app.route('/get-company', methods=['GET'])
def get_company():
    con = postgres()
    cur = con.cursor()
    query = "SELECT * FROM company"
    cur.execute(query=query)
    companies = cur.fetchall()
    cur.close()
    con.close()
    print(companies)
    return render_template('index.html', companies=companies)

@app.route('/select-company', methods=['GET'])
def select_company():
    id = request.args.get("id")
    con = postgres()
    cur = con.cursor()
    query = "SELECT * FROM {company} WHERE id={id} ".format(id=id, company="company")
    cur.execute(query=query)
    companies = cur.fetchall()
    cur.close()
    con.close()
    return render_template('index.html', companies=companies)
    