#!/usr/bin/env python

import sys,os,time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#shut off warning messages
GPIO.setwarnings(False)
#set pin 27 to OUTPUT, this pin triggers the SOLID STATE RELAY
GPIO.setup(27,GPIO.OUT)
#set pin 22 to INPUT, this pin is connected to MOTION DETECTOR
GPIO.setup(22,GPIO.IN)
#set pin 16 to OUTPUT, this pin controls pin 18
GPIO.setup(16,GPIO.OUT)
#set pin 18 to INPUT, if pin HIGH alarm is OFF, and vice versa
GPIO.setup(18,GPIO.IN)


while True:                       #set up endless loop
 if not(GPIO.input(18)):          #if ALARM is ON (Pin 18 LOW)
   if not (GPIO.input(22)):       #if MOTION DETECTED
           GPIO.output(27,True)   #turn on SOLID STATE RELAY
           for i in range(8):     #take 8X5= 40 pictures
               if not(GPIO.input(18)): #if ALARM ON Take Pics else don't            
                 # takes 8X5=40 pics at 640X480 resolution
                 # where 8 is in range(8) and take_pics takes 5 pics
                 os.system("sudo /home/pi/take_pics")
           if not(GPIO.input(18)):#if ALARM is on then send SMS    
	     os.system("sudo /home/pi/send_sms")
   if (GPIO.input(22)): # if ALARM is OFF (Pin 18 HIGH)
         GPIO.output(27,False)  # shut OFF SOLID STATE RELAY
 if(GPIO.input(18)):    # if MOTION NOT DETECTED shut OFF SOLID STATE RELAY
   GPIO.output(27,False)           
GPIO.cleanup()
