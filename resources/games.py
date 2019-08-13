from models.mario_saving_the_princess import MarioSavingThePrincessModel
from flask_restplus import Namespace, reqparse, Resource, fields

games_api_namespace = Namespace('games', description='Games related operations.')
gameslog_api_namespace = Namespace('gameslog', description='Game logs related operations.')

game_input_model = games_api_namespace.model("Game input model", {
    "game_name" : fields.String(description="Description string", required=True),
    "size" : fields.Integer(description="Size of the grid", min=2, required=True),
    "grid" : fields.String( description="List of strings for grid definition", required=True)
})

game_output_model = games_api_namespace.model("Game output format", {
    "error_flag": fields.String(description="Description string", required=True),
    "paths": fields.String(description="List of result paths", required=True)
})

@games_api_namespace.route('/<string:game_name>', )
@games_api_namespace.response(404, 'Game not found')
class Games(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('size', type=int, required=True, help="Size of grid cannot be left blank.")
    parser.add_argument('grid', type=str, required=True, help="Every game needs a grid string.", action='append')

    @staticmethod
    @games_api_namespace.expect(game_input_model)
    @games_api_namespace.response(400, "Bad request. Grid is not correct.", game_output_model)
    @games_api_namespace.response(404, "Game with name <game_name> not found.", game_output_model)
    @games_api_namespace.response(201, "Game result saved.", game_output_model)
    @games_api_namespace.response(500, "An error occured during saving result in database.")
    def post(game_name):

        data = Games.parser.parse_args()

        if game_name == "mario":
            game = MarioSavingThePrincessModel(data['size'], data['grid'])

            try:
                game.save_to_db()
            except Exception as e:
                #logger.error(e)
                return {"message": "An error occured during saving result in database"}, 500

            error_flag, paths = game.play()

            if int(error_flag, 2) == 1:
                return {"error_flag": error_flag, "paths": paths}, 400
            else:
                return {"error_flag": error_flag, "paths": paths}, 201
        else:
            return {"message": "Game with name {} not found".format(game_name)}, 404


@gameslog_api_namespace.route('/<string:game_name>')
@gameslog_api_namespace.param("game_name", description="Name of the game")
@gameslog_api_namespace.response(404, "Logs for game with name <game_name> not found.")
class GamesLog(Resource):
    @staticmethod
    def get(game_name):
        if game_name == "mario":
            return {"logs": [mario.json() for mario in MarioSavingThePrincessModel.query.all()]}
        else:
            return {"message": "Logs for game with name {} not found.".format(game_name)}, 404
