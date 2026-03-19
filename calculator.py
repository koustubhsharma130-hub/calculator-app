from tkinter import *
def press(num):
        e.insert(END,str(num))  
def clear():
        e.delete(0,END)
def close():
        th.destroy()             
def ans():
    try:
        result = eval(e.get()) 
        e.delete(0, END)
        e.insert(0, result)
    except Exception:
        e.delete(0, END)
        e.insert(0, "Error")



th=Tk()
th.title("CALCULATOR")
th.config(bg='green')
th.geometry("500x600+500+300")
e=Entry(th,width=50)
e.grid(row=0, columnspan=4, pady=5, ipady=30)

num = 1
for r in range(1,4):
    for c in range(3):
        b=Button(th,text=num,width=10,height=5,command=lambda n=num: press(n))
        b.grid(row=r,column=c)
        b.bind("<Enter>",lambda e:e.widget.config(bg="yellow"))
        b.bind("<Leave>",lambda e:e.widget.config(bg="white"))  
        num += 1

b0=Button(th,text="0",width=10,height=5,command=lambda: press(0))
b0.bind("<Enter>",lambda e:e.widget.config(bg="yellow"))
b0.bind("<Leave>",lambda e:e.widget.config(bg="white"))
b0.grid(row=4,column=0)

ba=Button(th,text="+",width=10,height=5,command=lambda: e.insert(END,"+"))
ba.bind("<Enter>",lambda e:e.widget.config(bg="indigo")) 
ba.bind("<Leave>",lambda e:e.widget.config(bg="white"))
ba.grid(row=1,column=3)
  
bs=Button(th,text="-",width=10,height=5,command=lambda: e.insert(END,"-"))
bs.bind("<Enter>",lambda e:e.widget.config(bg="indigo")) 
bs.bind("<Leave>",lambda e:e.widget.config(bg="white"))
bs.grid(row=2,column=3)

bm=Button(th,text="*",width=10,height=5,command=lambda: e.insert(END,"*"))
bm.bind("<Enter>",lambda e:e.widget.config(bg="indigo")) 
bm.bind("<Leave>",lambda e:e.widget.config(bg="white"))
bm.grid(row=3,column=3)
  
bd=Button(th,text="/",width=10,height=5,command=lambda: e.insert(END,"/"))
bd.bind("<Enter>",lambda e:e.widget.config(bg="indigo")) 
bd.bind("<Leave>",lambda e:e.widget.config(bg="white"))
bd.grid(row=4,column=3)
     
be=Button(th,text="=",width=22,height=5,command=ans)
be.bind("<Enter>",lambda e:e.widget.config(bg="purple"))
be.bind("<Leave>",lambda e:e.widget.config(bg="white"))
be.grid(row=4,column=1,columnspan=2)

bc=Button(th,text="   clear   ",command=clear)
bc.bind("<Enter>",lambda e:e.widget.config(bg="orange"))
bc.bind("<Leave>",lambda e:e.widget.config(bg="white"))
bc.grid(row=5,column=0,columnspan=2,pady=10)

ex=Button(th,text="   exit    ",command=close)
ex.bind("<Enter>",lambda e:e.widget.config(bg="red"))
ex.bind("<Leave>",lambda e:e.widget.config(bg="white"))
ex.grid(row=5,column=2,columnspan=2,pady=10)

th.mainloop()