from main import app
from main.blueprints.HomeBluePrint import bp as homebp

app.register_blueprint(homebp, url_prefix="/zoo")

