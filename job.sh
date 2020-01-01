#!/bin/sh
# Job à lancer en debug pour tester le server local SMTP

trap "kill 0" EXIT

python -m smtpd -c DebuggingServer -n localhost:1025 &
python "main.py" &

wait

