#!/usr/bin/env python3

from LoadBalancer import LoadBalancer
from flask import Flask, request, jsonify

loadbalancer = LoadBalancer()
app = Flask(__name__)

loadbalancer.connect("mongodb://root:root@51.91.157.95:27017")
loadbalancer.connect("mongodb://root:root@51.91.157.95:27018")
loadbalancer.connect("mongodb://root:root@51.91.157.95:27019")

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
    app.run(debug=True, host="0.0.0.0", threaded=True)
