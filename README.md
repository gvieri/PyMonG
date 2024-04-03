# PyMonG
Python Monitor In GPG

It is a simple script, written in python 3 that use the monitoring commands available on linux to obtain the desired info about your computer system status. 
This script will collect the output from commands as df -k and so on then it will encrypt by using gpg and at last it will print the encoded message on stedout. 

So it will be used in script that will send the encoded message by email, mqtt, other messenger and so on. 

Example:

python prova.monitor.py -h 
usage: prova.monitor.py [-h] [-v] [-a] [-k]

This simple program will help you to write an encrypted monitor about a server
status. The resulting string is printed on stdout and can be sent via mqtt or
smtp, etc..

options:
  -h, --help     show this help message and exit
  -v, --verbose  more verbose output
  -a, --archive  archive report in files in ~./repo_path
  -k, --key      choose gpg key to use


while true\ndo \necho `date`\nsleep 60 \ndone | python -u pymong.py -k mygpgpkey@example.com | mosquitto_pub -h public.mqtthq.com -t myownserver0000 -l 

The above command il a a way to monitor a server and then send the encrypted data via mqtt... Please substitute your own key to the the dummy key after -k option ... 

