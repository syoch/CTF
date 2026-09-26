#!/usr/bin/env bash

set -e

sudo losetup -d $DRIVE || true

IMAGE=`dirname $0`/disk.img
DRIVE=`sudo losetup -f $IMAGE -P --show`

mkdir mnt
sudo mount ${DRIVE}p3 mnt
