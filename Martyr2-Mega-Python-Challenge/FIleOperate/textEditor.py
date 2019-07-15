import tkinter as tk
import tkinter.scrolledtext as tst
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.textEdit=tst.ScrolledText(self,width=80,height=20)
        self.textEdit.grid(row=0,column=0,rowspan=6)
        self.btnOpen=tk.Button(self,text='打开',command=self.funcOpen)
        self.btnOpen.grid(row=1,column=1)
        self.btnSave=tk.Button(self,text='保存',command=self.funcSave)
        self.btnSave.grid(row=2,column=1)
        self.btnColor=tk.Button(self,text='颜色',command=self.funcColor)
        self.btnColor.grid(row=3,column=1)
        self.btnQuit=tk.Button(self,text='退出',command=self.funcQuit)
        self.btnQuit.grid(row=4,column=1)
    def funcOpen(self):
        self.textEdit.delete(1.0,tk.END)
        fname=tk.filedialog.askopenfilename(filetypes=[('文本文件','.txt')])
        with open(fname,'r') as f:
            str1=f.read()
        self.textEdit.insert(0.0,str1)
    def funcSave(self):
        str1=self.textEdit.get(1.0,tk.END)
        fname=tk.filedialog.asksaveasfilename(filetypes=[('文本文件','.txt')])
        with open(fname,'w') as f:
            f.write(str1)
    def funcColor(self):
        t,c=tk.colorchooser.askcolor(title='askcolor')
        self.textEdit.config(bg=c)
    def funcQuit(self):
        root.destroy()
root=tk.Tk()
root.title('文本编辑器')
app=Application(master=root)
app.mainloop()
 