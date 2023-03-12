from flask import Flask, Response
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_page():
    return "{'status': 'success', 'message': 'Hello World!'}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
