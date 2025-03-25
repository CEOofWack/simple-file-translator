from deep_translator import GoogleTranslator
from deep_translator.exceptions import *
import ctk 
from ctk import *
import time
from supportedlangs import *

def translate():
    
    

    lang = ctk.entry.get()
    lang = str(lang)
    lang = lang.lower()
    
    
    if lang not in supported_langs:
        print(f"Error: {lang} is not a supported language")
       
   
    
    try:
        file1 = open('translate.txt', 'r')
        file1_text = file1.read()
        translate = GoogleTranslator(source = 'auto', target = lang).translate(file1_text)
        file1.close()
            
    except LanguageNotSupportedException:
        ctk.label1.configure(text='Error, language not supported')
        time.sleep(2)
        ctk.label1.configure(text='') 
        return
    
    except NotValidPayload:
        ctk.label1.configure(text='Error, language not supported')
        time.sleep(2)
        ctk.label1.configure(text='') 
        return
    except Exception as e:
        print(f"Error: {e}") 
        return
    
   
        
    
    translated = open('translated.txt', 'w')
    translated.write(translate)
    translated.close()
    
    