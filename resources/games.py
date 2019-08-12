from flask_restful import Resource, reqparse
from models.mario_saving_the_princess import MarioSavingThePrincessModel


class Games(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('size', type=int, required=True, help="Size of grid cannot be left blank")
    parser.add_argument('grid', type=str, required=True, help="Every game needs a grid string", action='append')

    @staticmethod
    def get(game):

        data = Games.parser.parse_args()

        if game == "mario":
            game = MarioSavingThePrincessModel(data['size'], data['grid'])
            game.save_to_db()
            error_flag, paths = game.play()
            return {"error_flag": error_flag, "paths": paths}

        return {"message": "Game with name {} not found".format(game)}


class GamesLog(Resource):
    @staticmethod
    def get(game):
        if game == "mario":
            return {"logs": [mario.json() for mario in MarioSavingThePrincessModel.query.all()]}
