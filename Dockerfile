FROM debian:11
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3 python3-venv python3-pip && apt-get clean

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["bash", "Run"]
