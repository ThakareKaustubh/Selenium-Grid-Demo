FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk unzip && \
    wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz && \
    tar -zxvf allure-2.27.0.tgz && \
    mv allure-2.27.0 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure
COPY . .

CMD ["pytest"]
