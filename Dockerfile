FROM python:2.7

ADD . /CalcApp
WORKDIR /CalcApp
EXPOSE 8000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]