from __future__ import absolute_import

import copy

import flask
from google.protobuf import empty_pb2
from google.protobuf import json_format

from shiny import shiny_pb2


app = flask.Flask(__name__)


def _request_to_proto(request, message):
    combined = copy.deepcopy(flask.request.json)
    combined.update(flask.request.args.to_dict())
    return json_format.ParseDict(combined, message)


@app.route('/v1/do-nothing/<unicorn_name>', methods=['POST'])
def do_nothing(unicorn_name):
    request = _request_to_proto(
        flask.request, shiny_pb2.DoNothingRequest())

    request.unicorn.name = unicorn_name

    print(request)

    response = empty_pb2.Empty()
    return flask.jsonify(json_format.MessageToDict(response))


if __name__ == '__main__':
    app.run(port=8080, debug=True)
