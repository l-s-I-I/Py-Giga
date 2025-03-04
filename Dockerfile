FROM debian:11
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install \
RUN python3 -m venv venv
COPY . /app/
WORKDIR /app/
RUN pip3 install --upgrade pip
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
CMD ["bash", "Run"]
