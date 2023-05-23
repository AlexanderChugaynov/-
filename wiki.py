import wikipedia
import tkinter as tk


wikipedia.set_lang("ru")

def search():
    query = box.get()
    try:
        result = wikipedia.summary(query)
        text.delete(1.0, tk.END)
        text.insert(tk.END, result)
    except wikipedia.exceptions.DisambiguationError as e:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "Что вы имели ввиду?" + "".join(e.options))

def save():
    query = box.get()
    result = wikipedia.summary(query)
    with open(query + ".txt", "w", encoding="utf-8") as f:
        f.write(result)

def random_article():
    query = wikipedia.random()
    result = wikipedia.summary(query)
    text.delete(1.0, tk.END)
    text.insert(tk.END, result)

w = tk.Tk()
w.title("Википедия")

head = tk.Frame(w)
write = tk.Frame(w)
res = tk.Frame(w)
category = tk.Frame(w)

tk.Label(head, text="Википедия", font=("Times", 30, "")).pack(side=tk.TOP)

tk.Label(write, text="Поиск", font=("Times", 20)).pack(side=tk.LEFT)
box = tk.Entry(write, width=40, font=("Times", 20))
box.pack(side=tk.LEFT, fill=tk.BOTH, expand=6)
box.focus_set()

button1 = tk.Button(write, text="Искать", command=search, font=("Times", 15), bg="orange", fg="white")
button1.pack(side=tk.RIGHT)

button2 = tk.Button(write, text="Случайная статья", command=random_article, font=("Times", 15), bg="orange", fg="white")
button2.pack(side=tk.RIGHT)


button3 = tk.Button(write, text="Сохранить в txt", command=save, font=("Times", 15), bg="orange", fg="white")
button3.pack(side=tk.RIGHT)



text = tk.Text(w, font=("Times", 18), bg="lightblue", padx=55, pady=10)

tk.Label(res, text="Результаты поиска: ", font=("Times", 25)).pack(side=tk.LEFT)
head.pack()
write.pack(side=tk.TOP)
res.pack(side=tk.TOP, pady=30, padx=60)
text.pack()

w.mainloop()
