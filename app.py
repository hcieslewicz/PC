from flask import Flask
from flask_restful import Api

from resources.games import Games, GamesLog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


# Flask decorator to create tables
@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Games,     '/games/<string:game>')
api.add_resource(GamesLog,  '/gameslog/<string:game>')


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
