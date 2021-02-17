FROM debian:buster

RUN apt update && apt upgrade -y \
    curl python3 python3-pip python3-dev python3 -V git wget vim

RUN pip3 install RPi.GPIO paho-mqtt

WORKDIR /root
RUN git clone --depth 1 https://github.com/akihiro0000/dust-sensor.git
