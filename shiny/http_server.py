from flask import Flask


app = Flask(__name__)


@app.route('/v1/do-nothing/<unicorn_name>', methods=['POST'])
def do_nothing(unicorn_name):
    return ''


if __name__ == '__main__':
    app.run(port=8080, debug=True)
