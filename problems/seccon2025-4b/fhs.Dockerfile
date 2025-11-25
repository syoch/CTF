FROM ubuntu:24.04

RUN apt update && apt install -y \
  gdb gdbserver \
  python3 \
  python3-pip \
  wget \
  curl \
  vim \
  git

