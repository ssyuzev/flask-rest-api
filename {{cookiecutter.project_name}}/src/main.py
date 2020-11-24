
import os

from werkzeug.utils import secure_filename
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
)
from flask_migrate import Migrate
from flask_smorest import Api

from config import get_config
from models import User as UserModel, db
from resources import healthcheck_api, user_api
from schemas import ma


migrate = Migrate()


def create_app(env=None):
    app = Flask(__name__)
    app.config.from_object(get_config(env))
    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        ma.init_app(app)
    return app


app = create_app()
api = Api(app)
api.register_blueprint(healthcheck_api)
api.register_blueprint(user_api)


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    return f"""
    <!doctype html>
    <title>upload new File</title>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><input type=submit value=Upload>
    </form>
    """


# CLI for migrations
@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=UserModel)


if __name__ == "__main__":
    app.run(debug=True)
