# youranidiotinpython
Remake of the Youranidiot virus in python with a safety feature.

This project uses the following modules:
  tkinter
  random
  pyttsx3
  threading
  pynput
  
The app first starts a thread that creates 'maxVal' number of tkinter toplevels that contain an image called log.png. #maxVal is an integer variable
It also uses pyttsx3 to say 'your an idiot lol hahaha' in an infinite while loop.

python 3.12 breaks this program, so it is advised to run on python 3.11 or lower.

As a safety precaution the project uses pynput to check for a hotkey that closes the entire program.

Note: The hotkey is 'CTRL + C'
