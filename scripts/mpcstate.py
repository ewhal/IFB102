#!/usr/bin/python
#@reboot /path/to/mpcstate.py
import RPi.GPIO as GPIO
from time import sleep 
from os import system


state = True
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    start_state = GPIO.input(18)
    stop_state = GPIO.input(21)
    prev_state = GPIO.input(16)
    next_state = GPIO.input(12)
    volume_down_state = GPIO.input(24)
    volume_up_state = GPIO.input(4)
    ip = GPIO.input(23)

    if prev_state == False:
	print "16"
        system("mpc prev")
    	sleep(0.2)
    if next_state == False:
	print "12"
        system("mpc next")
    	sleep(0.2)
    if volume_down_state == False:
	print "24"
        system("mpc volume -10")
    if volume_up_state == False:
	print "4"
        system("mpc volume +10")
    if ip == False:
	print "23"
	system("python /root/ip.py")
    	sleep(0.2)



    if stop_state == False:
	print "21"
    	system("mpc stop")

    if start_state == False:
	print "18"
	system("mpc play")

