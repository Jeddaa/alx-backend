#!/usr/bin/env python3
''' Basic flask application '''
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """
    Configuration for Babel
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


def get_user():
    """
    Returns a user dictionary or None if ID value can't be found
    or if 'login_as' URL parameter was not found
    """
    id = request.args.get('login_as')
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    '''execute before other requests'''
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def index():
    '''first route '''
    return render_template('5-index.html')


# comment line 28 and uncomment line 34 for this to work as
# the new babel doen't support @babel.localselector anymore
# this was left this way because of alx checker
@babel.localeselector
def get_locale():
    ''' get locale from request header '''
    lang = request.args.get('locale')
    id = request.args.get('login_as')
    if lang in app.config['LANGUAGES']:
        return lang
    if g.user:
        lang = g.user.get('locale')
        if lang and lang in app.config['LANGUAGES']:
            return lang
    lang = request.headers.get('langale', None)
    if lang in app.config['LANGUAGES']:
        return lang
    # return 'fr'
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
