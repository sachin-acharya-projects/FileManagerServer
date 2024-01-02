from configurations.Settings import DEBUG_STATUS
from configurations.app import app
from flask import (
    render_template,
    redirect,
    jsonify,
    url_for,
    Response,
    request,
    session,
)


@app.errorhandler(404)
def handlePageMissing(e):
    return f"<strong>{e}</strong>"


@app.route("/")
def home():
    return "<h1>Welcome to HOMEPAGE</h1>"


# Browse Files
@app.route("/browse")
def browseFiles():
    ...

if __name__ == "__main__":
    app.run(debug=DEBUG_STATUS)
