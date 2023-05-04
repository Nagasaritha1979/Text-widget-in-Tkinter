from tkinter import *

win=Tk()

def clear_text():
    text1.delete(1.0,END)
    label1.config(text='')
    
def get_text():
    name=text1.get(1.0,END)
    label1.config(text=name)
    print(name)
    
def add_text():
    text1.insert(END,"\nAn apple a day keeps the doctor away.")

text1=Text(win,width=80,height=20)
text1.pack(pady=10)

btn_frame=Frame(win)
btn_frame.pack()

btn1=Button(btn_frame, text="Clear" ,command=clear_text)
btn1.pack(side=LEFT)
btn2=Button(btn_frame,text="Submit",command=get_text)
btn2.pack(side=LEFT,padx=10)
btn3=Button(btn_frame,text="Add",command=add_text)
btn3.pack(side=LEFT)

label1=Label(win,text='')
label1.pack()

win.mainloop()
