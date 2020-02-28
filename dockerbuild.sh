#!/bin/bash

echo "[ainblockchain/evaluate-image] Docker tag (ex 1.0.0): "
  read tag
  docker build -t ainblockchain/evaluate-image:${tag} .
  docker push ainblockchain/evaluate-image:${tag}
