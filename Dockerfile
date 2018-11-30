from python:3.7-alpine

ADD hanako ./hanako
ADD requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "-m", "hanako.cli.server"]