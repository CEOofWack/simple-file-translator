from customtkinter import *
from translator import translate
import time


    


def ctkrender():
    global lang, label1, label2, entry, title

    app = CTk()
    app.title('CS2')
    app.geometry('1400x700')
    app._set_appearance_mode('light')



    title = CTkLabel(app, text = 'CRAZYTranslator', font = ('papyrus', 25), text_color='black', bg_color='#EBEBEA')
    
    label1 = CTkLabel(app, text = '', font = ('papyrus', 25), text_color='RED', bg_color='#EBEBEA')
    label2 = CTkLabel(app, text = 'Enter language here ↓↓↓↓', font = ('papyrus', 25), text_color='RED', bg_color='#EBEBEA')
    entry = CTkEntry(app, font = ('papyrus', 20), text_color='magenta', corner_radius=32, bg_color='#EBEBEA')


    entry.bind("<Return>", lambda event: translate())

    
    title.pack()
    label1.pack()
    label2.pack()
    entry.pack()
   

    app.mainloop()


