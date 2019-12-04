FROM ubuntu:16.04
MAINTAINER cap-diego

ENV USER jenkins

USER root

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk wget gnupg && \
    sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/> /etc/apt/sources.list.d/jenkins.list'

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 9B7D32F2D50582E6
RUN apt-get update && apt-get install -y git jenkins

#RUN groupadd -r $USER && useradd -r -g $USER $USER
#RUN useradd -r -g $USER $USER
RUN apt-get install -y nano && apt-get install -y vim
#RUN service jenkins restart
#RUN service jenkins start
#RUN service jenkins status
# update
RUN apt-get update
# install curl
RUN apt-get install -y curl
# get install script and pass it to execute:
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash
# and install node
RUN apt-get install -y nodejs

USER $USER

CMD tail -f /dev/null


