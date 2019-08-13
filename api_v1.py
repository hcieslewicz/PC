from flask import Blueprint
from flask_restplus import Api
from resources.games import games_api_namespace, gameslog_api_namespace

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
#api = Api(blueprint)


#from .apis.namespace2 import api as ns2
# ...
#from .apis.namespaceX import api as nsX


api = Api(blueprint,
    title='Games API',
    version='1.0',
    description='This is API documentation for mario game purpose',
    # All API metadatas
)

api.add_namespace(games_api_namespace)
api.add_namespace(gameslog_api_namespace)
#api.add_namespace(ns2)
## ...
#api.add_namespace(nsX)

