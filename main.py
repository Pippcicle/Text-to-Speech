from tkinter import *
from gtts import gTTS
import os

root = Tk()
root.configure(background = "#B8E1FF")
root.title("Text-to-Speech Converter")
root.geometry('650x550+350+200')

heading = Label(root, text = 'Text-to-Speech Convertor', bg = "#B8E1FF", fg = "#82ABA1", font = ('arial',35,'bold'))
heading.pack()

entry = Entry(root, width = 45, bd = 4, font = 15 )
entry.pack(pady = 30)

entry.insert(0, "")

def convert(): 
    language = 'en'
    my_text = gTTS(text = entry.get(), lang = language, slow = False)
    my_text.save("audio.wav")
    os.system("audio.wav")

submit_btn = Button(root, text = "Submit", font = ('arial', 20, 'bold'), bg = '#517664', fg = '#9FD8CB', width = 15, command = convert)
submit_btn.pack(pady = 30)

root.mainloop()