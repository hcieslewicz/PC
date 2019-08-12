from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT


from resources.games import Games

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)



#jwt = JWT(app, authenticate, identity)


api.add_resource(Games, '/games/<string:game>')
#api.add_resource(Games, '/games')

#api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(port=5000, debug=True)