FROM python:3.8-slim
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python","app.py"]