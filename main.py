from tkinter import *
from tkinter.ttk import *
from tkinter import font

root = Tk()
root.title("備忘錄")
root.geometry("1200x620+10+10")
root.resizable(False,False)

def change_font_family(event):
    selected_family = fontfamily_Combobox.get()
    textarea.config(font=(selected_family, textarea['font'][1]))

def change_font_size(event):
    selected_size = size_variable.get()
    textarea.config(font=(textarea['font'][0], selected_size))

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

labelframe = LabelFrame(root, width=400, height=50, text='標題')
labelframe.pack(padx=10, pady=10)
input_font = ("Helvetica", 20)

text_input = Text(labelframe, width=400, height=1, wrap='none', font=input_font)
text_input.pack()

labelframe = LabelFrame(root, width=400, height=150, text='內容')
labelframe.pack(padx=10, pady=5)

input_font = ("Helvetica", 15)

text_input = Text(labelframe, width=110, height=20, wrap='word', font=input_font)
text_input.pack()

status_bar=Label(root,text='備忘錄')
status_bar.pack(side=BOTTOM)

root.mainloop()