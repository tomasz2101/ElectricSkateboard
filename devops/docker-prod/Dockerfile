#FROM resin/rpi-raspbian:jessie
FROM debian:jessie
MAINTAINER TW

RUN apt-get update && apt-get install -y \
  git \
  build-essential \
  gcc \
  python \
  python-dev \
  python-pip \
  python-virtualenv \
  supervisor \
  vim \
  python-mysqldb
RUN rm -rf /var/lib/apt/lists/*

RUN pip install pyserial
RUN pip install pathlib

#RUN git clone git://git.drogon.net/wiringPi
#WORKDIR wiringPi
#RUN bash build
#RUN pip install wiringpi2

RUN mkdir /skateboard

#supervisor configuration
COPY ./run_once.script /etc/supervisor/runonce.sh
RUN chmod +x /etc/supervisor/runonce.sh
COPY ./supervisor.conf /etc/supervisor/conf.d/supervisor.conf

#vim configuration
COPY ./vim.rc /root/.vimrc

# cron
COPY ./crontabfile /tmp/crontabfile
#RUN crontab /tmp/crontabfile
RUN rm -f /tmp/crontabfile

# Define working directory
WORKDIR /skateboard
#VOLUME /data

CMD ["/usr/bin/supervisord"]