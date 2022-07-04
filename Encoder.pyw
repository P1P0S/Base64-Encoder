from tkinter import filedialog, Tk, Button, PhotoImage,Text
import tkinter as tk
import base64, os, glob

root = Tk()
root.title('Crypter')
root.resizable(0,0)
root.geometry('250x290')
root.iconbitmap('./images/ano.ico')

textBox = Text(root, height=9, width=28)
textBox.config(state='disable')
textBox.pack()

imgLock = PhotoImage(file='./images/locked.png')
imgUnlock = PhotoImage(file='./images/unlocked.png')

def comando(op):
    if(op == 1):
        inp = filedialog.askdirectory()
        os.chdir(inp)
        file = glob.glob('*')
        for x in file:
            Ffile = open(x,'rb')
            data = base64.b64encode(Ffile.read()).decode('utf-8')
            Ffile.close()
            Sfile = open(x,'w+')
            Sfile.write(data)
            Sfile.close()
            textBox.config(state='normal')
            textBox.delete(1.1, tk.END)
            textBox.insert(1.1,'\n\n\n\n\n'+' '*10+'Encoded!')
            textBox.config(state='disabled')
            

    elif(op == 2):
        inp = filedialog.askdirectory()
        os.chdir(inp)
        file = glob.glob('*')
        for x in file:
            Ffile = open(x,'rt')
            data = base64.b64decode(Ffile.read())
            Ffile.close()
            Sfile = open(x,'wb')
            Sfile.write(data)
            Sfile.close()
            textBox.config(state='normal')
            textBox.delete(1.1, tk.END)
            textBox.insert(1.1,'\n\n\n\n\n'+' '*10+'Decoded!')
            textBox.config(state='disabled')
 
Button(text='Encode', border=0.5, image=imgLock, width=150, height=50, compound="left", 
        command = lambda: comando(1)).place(x=40,y=160)
Button(text='Decode', border=0.5, image=imgUnlock, width=150, height=50, compound="left", 
        command = lambda: comando(2)).place(x=40,y=220)

root.mainloop()
