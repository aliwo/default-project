from application import application,models
from flask import request, render_template, session, redirect, url_for, send_from_directory, jsonify
from application.errors import InvalidUsage
from sqlalchemy import desc


@application.route('/', methods=['GET'])
def index():
    return 'Hello Flask!'\


# @application.route('/test', methods=['GET'])
# def test():
#     text =



@application.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
