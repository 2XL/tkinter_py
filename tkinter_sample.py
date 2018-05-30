#!/usr/bin/env python

from Tkinter import *
import tkFileDialog
import glob
import os
from tkFileDialog import askdirectory

ventana=Tk()
ventana.title("Tractament Fitxers")
ventana.minsize(600,300)
f=Frame(ventana)
f2=Frame(ventana)
f3=Frame(ventana)
fventana=Frame(ventana)
f4=Frame(ventana)


def Ocultrf():
	index=list.curselection()
	pos=0
	for i in index:	
		idx=int(i)-pos
		list.delete(idx,idx)
		pos=pos+1


def OcultNO():
	tamany=list.size()
	pos=0
	for i in range(0, tamany, 1):
		if list.selection_includes(pos) == 0:
			list.delete(pos)
		else:
			pos=pos+1


def Buscar():
	dir1=tkFileDialog.askdirectory()
	if dir1:
		d1.set(dir1)


def Sel_tots():
	list.selection_set(0, END)


def Sel_cap():
	list.selection_clear(0, END)


def Borrar():
	index=list.curselection()
	for i in index:
		os.system("rm " +list.get(i))
	vent1.destroy()
	Ocultrf()


def Ventana_borrar():
	vent1=Toplevel()
	vent1.title("Esborrar Fitxers")
	lab1=Label(vent1, text="Vols esborrar els fitxers seleccionats?")
	lab1.pack(anchor=W)
	bno=Button(vent1, text="No", command=vent1.destroy)
	bsi=Button(vent1, text="Yes", command=Borrar)
	bsi.pack(side=RIGHT, anchor=SE)
	bno.pack(side=RIGHT, anchor=SE)
	vent1.pack()
	global vent1
	

def Copy():
	index=list.curselection()
	direccion=tkFileDialog.askdirectory()
	for i in index:
		os.system("cp "+e1.get()+"/" +list.get(i)+" "+direccion)
	mostrar()


def Move():
	index=list.curselection()
	direccion=tkFileDialog.askdirectory()
	for i in index:
		os.system("mv "+e1.get()+"/" +list.get(i)+" "+direccion)
	mostrar()


def Ventana_rename():
	vent2=Toplevel()
	vent2.title("Patrons de renombrament")
	lab1=Label(vent2, text="Modifica substring: ")
	lab2=Label(vent2, text="a: ")
	bot=Button(vent2, text="Renombra", command=Renom)
	global ent1
	global ent2
	ent1=Entry(vent2)
	ent2=Entry(vent2)
	lab1.pack(side=LEFT)
	ent1.pack(side=LEFT)
	lab2.pack(side=LEFT)
	ent2.pack(side=LEFT)
	bot.pack(side=LEFT)
	global vent2

	
def Renom():
	index=list.curselection()
	for i in index:
		os.system("rename 's/" +ent1.get()+"/"+ent2.get()+"/' "+list.get(i))
	vent2.destroy()
	mostrar()



b=Button(ventana, text='Salir',command=ventana.quit)
b.pack(side=BOTTOM,anchor=SW)

bu=Button (f,text='Escollir directori treball',command=Buscar)
bu.pack(side=LEFT) 

Filtre=Label(f2,text='   Filtre por nom de fitxer:')
Filtre.pack(side=LEFT)

Llista=Label(f3,text='Llista:',bg="white", relief=SUNKEN)
Llista.pack(side=TOP,anchor=W)

Als=Label(f4, text='Als seleccionats:', bg="white", relief=SUNKEN)



Tots=Button(f4,text="Tots", command=Sel_tots)
Tots.pack(side=TOP,anchor=W)

Cap=Button(f4,text='Cap', command=Sel_cap)
Cap.pack(side=TOP,anchor=W)


Copiar=Button(f4,text='Copiar', command=Copy)
Moure=Button(f4,text='Moure', command=Move)
Esborrar=Button(f4,text='Esborrar', command=Ventana_borrar)
Renombrar=Button(f4,text='Renombrar', command=Ventana_rename)


Als.pack(side=TOP,anchor=E)
Copiar.pack(side=TOP,anchor=E)
Moure.pack(side=TOP,anchor=E)
Esborrar.pack(side=TOP,anchor=E)
Renombrar.pack(side=TOP,anchor=E)


Metacaracter=Entry(f2)
Metacaracter.pack(expand=TRUE, fill=X)
Metacaracter.insert(END,"*.*")


Scrollist=Scrollbar(fventana,orient=VERTICAL)
list=Listbox(fventana, selectmode=EXTENDED, yscrollcommand=Scrollist.set)
Scrollist.config(command=list.yview)
Scrollist.pack(side=RIGHT,fill=Y)
list.pack(side=TOP,expand=TRUE,fill=BOTH,anchor=CENTER)


d1=StringVar()
e1= Entry(f,textvariable=d1)
e1.pack(expand=TRUE,fill=X)

def Limpiar():
	list.delete(0,END)


def mostrar():

        list.delete(0,END)
	os.system("find "+e1.get()+" -name "+'"'+Metacaracter.get()+'"' " >llistat.txt" )
	llegir=open("./llistat.txt", 'r')
	os.system("rm llistat.txt")
	for i in llegir:
		i=i.replace("\n","") 
		i=i.replace(e1.get()+"/","")
		list.insert(END, i)
	list.delete(0)

Omplir=Button (f3,text='Omplir',command=mostrar)
Omplir.pack(side=TOP,anchor=W)


Netejar=Button (f3, text='Netejar',command=Limpiar)
Netejar.pack(side=TOP,anchor=W)
          





OcultarNo=Button (f3, text='Ocultar NO seleccionats', command=OcultNO)
OcultarNo.pack(side=TOP,anchor=W)

Ocultar=Button (f3, text='Ocultar seleccionats',command=Ocultrf)
Ocultar.pack(side=TOP,anchor=W)


f.pack(side=TOP,fill=X)
f2.pack(side=TOP,fill=X)
f3.pack(side=LEFT,anchor=NW)
f4.pack(side=RIGHT,anchor=NE)
fventana.pack(anchor=N,expand=TRUE,fill=X)

ventana.mainloop()

