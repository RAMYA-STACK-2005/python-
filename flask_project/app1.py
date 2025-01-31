from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
     fruits = []
     def get(self):
        return {"fruits": self.fruits}
     def post(self):
        self.fruits.append("Pineapple")
        return {"fruits": "added successfully"}
api.add_resource(HelloWorld, '/fruits')
if __name__ == '__main__':
 app.run(debug=True)