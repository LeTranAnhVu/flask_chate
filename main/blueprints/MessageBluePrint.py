from flask import Blueprint, request, abort, g, jsonify
from main.blueprints.AuthBluePrint import login_required
import datetime

blueprint = Blueprint('message', __name__)


@blueprint.route('/<int:conversation_id>', methods=['GET', 'POST'])
@login_required()
def messages(conversation_id):
    if request.method == 'GET':
        return jsonify({'message':'get'}), 200

    if request.method == 'POST':
        return jsonify({'message':'post'}), 200
