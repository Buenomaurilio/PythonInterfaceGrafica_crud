from tkinter import*
import random
import time
import datetime

root = Tk()
root.geometry("1350x750+0+0")
root.title("Sistema de vendas")
root.configure(background= 'black')


#Frames Primários
Tops = Frame(root, width=1350, height=100, bd=9, relief="raise")
Tops.pack(side=TOP)

framef1 = Frame(root, width=900, height=650, bd=9, relief="raise")
framef1.pack(side=LEFT)

framef2= Frame(root, width=440, height=650, bd=9, relief="raise")
framef2.pack(side=RIGHT)


#Frames Secundários
frameft2 = Frame (framef2, width=440, height=550, bd=2, relief="raise")
frameft2.pack(side = TOP)

framefb2 = Frame(framef2, width=440, height=250, bd=2, relief="raise")
framefb2.pack(side = BOTTOM)

framef1a= Frame(framef1, width=900, height=531, bd=2, relief="raise")
framef1a.pack(side=TOP)

framef2a= Frame(framef1, width=950, height=531, bd=2, relief="raise")
framef2a.pack(side=BOTTOM)

framef1aa= Frame(framef1a, width=450, height=730, bd=2, relief="raise")
framef1aa.pack(side=LEFT)

framef1ab = Frame(framef1a, width=450, height=730, bd=2, relief="raise")
framef1ab.pack(side=RIGHT)



#CRIANDO FRAME DO RODAPÉ
framef2aa = Frame(framef2a, width=450, height=800, bd=2, relief="raise")
framef2aa.pack(side=LEFT)

framef2ab = Frame(framef2a, width=450, height=800, bd=2, relief="raise")
framef2ab.pack(side=RIGHT)

frameRODAPE = Frame(framef2a, width=280, height=190, bd=0, relief="raise")
frameRODAPE.pack(side=BOTTOM)




#TROCANDO A COR DE FUNDO DO FRAME DA ESQUERDA E DIREITA
framef2.configure(background= 'gray')
framef1.configure(background= 'blue')


#INSERINDO O RÓTULO DE CABEÇALHO COM O TÍTULO

lblInfo = Label(Tops,font = ('arial',40,'bold'),text="SISTEMA DE VENDAS ",bd = 8,width=55)
lblInfo.grid(row = 0, column = 0)

#============================================ DECLARANDO AS PRIMEIRAS VARIÁVEIS ====================================

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()

#SETANDO AS VARIÁVEIS

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")
var17.set("0")
var18.set("0")

#CRIANDO OS RADIO BUTTONS PARA O CAFÉ

Latte = Checkbutton(framef1aa,text="Latte \t",variable=var1,onvalue=1,offvalue=0, width = 15, font=('arial',18,'bold')).grid(row = 0,sticky = W)

Expresso = Checkbutton(framef1aa,text="Expresso \t",variable=var2,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 1,sticky = W)

Iced_Latte = Checkbutton(framef1aa,text="Iced_Latte \t",variable=var3,onvalue=1,offvalue=0, width = 22,font=('arial',18,'bold')).grid(row = 2,sticky = W)

Cafe_Cortado = Checkbutton(framef1aa,text="Cafe_Cortado \t",variable=var4,onvalue=1,offvalue=0, width = 22,font=('arial',18,'bold')).grid(row = 3,sticky = W)

Cafe_Leite = Checkbutton(framef1aa,text="Cafe_Leite \t",variable=var5,onvalue=1,offvalue=0, width = 22,font=('arial',18,'bold')).grid(row = 4,sticky = W)

Cafe_Preto = Checkbutton(framef1aa,text="Cafe_Preto \t",variable=var6,onvalue=1,offvalue=0, width = 22,font=('arial',18,'bold')).grid(row = 5,sticky = W)

Cafe_creme = Checkbutton(framef1aa,text="Cafe_creme \t",variable=var7,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 6,sticky = W)

Capuccino = Checkbutton(framef1aa,text="Capuccino \t",variable=var8,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 7,sticky = W)

Cafe_Expresso = Checkbutton(framef1aa,text="Cafe_Expresso \t",variable=var9,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 8,sticky = W)



#CRIANDO OS RADIO BUTTON DOS BOLOS

Bolo_cafe = Checkbutton(framef1ab,text="Bolo_cafe \t",variable=var10,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 0,sticky = W)

Bolo_Cenoura = Checkbutton(framef1ab,text="Bolo_Cenoura \t",variable=var11,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 1,sticky = W)

Bolo_Milho= Checkbutton(framef1ab,text="Bolo_Milho \t",variable=var12,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 2,sticky = W)

Bolo_Banana = Checkbutton(framef1ab,text="Bolo_Banana \t",variable=var13,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 3,sticky = W)

Bolo_Morango = Checkbutton(framef1ab,text="Bolo_Morango \t",variable=var14,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 4,sticky = W)

Bolo_Limao = Checkbutton(framef1ab,text="Bolo_Limao \t",variable=var15,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 5,sticky = W)

Bolo_Caçarola = Checkbutton(framef1ab,text="Bolo_Caçarola \t",variable=var16,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 6,sticky = W)

Bolo_Chocolate = Checkbutton(framef1ab,text="Bolo_Chocolate \t",variable=var17,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 7,sticky = W)

Bolo_Gelado = Checkbutton(framef1ab,text="Bolo_Gelado \t",variable=var18,onvalue=1,offvalue=0, width = 22, font=('arial',18,'bold')).grid(row = 8,sticky = W)

