from tkinter import *
from tkinter.ttk import *
from tkinter import font

root = Tk()
root.title("備忘錄")
root.geometry("1200x620+10+10")
root.resizable(False,False)

tool_bar=Label(root)
tool_bar.pack(side=TOP,fill=X)
font_families=font.families()
font_family_variable=StringVar()
fontfamily_Combobox=Combobox(tool_bar,width=30,value=font_families,state='readonly',textvariable=font_family_variable)
fontfamily_Combobox.current(font_families.index('Arial'))
fontfamily_Combobox.grid(row=0,column=0,padx=5)
size_variable=IntVar(),
font_size_Combobox=Combobox(tool_bar, width=14, textvariable=size_variable,state='readonly',values=tuple(range(8,81 )))
font_size_Combobox.current(4)
font_size_Combobox.grid(row=0,column=1,padx=5)

boldImage=PhotoImage(file='bold.png')
boldButton=Button(tool_bar,image=boldImage)
boldButton.grid(row=0,column=2,padx=5)

italicImage=PhotoImage(file='italic.png')
italicButton=Button(tool_bar,image=italicImage)
italicButton.grid(row=0,column=3,padx=5)

underlineImage=PhotoImage(file='underline.png')
underlineButton=Button(tool_bar,image=underlineImage)
underlineButton.grid(row=0,column=4,padx=5)

fontColorImage=PhotoImage(file='font_Color.png')
fontColorButton=Button(tool_bar,image=fontColorImage)
fontColorButton.grid(row=0,column=5,padx=5)

leftAlignImage=PhotoImage(file='left.png')
leftAlignButton=Button(tool_bar,image=leftAlignImage)
leftAlignButton.grid(row=0,column=6,padx=5)

rightAlignImage=PhotoImage(file='right.png')
rightAlignButton=Button(tool_bar,image=rightAlignImage)
rightAlignButton.grid(row=0,column=7,padx=5)

centerAlignImage=PhotoImage(file='center.png')
centerAlignButton=Button(tool_bar,image=centerAlignImage)
centerAlignButton.grid(row=0,column=8,padx=5)

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(root,yscrollcommand=scrollbar.set,font=('arial',12))
textarea.pack(fill=BOTH,expand=True)
scrollbar.config(command=textarea.yview)

status_bar=Label(root,text='Status Bar')
status_bar.pack(side=BOTTOM)

root.mainloop()