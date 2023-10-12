FROM python:3.10-slim

ENV SHELL /bin/bash

# Install system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
      apt-transport-https \
      bzip2 \
      g++ \
      git \
      graphviz \
      libgl1-mesa-glx \
      libhdf5-dev \
      openmpi-bin \
      wget && \
    rm -rf /var/lib/apt/lists/*

# Install ML lib
RUN pip3 install "tensorflow[and-cuda]"
RUN python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
RUN pip3 install flask
RUN pip3 install pandas 
RUN pip3 install "numpy<1.26"
RUN pip3 install pillow
RUN pip3 install requests
RUN pip3 install flask_cors

# Copy code.
RUN mkdir /image-eval
ADD ./ /image-eval

# make donwload dir
RUN mkdir /image-eval/src/images/

EXPOSE 80

WORKDIR /image-eval
ENTRYPOINT python3 ./src/server.py 
