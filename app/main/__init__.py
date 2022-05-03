from flask import Blueprint

"""
Creating a blueprint
"""
main = Blueprint('main',__name__)
from . import views,errors