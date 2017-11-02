"""
Flask web site with vocabulary matching game (identify vocabulary words that can be made from a scrambled string)
"""
import flask
import logging
import config                       # Our own module


def process(raw):
    app.logger.info("in process")
    cooked = {}
    i = 0
    for line in raw:
        parts = line.split(';')
        if len(parts) != 5:
            raise ValueError("Text file format is invalid")
        else:
            cooked[i] = {}
            cooked[i]['name'] = parts[0]
            cooked[i]['lat'] = float(parts[1])
            cooked[i]['lng'] = float(parts[2])
            cooked[i]['addy'] = parts[3]
            cooked[i]['sport'] = parts[4]
        i += 1
    return cooked


############# Globals #############
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY  # Should allow using session variables
app.API_key = CONFIG.API_KEY


############# Pages #############
@app.route("/")
@app.route("/index")
def index():
    """The main page of the application"""
    f = open("data/volleyball.txt")
    poi = process(f)
    app.logger.info(poi)
    flask.g.API_key = app.API_key
    return flask.render_template('homepage.html', poi=poi)

############# Error handlers #############


@app.errorhandler(404)
def error_404(e):
    app.logger.warning("++ 404 error: {}".format(e))
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning("++ 500 error: {}".format(e))
    assert not True  # I want to invoke the debugger
    return flask.render_template('500.html'), 500


@app.errorhandler(403)
def error_403(e):
    app.logger.warning("++ 403 error: {}".format(e))
    return flask.render_template('403.html'), 403


############# Main #############
if __name__ == "__main__":

    if CONFIG.DEBUG:
        app.debug = True
        app.logger.setLevel(logging.DEBUG)
        app.logger.info(
            "Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
