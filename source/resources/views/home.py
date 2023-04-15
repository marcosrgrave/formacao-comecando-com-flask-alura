from os import getenv

from flask import render_template, make_response
from flask_restful import Resource

from source.resources.views.newgame import NewGamePage
from source.server.mock_data import games


class HomePage(Resource):
    RESOURCE_URL: str = "/"

    @staticmethod
    def get() -> make_response:
        template = render_template(template_name_or_list="body/home.html",
                                   title="GAME STORE",
                                   games=games,
                                   new_game_page=getenv("API_URL") + NewGamePage.RESOURCE_URL)
        response = make_response(template)
        response.headers["Content-Type"] = "text/html"
        return response
