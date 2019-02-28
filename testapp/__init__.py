from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # Config
    app.config.update(
        CFG_SITE_NAME='testapp',
    )
    app.config.from_pyfile('config.py', silent=True)

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({
            "status": 404,
            "error": "Page doesn't exist"
        }), 404

    # DB
    from .models import Test
    db.init_app(app)

    # CLI
    from testapp.cli import db_cli
    app.cli.add_command(db_cli)

    # API Blueprints
    from testapp.views import blueprint as api_blueprint

    app.register_blueprint(api_blueprint)

    return app


__all__ = ('db', 'create_app')
