import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


from games.mario_saving_the_princess import MarioSavingThePrincess

class Games(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('size', type=int, required=True, help="Size of grid cannot be left blank")
    parser.add_argument('grid', type=str, required=True, help="Every game needs a grid string", action='append')

    def get(self, game):

        data = Games.parser.parse_args()
        print(data)
        if game == "mario":
            game = MarioSavingThePrincess(data['size'], data['grid'])
            error_flag, paths = game.play()
            return {"error_flag" : error_flag, "paths": paths}

        return {"message" : "Game with name {} not found".format(game)}

