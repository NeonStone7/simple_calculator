import tkinter as kk
def option(i):
    if i!= '=':
        entry.insert(kk.END,i)
    else:
        expression=entry.get()
        try:
            value=eval(expression)
            new_string=f'{value: ,}'
            entry.delete(0, kk.END)
            entry.insert(0, new_string)
        except Exception as e:
            entry.delete(0, kk.END)
            entry.insert(0,e)
root=kk.Tk()
root.title('Simple Calculator')
entry=kk.Entry(root,width=26,borderwidth=5,font=('arial',12))
entry.grid(row=0,column=0,padx=8,pady=8,columnspan=5)
shape=kk.Frame(root,width=40,height=100)
shape.grid(row=1,columnspan=2)
button_text=['1','2','3','4','5','6','7','8','9','10','-','+','*','/','%','^','=','(',')','//']
i=j=0
for x in button_text:
    b=kk.Button(shape,width=5,text=x,command=lambda x=x: option(x))
    b.grid(row=i,column=j,ipadx=2,ipady=4)
    j+=1
    if j==5:
        i+=1
        j=0
del_btn=kk.Button(root,text='Clear',width=30,command=lambda: entry.delete(0,kk.END))
del_btn.grid(row=2,columnspan=5,ipadx=5,ipady=4)
root.mainloop()