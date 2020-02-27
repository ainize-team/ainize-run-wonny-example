FROM tensorflow/tensorflow:1.13.1-gpu-py3

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

# copy ain-v1-worker code.
RUN mkdir /image-eval
ADD package.json /image-eval
ADD ./ /image-eval

EXPOSE 5000

WORKDIR /image-eval
RUN yarn
ENTRYPOINT python3 ./src/server.py 
