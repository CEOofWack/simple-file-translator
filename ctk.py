from customtkinter import *
from deep_translator import GoogleTranslator , exceptions

def translate():
    file1 = open('translate.txt', 'r')
    text = file1.read()
    try:
        translate = GoogleTranslator(source = 'auto', target = lang).translate(text)
    except exceptions.LanguageNotSupportedException:
        label1.configure(text='Error, language not supported')  
    
    translated = open('translated.txt', 'w')
    translated.write(translate)
    translated.close()
    file1.close()
    
    


def ctkrender():
    global lang, label1, entry

    app = CTk()
    app.title('CS2')
    app.geometry('1400x700')
    app._set_appearance_mode('light')



    title = CTkLabel(app, text = 'CRAZYTranslator', font = ('papyrus', 25), text_color='black', bg_color='#EBEBEA')
    
    label1 = CTkLabel(app, text = '', font = ('papyrus', 25), text_color='RED', bg_color='#EBEBEA')
    label2 = CTkLabel(app, text = 'Enter language here ↓↓↓↓', font = ('papyrus', 25), text_color='RED', bg_color='#EBEBEA')
    entry = CTkEntry(app, font = ('papyrus', 20), text_color='magenta', corner_radius=32, bg_color='#EBEBEA')

    global lang 
    lang = entry.get()
    lang = str(lang)
    

    entry.bind("<Return>", lambda event: translate())

    
    title.pack()
    label1.pack()
    label2.pack()
    entry.pack()
   

    app.mainloop()


