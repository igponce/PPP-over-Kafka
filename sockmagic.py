#!/usr/bin/env pyhton
#
# Send stdin to port 9999/tcp, read stdout from 

from __future__ import print_function
import os
import sys
# from pyyaml import read, dump
from confluent-kafka import Producer, Consumer

# Setup

print("Forking:\nPort 9999 is stdout (what you type),\nPort 8888 is stdin (whay you see here)")

pid = os.fork()

if pid == 0 :
   # child process
   sys.stdout.close()
   # Start netcat on port 9999      
   os.execv("/bin/nc", ['nc', '-l', '-p', '9999'])

else :
   # parent process
   sys.stdin.close()
   # Startigpon kafka-console-consumer
   os.execv("/bin/nc", ['nc', '-l', '-p', '8888'])

print ("Program terminated - both stdin and stdout are closed")