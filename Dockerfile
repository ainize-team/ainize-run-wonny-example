FROM tensorflow/tensorflow:1.13.1-gpu-py3

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
RUN pip3 install flask 
RUN pip3 install pandas 
RUN pip3 install keras==2.1.3
RUN pip3 install "numpy<1.17"
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
