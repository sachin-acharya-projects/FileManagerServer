from configurations.Settings import *
from flask import Flask

# Flask app initialization
app = Flask(
    __name__,
    static_folder=STATIC_FOLDER,
    static_url_path=STATIC_URL_PATH,
    template_folder=TEMPLATE_FOLDER,
)

# Application Configurations
app.config["secret"] = SECRET_KEY
