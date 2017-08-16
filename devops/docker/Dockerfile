#FROM resin/rpi-raspbian:jessie
FROM debian:jessie
MAINTAINER TW

RUN mkdir /data
# update
RUN apt-get update
# Install dependencies
RUN apt-get install -y git
RUN apt-get install -y build-essential
RUN apt-get install -y gcc
RUN apt-get install -y python
RUN apt-get install -y nano
RUN apt-get install -y python-dev
RUN apt-get install -y supervisor
RUN apt-get install -y python-pip
RUN apt-get install -y python-virtualenv
RUN apt-get install -y dos2unix
RUN rm -rf /var/lib/apt/lists/*
     


# RUN pip install pyserial
# RUN git clone git://git.drogon.net/wiringPi


# RUN make 
# RUN gcc
#RUN cd wiringPi && ./build
#RUN pip install wiringpi2

COPY ./sync /data

#supervisor configuration
COPY ./run_once.script /etc/supervisor/runonce.sh
RUN chmod +x /etc/supervisor/runonce.sh
COPY ./supervisor.conf /etc/supervisor/conf.d/supervisor.conf



# cron
COPY ./crontabfile /tmp/crontabfile
# RUN crontab /tmp/crontabfile
RUN rm -f /tmp/crontabfile

# Define working directory
WORKDIR /data
#VOLUME /data

CMD ["/usr/bin/supervisord"]