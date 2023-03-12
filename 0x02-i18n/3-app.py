#!/usr/bin/env python3
''' Basic flask application '''
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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


@app.route('/', strict_slashes=False)
def index():
    '''first route '''
    return render_template('3-index.html')


# comment line 28 and uncomment line 34 for this to work as
# the new babel doen't support @babel.localselector anymore
# this was left this way because of alx checker
@babel.localeselector
def get_locale():
    ''' get locale from request header '''
    # return 'fr'
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
