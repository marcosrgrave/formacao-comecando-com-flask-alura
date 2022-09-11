from flask import Flask
from flask_restful import Api

from source.resources.games import AddGame
from source.resources.views.home import HomePage
from source.resources.views.newgame import NewGamePage


class Server:
    games_list: list = []

    def __init__(self) -> None:
        self.app = Flask(__name__,
                         template_folder="../../templates",
                         static_folder="../../static")

        self.api = Api(self.app)
        self.__add_api_resources(self.api)

    @staticmethod
    def __add_api_resources(api: Api) -> None:
        api.add_resource(AddGame, AddGame.RESOURCE_URL)
        api.add_resource(HomePage, HomePage.RESOURCE_URL)
        api.add_resource(NewGamePage, NewGamePage.RESOURCE_URL)

    def run(self) -> None:
        self.app.run(debug=True)
