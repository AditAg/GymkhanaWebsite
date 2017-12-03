import Tkinter
top=Tkinter.Tk()

frame=Tkinter.Frame(top,bg='grey',height=500,width=800)
frame.pack()
frame.grid(row=0,columnspan=3)

var=Tkinter.StringVar()
text=Tkinter.Label(frame,textvariable=var,font=("Hevetica",12),justify='left')
txt='Tkinter Chat...\n'
var.set(txt)
text.pack()

def attch(data):
    global txt
    txt+=data+'\n'
    var.set(txt)
    text.pack()
    
en=Tkinter.Entry(top,width=100,bd=4)
en.pack()

label=Tkinter.Label(top,text='Enter : ',font=("Hevetica",12))
label.pack()

but=Tkinter.Button(top,text='Submit',width=18,command=lambda:attch(en.get()))
but.pack()

label.grid(row=1,column=0)
en.grid(row=1,column=1)
but.grid(row=1,column=2)

top.mainloop()
