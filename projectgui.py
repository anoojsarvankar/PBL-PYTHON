from tkinter import*
from tkinter import messagebox



root = Tk()

root.geometry("1200x800")
root.title("K B C")



f1=Frame(root,bg='black')

# def exit():
#     exit(0)

def start():



    f1=Frame(root, bg='black')
    f1.pack(side=TOP, expand=YES, fill=BOTH)
    l = Label(f1, text='Your Question', bg='black', fg='white')
    l.pack(side=TOP, expand=YES, fill=BOTH)

    var1 = IntVar()
    var2 = IntVar()
    f1 = Frame(root, bg='black')
    f1.pack(side=TOP, expand=YES, fill=BOTH)

    r1 = Checkbutton(f1, text='1', bg='black', fg='white')
    r1.pack(side=LEFT, expand=YES, fill=BOTH)

    r2 = Checkbutton(f1, text='2', bg='black', fg='white')
    r2.pack(side=LEFT, expand=YES, fill=BOTH)

    var3 = IntVar()
    var4 = IntVar()
    f1 = Frame(root, bg='black')
    f1.pack(side=TOP, expand=YES, fill=BOTH)

    r3 = Checkbutton(f1, text='3', bg='black', fg='white')
    r3.pack(side=LEFT, expand=YES, fill=BOTH)

    r4 = Checkbutton(f1, text='4', bg='black', fg='white')
    r4.pack(side=LEFT, expand=YES, fill=BOTH)

    f1 = Frame(root, bg='black')
    f1.pack(side=TOP, expand=YES, fill=BOTH)
    b = Button(f1, text="Submit", bg='gray', fg='black')
    b.pack(side=LEFT, expand=YES)
    l = Label(f1, text='Answer is ', bg='black', fg='white')
    l.pack(side=LEFT, expand=YES, fill=BOTH)

    f1 = Frame(root, bg='black')
    f1.pack(side=TOP, expand=YES, fill=BOTH)
    b = Button(f1, text="Cancel game", bg='gray', fg='black',command=exit)
    b.pack(side=LEFT, expand=YES)



def main():
    f1 = Frame(root, bg='black')
    f1.pack(side=TOP, expand=YES)
    l=Label(f1, text='A P SHAH', bg='black', fg='white')
    l.pack(side=LEFT, expand=YES)

    f1.pack(side=TOP, expand=YES, fill=BOTH)
    l=Label(f1, text='K B C', bg='black', fg='white')
    l.pack(side=LEFT, expand=YES)


    f1.pack(side=TOP, expand=YES, fill=BOTH)
    b = Button(f1, text ="START",bg='gray', fg='black',command =start)
    b.pack(side=LEFT, expand=YES)

main()

root.mainloop()
