#!/usr/bin/env python3
"""
Flask app module
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
from typing import (
    Dict,
    Union
)


class Config(object):
    """
    Class that configures attributes
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Function that returns a user dictionary or
    None if ID value can't be found or if 'login_as'
    URL parameter was not found
    """
    id = request.args.get('login_as', None)
    if id and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Function that adds user to
    flask if user is found
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Function that determines best language match based on supported languages
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Handles / route
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
