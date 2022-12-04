from tkinter import *
import random
import pyttsx3
from threading import Thread
from pynput import keyboard

items = dict()
maxVal = 5000


def speak():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 200)
    while True:
        engine.say("youre an idiot lol hahaha")
        engine.runAndWait()


def tell():
    Thread(target=speak).start()


def logged():
    global root, bgIMG, bgCanvas, maxVal
    tell()
    colours = ['blue', 'green', 'red', 'yellow', 'orange', 'violet', 'indigo']
    root = dict()
    bgIMG = dict()
    bgCanvas = dict()
    main = Tk()
    main.withdraw()
    for i in range(maxVal):
        x = random.randint(-20, 1000)
        y = random.randint(0, 600)
        root[i] = Toplevel(main)
        bgIMG[i] = PhotoImage(file='log.png')
        bgCanvas[i] = Canvas(root[i], width=400, height=200)
        bgCanvas[i].pack()
        bgCanvas[i].create_image(0, 0, image=bgIMG[i], anchor='nw')
        root[i].overrideredirect(True)
        root[i].geometry(f'400x200+{str(x)}+{str(y)}')
        root[i].attributes('-topmost', 1)
        root[i].resizable(0, 0)
        """ label = Label(root, text='hello world')
        label.pack() """
        root[i].update()
    for i in range(maxVal):
        root[i].mainloop()


def onHotKey():
    quit()


def onPress(f):
    return lambda k: f(l.canonical(k))


item = Thread(target=logged)
item.daemon = True
item.start()


def hotk():
    global l
    hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+c'), onHotKey)
    with keyboard.Listener(on_press=onPress(hotkey.press), on_release=onPress(hotkey.release)) as l:
        l.join()


Thread(target=hotk).start()
