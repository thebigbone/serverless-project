FROM ubuntu:latest

COPY . /app

WORKDIR /app

RUN apt update -y && apt install python3 python3-pip

RUN pip3 install -r requirements.txt

EXPOSE 5555

CMD ["python3", "app.py"]