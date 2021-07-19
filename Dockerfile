FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN apt-get update -qy && \
    apt-get install -qq -y && \
    apt-get install -y locales locales-all && \
    apt-get install -y build-essential libpq-dev && \
    apt-get clean && \
    pip install --upgrade pip && \
    pip install -r ./requirements.txt
EXPOSE 5002
CMD python ./app.py
