from flask import Flask
from config.config import config
from mongo_config import mongodb_client


def init_app(): 
    app = Flask(__name__, instance_relative_config=False)

    app.config["MONGO_URI"] = config["mongodb"]["uri"]

    mongodb_client.init_app(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(grades_blueprint)

    return app


if __name__ == "__main__": 
    from modules.auth.auth_controller import auth as auth_blueprint 
    from modules.grades.grades_controller import grades as grades_blueprint 

    app = init_app()

    @app.route('/', methods=['GET'])
    def home(): 
        return "All Systems Operational."

    app.run(port=5000, debug=True)

