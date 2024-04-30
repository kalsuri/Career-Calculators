from flask import Flask
from .routes import configure_routes

def create_app():
    # Initialize the Flask application
    app = Flask(__name__, instance_relative_config=True)
    
    # Load the default configuration
    app.config.from_object('config.Config')

    # Load the configuration from the instance folder
    app.config.from_pyfile('application.cfg', silent=True)
    
    # Register the routes from the routes.py file
    configure_routes(app)
    
    return app
