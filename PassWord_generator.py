import random
from tkinter import *
from tkinter import messagebox

root = Tk()

v = StringVar()
generatedPass = Entry(root, width=16, textvariable=v,justify='center')
generatedPass.place(x=25, y=80)

passLenght = Label(root, text=("Enter the length of the password"))
passLenght.place(x=1, y=1)

lenght_of_thePass = Entry(root, width=5)
lenght_of_thePass.place(x=35, y=20)

Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowercase = "abcdefghijklmnopqrstuvwxyz"
Digits = "0123456789"
Symbols = "()!?*+=_-"

var = StringVar()
var.set("HARD") # initial value

option = OptionMenu(root, var, "HARD", "NORMAL", "EAZY")
option.place(x=95,y=22)

def chech():
    #HARD
    hardMixedbag = Uppercase + Lowercase + Digits + Symbols
    #NORMAL
    normalMixedbag = Uppercase + Lowercase + Digits
    #EAZY
    eazyMixedbag = Lowercase + Digits
    if var.get() == "HARD":
        return hardMixedbag
    elif var.get() == "NORMAL":
        return normalMixedbag
    else:
        return eazyMixedbag

def generate():
    while True:
        word_length = lenght_of_thePass.get()

        if word_length == "":
            messagebox.showwarning("Something missing", "Enter the lenght of the password!")
            return False
        else:
            wordlength = int(word_length)
            Madeword = ""
            for x in range(wordlength):
                difficulty = chech()
                ch = random.choice(difficulty)
                Madeword = Madeword + ch
            break
    password = str(Madeword)
    v.set(Madeword)
    


generatePassBtn = Button(root, text=("GENERATE PASSWORD"), command=generate)
generatePassBtn.place(x=25, y=55)


windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

def main():
    root.resizable(False,False)
    root.title("Password Generator")
    root.geometry("220x120")
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.mainloop()


if __name__ == '__main__':
    main()