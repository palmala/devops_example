from python:3.10.10-slim

RUN apt-get update
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /
ENTRYPOINT ["python"]
CMD ["/app/main.py"]