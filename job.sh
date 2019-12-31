#!/bin/sh

trap "kill 0" EXIT

 # todo remove this might not be useful anymore
 # python -m smtpd -c DebuggingServer -n localhost:1025 &

# start main process

python "C:\Users\User\Desktop\VdmScraperPro\main.py" &

wait

