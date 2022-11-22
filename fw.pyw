import tkinter as tk
from tkhtmlview import HTMLScrolledText


import fw_support


class ToplevelWin:
    def __init__(self, root, db):

        root.geometry("720x820+400+100")
        root.resizable(False,False)
        root.title("Foreign Words")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")
        root.iconbitmap(f"fw.ico")

        self.db = db
        self.root = root

        self.Frame1 = tk.Frame(self.root)
        self.Frame1.place(x= 10, y=10, height=800, width=700)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.ButtonNext = tk.Button(self.Frame1)
        self.ButtonNext.place(x=575, y=10, height=35, width=100)
        self.ButtonNext.configure(activebackground="#d9d9d9")
        self.ButtonNext.configure(activeforeground="black")
        self.ButtonNext.configure(background="#d9d9d9")
        self.ButtonNext.configure(compound='left')
        self.ButtonNext.configure(disabledforeground="#a3a3a3")
        self.ButtonNext.configure(foreground="#000000")
        self.ButtonNext.configure(highlightbackground="#d9d9d9")
        self.ButtonNext.configure(highlightcolor="black")
        self.ButtonNext.configure(pady="0")
        self.ButtonNext.configure(text='''Next word''')
        self.ButtonNext.configure(command= fw_support.next_word)

        self.ButtonTranslate = tk.Button(self.Frame1)
        self.ButtonTranslate.place(x= 575, y=50, height=35, width=100)
        self.ButtonTranslate.configure(activebackground="#d9d9d9")
        self.ButtonTranslate.configure(activeforeground="black")
        self.ButtonTranslate.configure(background="#d9d9d9")
        self.ButtonTranslate.configure(compound='left')
        self.ButtonTranslate.configure(disabledforeground="#a3a3a3")
        self.ButtonTranslate.configure(foreground="#000000")
        self.ButtonTranslate.configure(highlightbackground="#d9d9d9")
        self.ButtonTranslate.configure(highlightcolor="black")
        self.ButtonTranslate.configure(pady="0")
        self.ButtonTranslate.configure(text='''Translate''')
        self.ButtonTranslate.configure(command= fw_support.translate)

        self.ButtonAdd = tk.Button(self.Frame1)
        self.ButtonAdd.place( x=575, y=90, height=35, width=100 )
        self.ButtonAdd.configure(activebackground="#d9d9d9")
        self.ButtonAdd.configure(activeforeground="black")
        self.ButtonAdd.configure(background="#d9d9d9")
        self.ButtonAdd.configure(compound='left')
        self.ButtonAdd.configure(disabledforeground="#a3a3a3")
        self.ButtonAdd.configure(foreground="#000000")
        self.ButtonAdd.configure(highlightbackground="#d9d9d9")
        self.ButtonAdd.configure(highlightcolor="black")
        self.ButtonAdd.configure(pady="0")
        self.ButtonAdd.configure(text='''New word''')
        self.ButtonAdd.configure(command=fw_support.add_word)

        self.ButtonEdit = tk.Button(self.Frame1)
        self.ButtonEdit.place( x=575, y=130, height=35, width=100 )
        self.ButtonEdit.configure(activebackground="#d9d9d9")
        self.ButtonEdit.configure(activeforeground="black")
        self.ButtonEdit.configure(background="#d9d9d9")
        self.ButtonEdit.configure(compound='left')
        self.ButtonEdit.configure(disabledforeground="#a3a3a3")
        self.ButtonEdit.configure(foreground="#000000")
        self.ButtonEdit.configure(highlightbackground="#d9d9d9")
        self.ButtonEdit.configure(highlightcolor="black")
        self.ButtonEdit.configure(pady="0")
        self.ButtonEdit.configure(text='''Edit word''')
        self.ButtonEdit.configure(command=fw_support.update_word)

        self.ButtonDelete = tk.Button(self.Frame1)
        self.ButtonDelete.place( x=575, y=170, height=35, width=100 )
        self.ButtonDelete.configure(activebackground="#d9d9d9")
        self.ButtonDelete.configure(activeforeground="black")
        self.ButtonDelete.configure(background="#d9d9d9")
        self.ButtonDelete.configure(compound='left')
        self.ButtonDelete.configure(disabledforeground="#a3a3a3")
        self.ButtonDelete.configure(foreground="#000000")
        self.ButtonDelete.configure(highlightbackground="#d9d9d9")
        self.ButtonDelete.configure(highlightcolor="black")
        self.ButtonDelete.configure(pady="0")
        self.ButtonDelete.configure(text='''Delete word''')
        self.ButtonDelete.configure(command = fw_support.delete_word)

        self.ButtonClose = tk.Button(self.Frame1)
        self.ButtonClose.place( x=575, y=300, height=35, width=100 )
        self.ButtonClose.configure(activebackground="#d9d9d9")
        self.ButtonClose.configure(activeforeground="black")
        self.ButtonClose.configure(background="#d9d9d9")
        self.ButtonClose.configure(compound='left')
        self.ButtonClose.configure(disabledforeground="#a3a3a3")
        self.ButtonClose.configure(foreground="#000000")
        self.ButtonClose.configure(highlightbackground="#d9d9d9")
        self.ButtonClose.configure(highlightcolor="black")
        self.ButtonClose.configure(pady="0")
        self.ButtonClose.configure(text='''Close''')
        self.ButtonClose.configure(command = fw_support.to_tray)

        self.ButtonSettings = tk.Button(self.Frame1)
        self.ButtonSettings.place( x=575, y=210, height=35, width=100 )
        self.ButtonSettings.configure(activebackground="#d9d9d9")
        self.ButtonSettings.configure(activeforeground="black")
        self.ButtonSettings.configure(background="#d9d9d9")
        self.ButtonSettings.configure(compound='left')
        self.ButtonSettings.configure(disabledforeground="#a3a3a3")
        self.ButtonSettings.configure(foreground="#000000")
        self.ButtonSettings.configure(highlightbackground="#d9d9d9")
        self.ButtonSettings.configure(highlightcolor="black")
        self.ButtonSettings.configure(pady="0")
        self.ButtonSettings.configure(text='''Settings''')
        self.ButtonSettings.configure(command = fw_support.set_rapid_key)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(x=10, y=10, height=180, width=540)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(font=("Arial", 25))
        self.Label1.configure(foreground="black")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(borderwidth = 2, relief="groove")
        self.Label1.configure(wraplength = 520)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(x=10, y=200, height=180, width=540)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(font=("Arial", 25))
        self.Label2.configure(foreground="black")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(borderwidth=2, relief="groove")
        self.Label2.configure(wraplength = 520)

        self.FrameHtml = tk.Frame(self.Frame1)
        self.FrameHtml.place(x=10, y=390, height=395, width=675)
        self.FrameHtml.configure(relief='groove')
        self.FrameHtml.configure(borderwidth="2")
        self.FrameHtml.configure(relief="groove")
        self.FrameHtml.configure(background="#d9d9d9")
        self.FrameHtml.configure(highlightbackground="#b4b4b4")
        self.FrameHtml.configure(highlightcolor="black")

        self.HtmlText = HTMLScrolledText(self.FrameHtml)
        self.HtmlText.configure(height=100, width=100 , background="#d9d9d9", highlightbackground="#b4b4b4", highlightcolor="#b4b4b4", state="disabled", padx=3, pady=3)
        self.HtmlText.pack(fill="both", expand=True)
        self.HtmlText.set_html("<html></html>")

        self.ButtonNext.focus_set()

def start_up():
    fw_support.main()

if __name__ == '__main__':
    fw_support.main()




