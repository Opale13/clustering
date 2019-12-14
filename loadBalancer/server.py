#!/usr/bin/env python3

from LoadBalancer import LoadBalancer
from flask import Flask, request, jsonify
import json

loadbalancer = LoadBalancer()
app = Flask(__name__)

def setup_loadbalancer():
    with open('config.json') as json_file:
        data = json.load(json_file)
        ip_server = data["ip_server"]
        port0, port1, port2 = data["mongodb"]["ports"]
        user = data["mongodb"]["credentials"]["user"]
        psw = data["mongodb"]["credentials"]["password"]

    loadbalancer.connect("mongodb://%s:%s@%s:%s" % (user, psw, ip_server, port0))
    loadbalancer.connect("mongodb://%s:%s@%s:%s" % (user, psw, ip_server, port1))
    loadbalancer.connect("mongodb://%s:%s@%s:%s" % (user, psw, ip_server, port2))

@app.route("/get", methods=['GET','POST'])
def get():
    if request.is_json:
        data = request.get_json()
        request = loadbalancer.get(data)
        return str(request)

@app.route("/post", methods=['GET','POST'])
def post():
    if request.is_json:
        data = request.get_json()
        loadbalancer.post(data)
        return str(data)

if __name__ == '__main__':
    setup_loadbalancer()
    app.run(debug=True, host="0.0.0.0", threaded=True)
