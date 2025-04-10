from tkinter import *
from gtts import gTTS
import os

root = Tk()
root.configure(background = '#C880B7')
root.title("What food do you like ? ")
root.geometry('450x350')

heading = Label(root, text = "Favourite Food", font = ('arial', 35, 'bold'), bg = '#C880B7', fg = '#4A2040')
heading.pack()

entry = Entry(root, width = 45, bd = 4, font = 15 )
entry.pack(pady = 30)

entry.insert(0, "")

def convert(): 
    language = 'en'
    my_text = gTTS(text = "I like to eat" + entry.get(), lang = language, slow = False)
    my_text.save("audio.wav")
    os.system("audio.wav")

submit_btn = Button(root, text = "Submit", font = ('arial', 20, 'bold'), bg = '#9F6BA0', fg = '#4A2040', width = 15, command = convert)
submit_btn.pack(pady = 30)

root.mainloop()