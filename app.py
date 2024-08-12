import connexion
from extensions import db
from splitwise.common.exceptions import BaseCustomError


app = connexion.App(__name__, specification_dir="./splitwise/swagger")
app.add_api("swagger.yaml")

flask_app = app.app

flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///splitwise.db"
flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(flask_app)

# Create the database and tables
with flask_app.app_context():
    db.create_all()


@flask_app.errorhandler(BaseCustomError)
def handle_custom_error(error):
    response = {
        "error": {
            "message": error.message,
        }
    }
    return response, error.status_code


# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
