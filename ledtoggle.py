from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware

green = LED(27)
red = LED(22)
blue = LED(17)

win = Tk()
win.title("LED Toggler")
myfont = tkinter.font.Font(family = "helvetica", size = 12, weight = "bold")

def greenToggle():
    red.off()
    green.on()
    blue.off()

def redToggle():
    red.on()
    green.off()
    blue.off()

def blueToggle():
    red.off()
    green.off()
    blue.on()

def quitwin():
    red.off()
    green.off()
    blue.off()
    win.destroy()

ledbutton = Radiobutton(win, text = "Green LED on", font = myfont, command = lambda: greenToggle(), value = 0, bg = "bisque2", height = 1, width = 24)
ledbutton.grid(row=0,column=1)

redbutton = Radiobutton(win, text = "Red LED", font = myfont, command = lambda: redToggle(), value = 1, bg = "bisque2", height = 1, width = 24)
redbutton.grid(row=1,column=1)

bluebutton = Radiobutton(win, text = "Blue LED on", font = myfont, command = lambda: blueToggle(), value = 3, bg = "bisque2", height = 1, width = 24)
bluebutton.grid(row=2,column=1)

offbutton = Button(win, text = "Quit", font = myfont, command = lambda: quitwin(), bg = "bisque2", height = 1, width = 24)
offbutton.grid(row=3,column=1)




