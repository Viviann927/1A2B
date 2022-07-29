import tkinter as tk
import tkinter.messagebox
import random
import re

def __guess1():
    ans = set()
    while True:
        ans.add(random.randint(0,9))
        if len(ans) == 4:
            break
    return list(ans)

cnt = 1
anss = __guess1()   

def __guess2():
    global anss, cnt
    x = ent.get()
    a = 0
    b = 0
    if len(x) == 4:
        if x[0] in x[1:4] or x[1] in x[2:4] or x[2] in x[-1] or x[3] in x[0:3]:
           tk.messagebox.showwarning('Warning',"Numbers Can't Be The Same!" )
        for i in range(4):
            if int(x[i]) == anss[i]:
                 a+=1
            elif int(x[i]) in anss:
                 b+=1
        lst.insert(tk.END, '('+x+')'+' ==> '+str(a)+"A"+str(b)+"B")
        ent.delete(0, tk.END)
        lst.insert(tk.END, "You Guess"+" "+str(cnt)+" "+"Times！")
        lst.insert(tk.END, "------------------------------")
        cnt+=1
        
        if a == 4:
            lst.insert(tk.END, "Congratulations！")
            tk.messagebox.showinfo('Text','Bingo!')
            lst.delete(0, tk.END)
            __again()
    if x == '':
        tk.messagebox.showwarning('Warning',"Can't Be Blank!" )
    else:
        if not re.findall('[0-9]', str(x)):
          tk.messagebox.showwarning('Warning',"Only Numbers!" )  
        elif len(x) > 4:
          tk.messagebox.showwarning('Warning',"Too Long!" )   
        elif len(x) < 4:
          tk.messagebox.showwarning('Warning',"Too Short!" )                       
          

def __delete():
    MBX1 = tk.messagebox.askyesno('Text','Are You Sure To Delete?')
    if MBX1:
        lst.delete(0, tk.END)
    else:
        pass


def __again():
    global anss, cnt 
    MBX2 = tk.messagebox.askyesno('Text','Want Try One More?')
    if MBX2:
        lst.delete(0, tk.END)
        cnt = 1
        anss = __guess1()
    else:
        if not MBX2:
            root.destroy()
        

def __bye():
    MBX3 = tk.messagebox.askyesno('Exit','Are You Sure To Exit?')
    if MBX3:
        root.destroy()
    else:
        pass

def __Ans():
    global anss
    root1 = tk.Tk()
    root1.title('The Answer')
    root1.geometry('250x100+1100+300')
    root1.config(bg='#DCD0C0')
    root1.resizable(False,False)
    instr = tk.Text(root1, font=('YouYuan', 20), bg='black', fg='white', padx=60, pady=20)
    if True:
        instr.insert(tk.END, anss)
        instr.pack(padx=15, pady=15)
        root1.after(2000, lambda: root1.destroy())
    root1.mainloop()
    
#=============================== 
root = tk.Tk()
root.title("Let's Guess")
root.geometry('400x450+700+300')
root.resizable(False,False)
root.attributes('-topmost',1)
root.config(bg='#DCD0C0')

#=============================== 
frm = tk.Frame(root, width=400 , height=170, bg='#DCD0C0')
frm.grid(row=0, column=0)

lb = tk.Label(frm, text='✲ Guess 4 Different Numbers ✲', font=('YouYuan',17), bg='#DCD0C0')
lb.place(x=9, y=10)

ent = tk.Entry(frm, width=10, bd=3, fg='blue', font=('YouYuan',17), relief=tk.RAISED)
ent.focus_set()
ent.place(x=130, y=55)

lb2 = tk.Label(frm, text='ex:0123', font=('YouYuan',13), bg='#DCD0C0')
lb2.place(x=153, y=88)

bnt1 = tk.Button(frm, text=' GUESS！', bg='lightgreen', font=('YouYuan',15), relief=tk.RAISED, command=__guess2)
bnt1.place(x=5, y=120)
bnt2 = tk.Button(frm, text=' DELETE！', bg='lightblue', font=('YouYuan',15), relief=tk.RAISED, command=__delete)
bnt2.place(x=100, y=120)
bnt3 = tk.Button(frm, text=' AGAIN！', bg='#d1b7dc', font=('YouYuan',15), relief=tk.RAISED, command=__again)
bnt3.place(x=205, y=120)
bnt4 = tk.Button(frm, text=' BYEEE！', bg='lightpink', font=('YouYuan',15), relief=tk.RAISED, command=__bye)
bnt4.place(x=300, y=120)

#=============================== 
frm2 = tk.Frame(root, width=400 , height=120)
frm2.grid(row=1, column=0)

yscb = tk.Scrollbar(frm2)
yscb.pack(side=tk.RIGHT, fill=tk.Y)
lst = tk.Listbox(frm2, width=32 , height=11, bg='lightgray', font=('YouYuan',15))
lst.pack()

yscb.config(command=lst.yview)
lst.config(yscrollcommand=yscb.set)

#=============================== 
frm3 = tk.Frame(root, width=400 , height=100, bg='#DCD0C0')
frm3.grid(row=2, column=0)

bnt5 = tk.Button(frm3, text="ANS", bg='#DCD0C0', font=('YouYuan',14), relief=tk.RAISED, command=__Ans)
bnt5.place(x=350, y=10)

root.mainloop()