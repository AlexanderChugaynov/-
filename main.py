import wikipedia
from tkinter import *
wikipedia.set_lang("ru")


w = Tk()
w.title("Википедия")
w.config()

head=Frame(w)
write = Frame(w)
res = Frame(w)

Label(head, text="Википедия",font=("Times",30,"")).pack(side=TOP)
Label(write,text="Поиск",font=("Times",20)).pack(side=LEFT)

Label(res,text="Результаты поиска: ",font=("Times",25)).pack(side=LEFT)
box = Entry(write,width=40,font=("Times",20))
box.pack(side=LEFT,fill=BOTH,expand=6)
box.focus_set()

qr=""
text=Text(w,font=("Times",18),bg="lightblue",padx=55,pady=10)

def result():
    global qr
    qr = box.get()
    try:
        txt = wikipedia.summary(qr, auto_suggest=False)
        text.insert("1.0",txt)
    except:
        text.insert("1.0","Ничего не найдено")

button1 = Button(write,text="Искать",command=result,font=("Times",25),bg="orange",fg="white")
button1.pack(side=RIGHT)
head.pack()

write.pack(side=TOP)
res.pack(side=TOP,pady=30,padx=60)
text.pack()
w.mainloop()
