FROM python:3.8

ARG PORT

RUN useradd python

RUN mkdir -p /home/python/profanity && chown -R python:python /home/python

COPY . /home/python/profanity

WORKDIR /home/python/profanity

USER python

RUN pip3 install fastapi==0.63.0 better_profanity==0.7.0 uvicorn==0.11.8 --no-warn-script-location

WORKDIR /home/python/profanity/profanity-check

RUN pip3 install -r ./requirements.txt --no-warn-script-location && pip3 install .

WORKDIR /home/python/profanity

CMD python3 main.py
