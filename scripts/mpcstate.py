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



while True:
    start_state = GPIO.input(18)
    stop_state = GPIO.input(21)
    prev_state = GPIO.input(16)
    next_state = GPIO.input(12)
    volume_down_state = GPIO.input(24)
    volume_up_state = GPIO.input(4)

    if prev_state == False:
        print "button 16"
        system("mpc prev")
	system("python /root/lcd.py")
        sleep(0.2)
    if next_state == False:
        print "button 12"
        system("mpc next")
	system("python /root/lcd.py")
        sleep(0.2)
    if volume_down_state == False:
        print "button 24"
        system("mpc volume -10")
        sleep(0.2)
    if volume_up_state == False:
        print "button 4"
        system("mpc volume +10")
        sleep(0.2)


    if stop_state == False:
    	print "button 21"
    	state = False
    	system("mpc stop")
    	sleep(0.2)

    if start_state == False:
    	print "button 18"
    	start = True
	system("mpc play")
	system("python /root/lcd.py")
    	sleep(0.2)

