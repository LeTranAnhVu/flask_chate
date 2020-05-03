from main import app
from main.blueprints.HomeBluePrint import bp as homebp
from main.blueprints.AuthBluePrint import blueprint as auth_blueprint
from main.blueprints.MessageBluePrint import blueprint as message_blueprint

# auth
app.register_blueprint(auth_blueprint, url_prefix='/api/auth')


#messages
app.register_blueprint(message_blueprint, url_prefix='/api/messages')
