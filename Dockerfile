from python:3.10

RUN apt-get update && apt-get install -y python3-tk
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /
ENTRYPOINT ["python"]
CMD ["/app/main.py"]