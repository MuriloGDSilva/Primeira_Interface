import sys
import tkinter as tk
import tkinter.ttk as ttk
import os.path

_script = sys.argv[0]

_location = os.path.dirname(_script)

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40'  # X11 color: #666666
_ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
_ana2color = 'beige'  # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'

_style_code_ran = 0


def _style_code():
    global _style_code_ran

    if _style_code_ran:
        return

    style = ttk.Style()

    if sys.platform == "win32":
        style.theme_use('winnative')
        style.configure('.', background=_bgcolor)
        style.configure('.', foreground=_fgcolor)
        style.configure('.', font='TkDefaultFont')
        style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

    if _bgmode == 'dark':
        style.map('.', foreground=[('selected', 'white'), ('active', 'white')])

    else:
        style.map('.', foreground=[('selected', 'black'), ('active', 'black')])

    _style_code_ran = 1


class Cadastro:

    def __init__(self, top=None):
        top = tk.Tk()
        self.top = top

        top.geometry("600x450+280+121")
        top.minsize(120, 1)
        top.maxsize(1370, 749)

        top.title("Cadastro")
        top.configure(background="#000000")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.267, rely=0.089, relheight=0.789, relwidth=0.475)
        self.Frame1.configure(relief='raised')
        self.Frame1.configure(borderwidth="1")
        self.Frame1.configure(relief="raised")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        _style_code()

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.281, rely=0.085, height=39, width=125)
        self.TLabel1.configure(background="#ffffff")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {Arial} -size 15")
        self.TLabel1.configure(borderwidth="0")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(justify='center')
        self.TLabel1.configure(text='''Cadastro''')
        self.TLabel1.configure(compound='center')

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.284, rely=0.172, relwidth=0.421)

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.035, rely=0.31, height=30, relwidth=0.926)
        self.Entry1.configure(background="#ffffff")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Arial} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(relief="solid")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = tk.Entry(self.Frame1, show='*')
        self.Entry2.place(relx=0.035, rely=0.507, height=30, relwidth=0.926)
        self.Entry2.configure(background="#ffffff")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Arial} -size 10")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(relief="solid")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.035, rely=0.254, height=21, width=84)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='sw')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 8 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Usuario/Email*''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.035, rely=0.451, height=21, width=44)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='sw')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 8 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Senha*''')

        self.Button1_1 = tk.Button(self.Frame1, command=self.cadastro_usuario)
        self.Button1_1.place(relx=0.316, rely=0.732, height=44, width=97)
        self.Button1_1.configure(activebackground="beige")
        self.Button1_1.configure(activeforeground="black")
        self.Button1_1.configure(background="#ffffff")
        self.Button1_1.configure(compound='left')
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font="-family {Arial} -size 9 -weight bold")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(relief="groove")
        self.Button1_1.configure(text='''Cadastrar-se''')
        top.mainloop()

    def cadastro_usuario(self):
        arquivo = open('usuarios.txt', 'a')
        arquivo.write(self.Entry1.get())
        arquivo.write(self.Entry2.get())
        arquivo.close()
        self.top.destroy()
