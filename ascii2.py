from tkinter import*

root = Tk()
root.title("ascii")
root.geometry("400x400")

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root,text="ascii:",bg="gold",fg="black")
label.place(relx=0.5, rely=0.5, anchor=CENTER)

def ascii():
    input_word=enter_word.get()
    for letter in input_word:
        label["text"]+=str(ord(letter))+" " 

button = Button(root,text="ascii:",bg="gold",fg="black",command=ascii)
button.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
