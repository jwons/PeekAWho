from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
import socket
from tkinter import *

from WinNote import *


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## For this demonstration we are just communicating with ourself. Later we will make an app to communicate with the Microcontroller
server = '0.0.0.0'
## Already checked that this port is not in use. In order to make sure you can open up command prompt and type ' netstat -aon '. The last number in localhost column (xx:xx:xx:135) is a port being used   
port = 10000

server_address = (server, port)
sock.bind(server_address)

sock.listen(1)

## This was created because without it the message will be multiplined. We 'append' this string
stringVariable = ''

## This was made in order to break the loop. It was an infinite loop so this breaks it
connecting = True





'''
def guiNotification():
    root = Tk()
    var = StringVar()

    var.set(output)

    ## The width = len(output)*10 sets the width of the message to be 10 pixels wide for each character
    #(I find this through trial and error until I got a single character per line)
    alert = Message(root, textvariable = var, width = (len(output)*10))
    close = Button(root, text = "Close", command = root.quit)
    
    ### PLACEMENT ON GUI
    alert.pack(expand = True)
    close.pack()
    
    root.mainloop()
'''


w = WindowsBalloonTip()

while connecting:
    connection, clinet_address = sock.accept()


    while True:
        data = connection.recv(16)
        if data:
            connection.sendall(data)
            stringVariable+=data.decode() ## This is the 'append' to the string. It takes the latest char sent over and adds it to the message (string)
        else:
            break

    print(stringVariable)
    knockTime = str( time.ctime(int(time.time())))
    output = stringVariable + " (" + knockTime + ")"
    if os.name == 'nt':
        #windowsNotification()
        w.ShowWindow("Door Notification", output)
        stringVariable = ''
        output = ''
    else:
        guiNotification()
    #connection.close()
    #connecting = False # kills the loop
    

