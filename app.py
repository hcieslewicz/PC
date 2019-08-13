from flask import Flask
from flask_restplus import Api
from api_v1 import blueprint

from resources.games import Games#, GamesLog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(blueprint)

api = Api(app)
#api = swagger.docs(Api(app), apiVersion='0.1')


# Flask decorator to create tables
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Games,     '/games/<string:game_name>')
#api.add_resource(GamesLog,  '/gameslog/<string:game>')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
