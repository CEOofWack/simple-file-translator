from deep_translator import GoogleTranslator, exceptions 
import ctk
import time

def translate():

    lang = ctk.entry.get()
    lang = str(lang)
    
    
    try:
        file1 = open('translate.txt', 'r')
        text = file1.read()
        translate = GoogleTranslator(source = 'auto', target = lang).translate(text)
    except exceptions.LanguageNotSupportedException:
        ctk.label1.configure(text='Error, language not supported') 
        time.sleep(3)
        ctk.label1.configure(text='') 
  
    except Exception as e:
        print(f"Error: {e}") 
    
    translated = open('translated.txt', 'w')
    translated.write(translate)
    translated.close()
    file1.close()
    