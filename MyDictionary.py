
from tkinter import *
from PyDictionary import PyDictionary
from PIL import Image, ImageTk
# importing the module
from englisttohindi.englisttohindi import EngtoHindi
dic=PyDictionary()

root=Tk()
root.geometry("700x500")
root.minsize(600,400)
root.configure(bg='cadetblue')
def dicti():
    meaning.config(text=dic.meaning(search.get())['Noun'][0])
    antonym.config(text=dic.antonym(search.get()))
    trans = EngtoHindi(str(search.get()))
    res = trans.convert
    result.set(res)
    

f=Frame(root)
f.pack()
Label(text="Skarsh Dictionary",font="constantia 24 ",fg="#299180").pack(pady=18)

f1=Frame(root)
f1.pack()
search=Entry(f1,font="constantia 19")
search.pack(side=LEFT,padx=20)
Button(f1,text="Search",font="constantia 14",relief=GROOVE,command=dicti).pack(padx=3,pady=6)
f2=Frame(root)
f2.pack(pady=12)
Label(f2,text="Meaning:-",font="timesnewroman 14 bold",fg="white",bg="#1c7569",borderwidth=1,relief=SUNKEN).pack(side=LEFT,fill=BOTH)
meaning = Label(f2, text="", font="timesnewroman 11")
meaning.pack()
f4=Frame(root)
f4.pack(pady=12)
Label(f4,text="Meaning in hindi:-",font="timesnewroman 14 bold",fg="white",bg="#1c7569",borderwidth=1,relief=SUNKEN).pack(side=LEFT)
Inhindi= Label(f4,text="",font="timesnewroman 20")
result=StringVar()
Label(f4, text="", textvariable=result,bg = "light grey",font="timesnewroman 21").pack(padx=12)

f3 = Frame(root)
f3.pack(pady=12)
Label(f3, text="Antonym:- ", font="timesnewroman 14 bold",fg="white",bg="#1c7569",borderwidth=1,relief=SUNKEN).pack(side=LEFT,fill=BOTH)
antonym = Label(f3, text=" ", font="timesnewroman 13")
antonym.pack()





  

root.mainloop()


'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
import requests

root = Tk()

e = 3
count = 0
nw = 0
c = 5
pad = 10

root.title("Dictonary")

def error():
    # global e
    # error = Label(root,text="Couldnt find any defination for the given word- X {}".format(str(e-2)))
    # error.grid(row=3,column=0,columnspan=3)
    # e += 1
    messagebox.showerror("Error","Couldnt find any defination for the given word")

def search():
    global nw
    global c
    global count
    global pad
    word = input.get()

    if(nw==3):
        c += 3
        count = 0
        pad = 0

    if(nw>5):
        r.set(1)
        Radiobutton(root,text="Same window",variable=r,state=DISABLED).grid(row=1,column=2)

    if r.get() == 1:
        try:
            
            response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
            json_data = json.loads(response.text)
            try:
                json_data = json_data[1]

            except:
                json_data = json_data[0]

            subroot1 = Tk()
            subroot1.title(word)

            meanings = json_data['meanings'][0]
            pos= meanings['partOfSpeech']
            defin = meanings['definitions'][0]
            defination = defin['definition']

            word1 = Label(subroot1,text="WORD: {}".format(json_data['word']),wraplength=500)
            phonetic = Label(subroot1,text="PHONETIC: {}".format(json_data['phonetic']),wraplength=500)
            origin = Label(subroot1,text="ORIGIN: {}".format(json_data['origin']),wraplength=500)
            posi = Label(subroot1,text="PART OF SPEECH: {}".format(pos),wraplength=500)
            defina = Label(subroot1,text="DEFINATION: {}".format(defination),wraplength=500)

            word1.grid(row=0,column=3)
            phonetic.grid(row=1,column=3)
            origin.grid(row=2,column=3)
            posi.grid(row=3,column=3)
            defina.grid(row=4,column=3)

        except:
            error()

    else:
        try:
            
            subroot1 = LabelFrame(root,padx=10,pady=10)
            response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
            json_data = json.loads(response.text)
            try:
                json_data = json_data[1]

            except:
                json_data = json_data[0]

            meanings = json_data['meanings'][0]
            pos= meanings['partOfSpeech']
            defin = meanings['definitions'][0]
            defination = defin['definition']

            word1 = Label(subroot1,text="WORD: {}".format(json_data['word']),wraplength=500)
            phonetic = Label(subroot1,text="PHONETIC: {}".format(json_data['phonetic']),wraplength=500)
            origin = Label(subroot1,text="ORIGIN: {}".format(json_data['origin']),wraplength=500)
            posi = Label(subroot1,text="PART OF SPEECH: {}".format(pos),wraplength=500)
            defina = Label(subroot1,text="DEFINATION: {}".format(defination),wraplength=500)

        

            subroot1.grid(row=count,column=c,rowspan=3,columnspan=3,padx=0)
            word1.grid(row=0,column=3)
            phonetic.grid(row=1,column=3)
            origin.grid(row=2,column=3)
            posi.grid(row=3,column=3)
            defina.grid(row=4,column=3)
            count += 3
            nw += 1
        

        except:
            error()
        


# {'word': 'hello', 'phonetic': 'həˈləʊ', 'phonetics': [{'text': 'həˈləʊ', 'audio': '//ssl.gstatic.com/dictionary/static/sounds/20200429/hello--_gb_1.mp3'}, {'text': 'hɛˈləʊ'}], 'origin': 'early 19th century: variant of earlier hollo ; related to holla.', 'meanings': [{'partOfSpeech': 'exclamation', 'definitions': [{'definition': 'used as a greeting or to begin a phone conversation.', 'example': 'hello there, Katie!', 'synonyms': [], 'antonyms': []}]}, {'partOfSpeech': 'noun', 'definitions': [{'definition': 'an utterance of ‘hello’; a greeting.', 'example': 'she was getting polite nods and hellos from people', 'synonyms': [], 'antonyms': []}]}, {'partOfSpeech': 'verb', 'definitions': [{'definition': 'say or shout ‘hello’.', 'example': 'I pressed the phone button and helloed', 'synonyms': [], 'antonyms': []}]}]}]

r = IntVar()
r.set(1)
label = Label(root,text="Enter a word")
input = Entry(root,width=20,borderwidth=5,fg="white",bg="black")
searchButton = Button(root,text="Search",width=30,command=search)

# bar = Scrollbar(root,orient=VERTICAL)
# bar.grid(row=0,column=7,sticky=NS)

Radiobutton(root,text="New window",variable=r,value=1).grid(row=1,column=1)
Radiobutton(root,text="Same window",variable=r,value=0).grid(row=1,column=2)
label.grid(row=0,column=0)
input.grid(row=0,column=1,columnspan=2)
searchButton.grid(row=2,column=0,columnspan=3)



root.mainloop()

'''