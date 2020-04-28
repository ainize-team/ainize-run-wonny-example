#!/bin/bash

echo "[<Docker url>] Docker tag (ex 1.0.0): "
  read tag
  docker build -t <Docker url>:${tag} .
  docker push <Docker url>:${tag}
