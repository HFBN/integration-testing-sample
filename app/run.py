from api.app import create_app
from api.config import Config

## Create the app using the defined function
flask_app = create_app(
    config_object=Config)


if __name__ == '__main__':
    # Run the app
    flask_app.run()