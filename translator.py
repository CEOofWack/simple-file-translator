# Import necessary libraries
from deep_translator import GoogleTranslator
from deep_translator.exceptions import *
import ctk 
from ctk import *
import time
from supportedlangs import *

# Function where translation and file handing is done

def translate():

    # Gets input from Custom Tkinter entry and stores in variable lang

    lang = ctk.entry.get()
    lang = str(lang)
    lang = lang.lower()
    
    # Checks if string returned is a language code i.e english = "en"

    if lang not in supported_langs:
        print(f"Error: {lang} is not a supported language")
       
    # Error handling for tranlation issues with deep_translator library, with all other Errors taken into account

    try:
        file1 = open('translate.txt', 'r')
        file1_text = file1.read()
        translate = GoogleTranslator(source= 'auto', target = lang).translate(file1_text)
        file1.close()
            
    except LanguageNotSupportedException:
        ctk.label1.configure(text='Error, language not supported')
        time.sleep(2)
        ctk.label1.configure(text='') 
        return
    
    except NotValidPayload:
        ctk.label1.configure(text='Error, origin file contains invalid payload')
        time.sleep(2)
        ctk.label1.configure(text='') 
        return
    except Exception as e:
        print(f"Error: {e}") 
        return
    
   
    # Opens target file and writes translated text of origin file, the closes it

    translated = open('translated.txt', 'w')
    translated.write(translate)
    
    translated.close()

    
    