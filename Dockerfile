FROM tensorflow/tensorflow:1.13.1-py3

RUN apt-get update
ENV SHELL /bin/bash

# install npm and python
RUN apt-get install -y \
        apt-transport-https

# install ml lib
RUN pip3 install flask 
RUN pip3 install pandas 
RUN pip3 install keras==2.1.3
RUN pip3 install "numpy<1.17"
RUN pip3 install pillow
RUN pip3 install requests
RUN pip3 install flask_cors

# copy code.
RUN mkdir /image-eval
ADD ./ /image-eval

# make donwload dir
RUN mkdir /image-eval/src/images/

EXPOSE 80

WORKDIR /image-eval
ENTRYPOINT python3 ./src/server.py 
