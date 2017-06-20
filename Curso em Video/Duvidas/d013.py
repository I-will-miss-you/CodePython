
#Importando biblioteca:
from tkinter import *


#Definindo função:
def onClick():
    print('Você clicou no botão OK!')

#Código da gui:
janela = Tk()



#Cria botão com texto = "OK" e comando associado: aoClicarOk()
bt_ok = Button(janela, text='OK', command=onClick)

#Usa-se pack() como gerenciador de layout
bt_ok.pack(side=TOP)

janela.title(' Janela ')
janela.geometry('250x50+300+300')
janela.mainloop()