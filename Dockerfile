FROM tensorflow/tensorflow:2.14.0-gpu

ENV SHELL /bin/bash

# install apt packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      apt-transport-https && \
#       bzip2 \
#       g++ \
#       git \
#       graphviz \
#       libgl1-mesa-glx \
#       libhdf5-dev \
#       openmpi-bin \
#       wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install ml lib
RUN pip3 install --ignore-installed blinker
RUN pip3 install --no-cache-dir \
    flask \
    pandas \
    "numpy<1.26" \
    pillow \
    requests \
    flask_cors

# copy code
COPY ./ /image-eval

# make donwload dir
RUN mkdir /image-eval/src/images/

EXPOSE 80

WORKDIR /image-eval
ENTRYPOINT python3 ./src/server.py 
