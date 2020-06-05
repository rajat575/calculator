from tkinter import *

def click(btnval):
    text = strVar.get()
    if btnval == "=":
        text = str(eval(text))
    elif btnval == "c":
        text = ""
    else:
        text += str(btnval)
    strVar.set(text)
root = Tk()
root.title("Calculator")
root.iconbitmap(r"icon_Wqy_icon.ico")
strVar = StringVar()
strVar.set("")
# ROW 0
Label(root, textvariable=strVar, width=5, height=2).grid(row=0,column=0, columnspan=4)
Button(root, text="C", width=7, height=2, command=lambda: click("c")).grid(row=0, column=3)
# ROW 4
Button(root, text=".", width=7, height=2, command=lambda: click(".")).grid(row=4, column=0)
Button(root, text="0", width=7, height=2, command=lambda: click("0")).grid(row=4, column=1)
Button(root, text="=", width=7, height=2, command=lambda: click("=")).grid(row=4, column=2)
Button(root, text="+", width=7, height=2, command=lambda: click("+")).grid(row=4, column=3)
# ROW 3
Button(root, text="1", width=7, height=2, command=lambda: click("1")).grid(row=3, column=0)
Button(root, text="2", width=7, height=2, command=lambda: click("2")).grid(row=3, column=1)
Button(root, text="3", width=7, height=2, command=lambda: click("3")).grid(row=3, column=2)
Button(root, text="-", width=7, height=2, command=lambda: click("-")).grid(row=3, column=3)
# ROW 2
Button(root, text="4", width=7, height=2, command=lambda: click("4")).grid(row=2, column=0)
Button(root, text="5", width=7, height=2, command=lambda: click("5")).grid(row=2, column=1)
Button(root, text="6", width=7, height=2, command=lambda: click("6")).grid(row=2, column=2)
Button(root, text="/", width=7, height=2, command=lambda: click("/")).grid(row=2, column=3)
# ROW 1
Button(root, text="7", width=7, height=2, command=lambda: click("7")).grid(row=1, column=0)
Button(root, text="8", width=7, height=2, command=lambda: click("8")).grid(row=1, column=1)
Button(root, text="9", width=7, height=2, command=lambda: click("9")).grid(row=1, column=2)
Button(root, text="*", width=7, height=2, command=lambda: click("*")).grid(row=1, column=3)
root.mainloop()
