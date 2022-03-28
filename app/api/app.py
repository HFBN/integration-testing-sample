from flask import Flask

# The main function which uses the Flask package to create our app.
def create_app(*, config_object) -> Flask:
    """Create a flask app instance."""

    # Instantiate a generic app
    flask_app = Flask('prediction_api')
    # Add config
    flask_app.config.from_object(config_object)

    # Import and add the blueprint - the blueprint is 
    # where we define our custom prediction logic
    from .controller import prediction_app
    flask_app.register_blueprint(prediction_app)

    return flask_app