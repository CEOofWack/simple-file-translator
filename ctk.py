from customtkinter import *
from translator import *





def ctkrender():
    global lang, label1, label2, entry, title

    file_1 = open('translate.txt', 'r')
    text_1= file_1.read()
    file_1.close()



    app = CTk()
    app.title('CS2')
    app.geometry('1400x700')
    app._set_appearance_mode('light')



    title = CTkLabel(app, text = 'CRAZYTranslator', font = ('papyrus', 25), text_color='black', bg_color='#EBEBEA')
    
    label1 = CTkLabel(app, text = '', font = ('papyrus', 25), text_color='RED', bg_color='#EBEBEA')
    label2 = CTkLabel(app, text = 'Enter language here ↓↓↓↓', font = ('papyrus', 25), text_color='RED', bg_color='#EBEBEA')
    entry = CTkEntry(app, font = ('papyrus', 20), text_color='magenta', corner_radius=32, bg_color='#EBEBEA')

    file1_label = CTkLabel(app, text = text_1, font = ('papyrus', 20), text_color='black', corner_radius=32, bg_color='#EBEBEA')
    file1_label.place(relx = 1.0, rely = 0.5, anchor = "e")


    entry.bind("<Return>", lambda event: translate())

    
    title.pack()
    label1.pack()
    label2.pack()
    entry.pack()

    file1_label.pack()
   

    app.mainloop()


