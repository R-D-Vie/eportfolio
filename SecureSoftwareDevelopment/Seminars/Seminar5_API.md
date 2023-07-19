# Seminar 5: Developing an API for a Distributed Environment

I had issues getting the provided code to work via the Jupyter Notebook environment on codio or by using jupyter directly on my machine, so I completed the work for this seminar by downloading flask directly to my machine.

After installing Flask, I ran the following codeblock via the windows terminal using first `flask run` and then `python3 api.py`.

```python
from flask import Flask
from flask_restful import Api, Resource, reqparse
 
app = Flask(__name__)
api = Api(app)
 
users = [
    {
        "name": "James",
        "age": 30,
        "occupation": "Network Engineer"
    },
    {
        "name": "Ann",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jason",
        "age": 22,
        "occupation": "Web Developer"
    }
]
 
class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404
 
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
 
        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400
 
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
 
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
 
        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
 
    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(User, "/user/<string:name>")
 
app.run(debug=True)
```




This is the output:

<img src="Picture1.png">

Not being familiar with Flask, I learned that running the by calling 'flask run' would start the program with the debugger off for security reasons. This could be fixed by settint the `FLASK_APP` variable to my file name "api.py" and running the app in debug mode:

<img src="Screenshot 2023-07-09 143634.png">

Running the app in debug mode using app.run(debug=True), enables debugging features and provides more detailed error messages during development.

#### Running Test Commands:

Running these commands: `w3m http://127.0.0.1:5000/user/Ann` and `w3m http://127.0.0.1:5000/user/Adam` invoked the GET method and returned either the user record (with code 200) or 'User Not Found' (with code 404).

In VSCode, I also experimented with the `post` method to add a user to the dictionary:

<img src="Screenshot 2023-07-09 145310.png">

#### What is the capability achieved by the flask library?

Flask is a useful web framework to allow the building of apps and APIs - it can be used to manage the underlying web-related tasks which underpin an application. In this example, it expemlifies the fact thst it can support HTTP methods like GET, POST, PUT, DELETE, which can be used to achieve CRDU capability.
