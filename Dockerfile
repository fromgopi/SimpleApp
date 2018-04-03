FROM python:2.7

ADD . /CalcApp
WORKDIR /CalcApp
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