#CRIANDO CAMPOS DE TEXTO CAFE

txtLatte = Entry (framef1aa,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 0, column = 1)
txtLatte = Entry (framef1aa,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 1, column = 1)
txtLatte = Entry (framef1aa,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 2, column = 1)
txtLatte = Entry (framef1aa,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 3, column = 1)
txtLatte = Entry (framef1aa,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 4, column = 1)
txtLatte = Entry (framef1aa,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 5, column = 1)
txtLatte = Entry (framef1aa,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 6, column = 1)
txtLatte = Entry (framef1aa,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 7, column = 1)
txtLatte = Entry (framef1aa,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 8, column = 1)


#CRIANDO CAMPOS DE TEXTO DOS BOLOS

txtLatte = Entry (framef1ab,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 0, column = 1)
txtLatte = Entry (framef1ab,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 1, column = 1)
txtLatte = Entry (framef1ab,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 2, column = 1)
txtLatte = Entry (framef1ab,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 3, column = 1)
txtLatte = Entry (framef1ab,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 4, column = 1)
txtLatte = Entry (framef1ab,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 5, column = 1)
txtLatte = Entry (framef1ab,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 6, column = 1)
txtLatte = Entry (framef1ab,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 7, column = 1)
txtLatte = Entry (framef1ab,font = ('arial',15,'bold'),bd = 1, width = 8, justify = 'left', state = DISABLED)
txtLatte.grid(row = 8, column = 1)


#CAMPOS DO RECIBO

lblRecibo = Label(frameft2, font = ('arial',12, 'bold'),text = "Recibo do Cliente :", bd = 2, anchor = W)
lblRecibo.grid(row = 0, column = 0, sticky = W)

txtRecibo = Text(frameft2, width = 59, height = 33, bg = "gray", bd = 8, font = ('arial', 9, 'bold'))
txtRecibo.grid(row = 1, column = 0, sticky = W)


#CAMPOS DOS BOTÕES


cmdTotal = Button(framefb2, padx = 16, pady = 1, bd = 3, fg = 'black', font = ('arial', 12, 'bold'),  width = 6, text = "Total").grid(row = 0, column = 0)
cmdRecibo = Button(framefb2, padx = 16, pady = 1, bd = 3, fg = 'black', font = ('arial', 12, 'bold'),  width = 6, text = "Recibo").grid(row = 0, column = 1)
cmdLimpar = Button(framefb2, padx = 16, pady = 1, bd = 3, fg = 'black', font = ('arial', 13, 'bold'),  width = 6, text = "Limpar").grid(row = 0, column = 2)
cmdSair = Button(framefb2, padx = 16, pady = 1, bd = 3, fg = 'black', font = ('arial', 12, 'bold'),  width = 6, text = "Sair").grid(row = 0, column = 3)

# CRIANDO OS CAMPOS DO RODAPE FRAME DA ESQUERDA

lblCustoBebidas = Label(framef2aa, font = ('arial',12, 'bold'),text = "Custo Bebidas :", bd = 3, )
lblCustoBebidas.grid(row = 0, column = 0, sticky = W)

txtCustoBebidas = Entry (framef2aa, font = ('arial', 12, 'bold'), bd = 1, justify = 'left', )
txtCustoBebidas.grid(row = 0, column = 1)

lblCustoBebidas = Label(framef2aa, font = ('arial',12, 'bold'),text = "Custo Bebidas :", bd = 3, )
lblCustoBebidas.grid(row = 1, column = 0, sticky = W)

txtCustoBebidas = Entry (framef2aa, font = ('arial', 12, 'bold'), bd = 1, justify = 'left')
txtCustoBebidas.grid(row = 1, column = 1)

lblCustoBebidas = Label(framef2aa, font = ('arial',12, 'bold'),text = "Custo Bebidas :", bd = 3)
lblCustoBebidas.grid(row = 2, column = 0, sticky = W)

txtCustoBebidas = Entry (framef2aa, font = ('arial', 12, 'bold'), bd = 1, justify = 'left')
txtCustoBebidas.grid(row = 2, column = 1)

# CRIANDO OS CAMPOS DO RODAPE FRAME DA DIREITA

lblCustoBebidas = Label(framef2ab, font = ('arial',12, 'bold'),text = "Custo Bebidas :", bd = 2)
lblCustoBebidas.grid(row = 0, column = 0, sticky = W)

txtCustoBebidas = Entry (framef2ab, font = ('arial', 12, 'bold'), bd = 1, justify = 'left')
txtCustoBebidas.grid(row = 0, column = 1)

lblCustoBebidas = Label(framef2ab, font = ('arial',12, 'bold'),text = "Custo Bebidas :", bd = 2)
lblCustoBebidas.grid(row = 1, column = 0, sticky = W)

txtCustoBebidas = Entry (framef2ab, font = ('arial', 12, 'bold'), bd = 1, justify = 'left')
txtCustoBebidas.grid(row = 1, column = 1)

lblCustoBebidas = Label(framef2ab, font = ('arial',12, 'bold'),text = "Custo Bebidas :", bd = 2)
lblCustoBebidas.grid(row = 2, column = 0, sticky = W)

txtCustoBebidas = Entry (framef2ab, font = ('arial', 12, 'bold'), bd = 1, justify = 'left')
txtCustoBebidas.grid(row = 2, column = 1)





root.mainloop()