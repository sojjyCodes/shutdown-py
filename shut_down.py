import os
import pyttsx3

user = input("Dou you want to shut down this system (Y/N): ")

if user == 'N':
    exit()

else:
    pyttsx3.speak("Shutting, down")
    os.system("poweroff")
