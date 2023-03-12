import random

import uvicorn
from fastapi import FastAPI, Response, Request
from fastapi.templating import Jinja2Templates
import logging
from prometheus_client import Counter, generate_latest, Summary
import time

logger = logging.getLogger(__name__)
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

TEST_COUNTER = Counter(
    'test_counter',
    'A test counter'
)

REQUEST_TIME = Summary(
    'test_request_time',
    'Time spent processing request'
)


@REQUEST_TIME.time()
def dummy_request():
    time.sleep(random.randint(1, 4))


@app.get(path="/")
async def root():
    TEST_COUNTER.inc()
    return {"message": "Hello"}


@app.get(path="/stuff")
async def some_other_stuff():
    dummy_request()
    return {"message": "This one is different!"}


@app.get(path="/metrics")
async def root():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
