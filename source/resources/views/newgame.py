from os import getenv

from flask import render_template, make_response
from flask_restful import Resource

from source.resources.views.home import HomePage


class NewGamePage(Resource):
    RESOURCE_URL: str = "/newgame"

    @staticmethod
    def get():
        template = render_template(template_name_or_list="body/newgame.html",
                                   title="REGISTER NEW GAME",
                                   home_page=getenv("API_URL") + HomePage.RESOURCE_URL)
        response = make_response(template)
        response.headers["Content-Type"] = "text/html"
        return response
