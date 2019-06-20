from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from flask import send_from_directory

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def angular():
    return send_from_directory("my-app/dist/my-app", "index.html")

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
      return send_from_directory('my-app/dist/my-app', path)

@app.route("/hello")
def hello():
    return jsonify({'text':'Hello World!'})

#@app.route("/<regex('\w\.(js|css)'):path>")
#def angular_src(path):
#    return send_from_directory("my-app/dist", path)

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id':1, 'name':'Balram'}}
        return jsonify(result)       


api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
   app.run(port=5000)
