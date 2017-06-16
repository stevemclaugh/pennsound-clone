# Audio Labeling Container
FROM ubuntu:14.04

MAINTAINER Steve McLaughlin <stephen.mclaughlin@utexas.edu>

EXPOSE 3805

ENV SHELL /bin/bash
#ENV PYTHONWARNINGS="ignore:a true SSLContext object"

# Update OS
RUN apt-get update && apt-get install -y \
software-properties-common \
build-essential \
python-dev \
python-pip \
wget \
git \
unzip \
&& python -m pip install -U pip \
&& pip install -U \
setuptools \
Flask \
Jinja2 \
unicodecsv

COPY ./setup.sh /home/
RUN mkdir -p /home/x/

COPY ./requirements.txt /var/local/
RUN pip install -qr /var/local/requirements.txt

# Install FFmpeg with mp3 support
#RUN add-apt-repository -y ppa:mc3man/trusty-media \
# && apt-get update -y \
# && apt-get install -y ffmpeg gstreamer0.10-ffmpeg

WORKDIR /home/x/
#ENTRYPOINT ["bash","/home/setup.sh"]
