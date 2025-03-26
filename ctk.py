# Import necessary libraries
from customtkinter import *
from translator import *



# Function to handle rendering od Cutsom Tkinter and its elemnts 

def ctkrender():
    global lang, label1, label2, entry, title

    # Custom Tkinter window parameters    

    app = CTk()
    app.title('CS2')
    app.geometry('700x700')
    app._set_appearance_mode('light')


    # Initialize all labels and entry point along with parameters 

    title = CTkLabel(app, text = 'CRAZYTranslator', font = ('papyrus', 25), text_color='black', bg_color='#EBEBEA')
    label1 = CTkLabel(app, text = '', font = ('papyrus', 25), text_color='RED', bg_color='#EBEBEA')
    label2 = CTkLabel(app, text = 'Enter language here ↓↓↓↓', font = ('papyrus', 25), text_color='RED', bg_color='#EBEBEA')
    entry = CTkEntry(app, font = ('papyrus', 20), text_color='magenta', corner_radius=32, bg_color='#EBEBEA')

    # Gets output from entry in tkinter when return key is pressed and passes it to the translate function

    entry.bind("<Return>", lambda event: translate())

    # Pack all widgets to Custom Tkinter window

    title.pack()
    label1.pack()
    label2.pack()
    entry.pack()

    # Main Tkinter loop

    app.mainloop()


