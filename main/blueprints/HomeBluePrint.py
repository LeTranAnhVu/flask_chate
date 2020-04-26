from flask import Blueprint, render_template

bp = Blueprint('home_bp', __name__)


@bp.route('')
def index():
    return render_template('room1.html')


@bp.route('/room2')
def room2():
    return render_template('room2.html')

@bp.route('/room3')
def room3():
    return render_template('room3.html')

