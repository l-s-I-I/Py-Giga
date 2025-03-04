FROM debian:11
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install \
    python3 python3-dev python3-dev python3-pip python3-venv 

RUN apt-get install git curl python3-pip ffmpeg -y
RUN apt-get install git curl python3-pip mediainfo -y
RUN apt-get install git curl python3-pip p7zip-full -y
RUN apt-get update \
    && apt-get install -y unzip wget
ARG USER=root
USER $USER
RUN python3 -m venv venv
WORKDIR /app
COPY . /app/
WORKDIR /app/
RUN pip3 install --upgrade pip
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
CMD ["bash", "Run"]
