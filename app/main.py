import uvicorn
from fastapi import FastAPI, Response
from fastapi.templating import Jinja2Templates
import logging
from prometheus_client import Counter, generate_latest

logger = logging.getLogger(__name__)
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

TEST_COUNTER = Counter(
    'test_counter',
    'A test counter'
)


@app.get(path="/")
async def root():
    TEST_COUNTER.inc()
    return {"message": "Hello"}


@app.get(path="/metrics")
async def root():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
