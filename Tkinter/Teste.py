import os.path
import sys
import tkinter as tk
import tkinter.ttk as ttk
from cadastro import Cadastro
import mysql.connector

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
        style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])
    if _bgmode == 'dark':
        style.map('.', foreground=[('selected', 'white'), ('active', 'white')])
    else:
        style.map('.', foreground=[('selected', 'black'), ('active', 'black')])

    _style_code_ran = 1


class Toplevel1:

    def __init__(self, top=None):
        self.top = top
        top = tk.Tk()
        top.geometry("600x450+293+145")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.title("Login")
        top.configure(background="#000000")
        self.top = top
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.267, rely=0.089, relheight=0.789, relwidth=0.475)
        self.Frame1.configure(relief='raised')
        self.Frame1.configure(borderwidth="1")
        self.Frame1.configure(relief="raised")
        self.Frame1.configure(background="#ffffff")
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
        self.TLabel1.configure(text='''LOGIN''')
        self.TLabel1.configure(compound='center')

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.284, rely=0.172, relwidth=0.421)

        self.Entry1_login = tk.Entry(self.Frame1)
        self.Entry1_login.place(relx=0.035, rely=0.366, height=30, relwidth=0.926)
        self.Entry1_login.configure(background="#ffffff")
        self.Entry1_login.configure(disabledforeground="#a3a3a3")
        self.Entry1_login.configure(font="-family {Arial} -size 10")
        self.Entry1_login.configure(foreground="#000000")
        self.Entry1_login.configure(insertbackground="black")
        self.Entry1_login.configure(relief="solid")

        self.Entry2_cadastro = tk.Entry(self.Frame1, show='*')
        self.Entry2_cadastro.place(relx=0.035, rely=0.563, height=30, relwidth=0.926)
        self.Entry2_cadastro.configure(background="#ffffff")
        self.Entry2_cadastro.configure(disabledforeground="#a3a3a3")
        self.Entry2_cadastro.configure(font="-family {Arial} -size 10")
        self.Entry2_cadastro.configure(foreground="#000000")
        self.Entry2_cadastro.configure(insertbackground="black")
        self.Entry2_cadastro.configure(relief="solid")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.035, rely=0.31, height=21, width=84)
        self.Label1.configure(anchor='sw')
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(borderwidth="0")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial} -size 8 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Usuario/Email*''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.035, rely=0.507, height=21, width=44)
        self.Label2.configure(anchor='sw')
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial} -size 8 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Senha*''')

        self.Button_login = tk.Button(self.Frame1, command=self.Verificar_login)
        self.Button_login.place(relx=0.175, rely=0.789, height=34, width=67)
        self.Button_login.configure(activebackground="beige")
        self.Button_login.configure(activeforeground="black")
        self.Button_login.configure(background="#ffffff")
        self.Button_login.configure(compound='left')
        self.Button_login.configure(cursor="arrow")
        self.Button_login.configure(disabledforeground="#a3a3a3")
        self.Button_login.configure(font="-family {Arial} -size 9 -weight bold")
        self.Button_login.configure(foreground="#000000")
        self.Button_login.configure(highlightbackground="#d9d9d9")
        self.Button_login.configure(highlightcolor="black")
        self.Button_login.configure(pady="0")
        self.Button_login.configure(relief="groove")
        self.Button_login.configure(text='''Login''')

        self.Button2_cadastro = tk.Button(self.Frame1, command=Cadastro)
        self.Button2_cadastro.place(relx=0.561, rely=0.789, height=34, width=67)
        self.Button2_cadastro.configure(activebackground="beige")
        self.Button2_cadastro.configure(activeforeground="black")
        self.Button2_cadastro.configure(background="#ffffff")
        self.Button2_cadastro.configure(compound='left')
        self.Button2_cadastro.configure(cursor="arrow")
        self.Button2_cadastro.configure(disabledforeground="#a3a3a3")
        self.Button2_cadastro.configure(font="-family {Arial} -size 9 -weight bold")
        self.Button2_cadastro.configure(foreground="#000000")
        self.Button2_cadastro.configure(highlightbackground="#d9d9d9")
        self.Button2_cadastro.configure(highlightcolor="black")
        self.Button2_cadastro.configure(pady="0")
        self.Button2_cadastro.configure(relief="groove")
        self.Button2_cadastro.configure(text='''Cadastro''')
        top.mainloop()

    def Verificar_login(self):

        # Estabelecendo conexão com o banco de dados
        cnx = mysql.connector.connect(user='root', password='',
                                      host='localhost',
                                      database='cadastrotk')

        # Cursor para executar as queries
        cursor = cnx.cursor()

        # ID do cadastro a ser verificado
        usuario = self.Entry1_login.get()
        senha = self.Entry2_cadastro.get()

        # Query que verifica se o cadastro está presente na tabela
        query = f"SELECT COUNT(*) FROM cadastrotk WHERE email = '{usuario}' and senha = '{senha}'"

        # Executando a query
        cursor.execute(query)

        # Obtendo o resultado
        resultado = cursor.fetchone()[0]

        if resultado > 0:
            print(f"Login Feito com sucesso!!.")
        else:
            print(f"Esse usuario não existe!!.")

        # Fechando a conexão e o cursor
        cursor.close()
        cnx.close()

        self.top.destroy()


Toplevel1()
