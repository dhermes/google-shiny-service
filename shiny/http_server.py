from __future__ import absolute_import

import copy

import flask
from google.protobuf import empty_pb2
from google.protobuf import json_format

from shiny import shiny_pb2


app = flask.Flask(__name__)


@app.route('/v1/do-nothing/<unicorn_name>', methods=['POST'])
def do_nothing(unicorn_name):
    combined = copy.deepcopy(flask.request.json)
    combined.update(flask.request.args.to_dict())
    unicorn = combined.setdefault('unicorn', {})
    unicorn['name'] = unicorn_name
    request_obj = json_format.ParseDict(
        combined, shiny_pb2.DoNothingRequest())
    print(request_obj)

    result = empty_pb2.Empty()
    return flask.jsonify(json_format.MessageToDict(result))


if __name__ == '__main__':
    app.run(port=8080, debug=True)
