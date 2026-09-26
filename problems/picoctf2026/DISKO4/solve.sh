#!/usr/bin/env bash

set -e

sudo losetup -d $DRIVE || true

IMAGE=`dirname $0`/disko-4.dd
DRIVE=`sudo losetup -f $IMAGE -P --show`

mkdir mnt
sudo mount ${DRIVE} mnt
