from flask import request, redirect
from flask_restful import Resource

from source.models.game import GameModel
from source.resources.views.home import HomePage
from source.server.mock_data import games


class AddGame(Resource):
    RESOURCE_URL: str = "/games/add"

    @staticmethod
    def post() -> redirect:
        new_game = GameModel(request.form.get("name"), request.form.get("category"))
        games.append(new_game)

        return redirect(HomePage.RESOURCE_URL)
