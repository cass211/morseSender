from morse import MorsePlayer
from tkinter import *
import os
# os.system('clear')

mp = MorsePlayer()

root = Tk()
root.title('mcSoundOutput')
root.geometry('600x400')

mcLabel = Label(root, text="Enter text to xmit in caps 50 chars max:")
mcLabel.pack()

mcTextbox = Entry(root, width=50)
mcTextbox.pack()

mcButton = Button(root, text='Submit', command=mp.play_string('CQ CQ'))
def play_textbox():
    text = mcTextbox.get()
    text = text.upper()
    mp.play_string(text)

mcButton.pack()

root.mainloop()




