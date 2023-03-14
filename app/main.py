from flask import Flask, Response
from prometheus_client import Counter, generate_latest
import logging

logger = logging.getLogger(__name__)
app = Flask(__name__)
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

TEST_COUNTER = Counter(
    'test_counter',
    'A test counter'
)


@app.route('/metrics', methods=['GET'])
def get_data():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route('/', methods=['GET'])
def hello_page():
    TEST_COUNTER.inc()
    return {'status': 'success', 'message': 'Hello World!'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
