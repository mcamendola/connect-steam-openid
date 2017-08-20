FROM python:3.6.2-alpine3.6

MAINTAINER Murilo Amêndola <muriloamendola@gmail.com>

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt
ADD ./run.py /app/run.py
ADD ./src /app/src 

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]