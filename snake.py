# -*- coding: cp1252 -*-
#######################################################################
#                    Louis Ménigault                                  #
#                                                                     #
#                    Snake version 1                                  #
#                                                                     #
#                                                                     #
#                                                                     #
#######################################################################
from Tkinter import *
from random import randrange
from math import sin,cos,pi
from os import getcwd,chdir
rep=getcwd()
def start(event=0):
    global flag,intcrono,vv
    if flag==0 :
        flag=1
        move()
    if vv==1:
        intcrono=1
        vv=0
        crono()
def move():
    global x,y,di,cw,flag,label,vs,nr,liste,listecercle,wintext,intcrono,loose,niveau,ts,ofi
    d=liste[0]
    f=d[0]
    can.coords(f,x,y,x+15,y+15)
    liste.append([f,x,y])
    del(liste[0])
    if di==1:
        y=y-15
    if di==2:
        y=y+15
    if di==3:
        x=x+15
    if di==4:
        x=x-15
    i=0

    while i<nr:
        t=listecercle[i]
        p=t[1]
        m=t[2]
        c=t[0]
        if x>p-20 and x<p+20 and y>m-20 and y<m+20:
            can.coords(c,0,0,0,0)
            listecercle[i]=[0,0,0]
            xn=20
            yn=20
            carre=can.create_rectangle(xn,yn,xn+15,yn+15,fill='pink')
            liste.append([carre,xn,yn])
            cw=cw+1
            if cw==nr:
                can.itemconfigure(wintext,text='YOU WIN !!!!!!!!!')
                flag=0
                intcrono=0
                loose=23454
                if niveau==10:
                    niveau=0
                wx=str('n'+str(niveau)+' '+str(ts)+'\n')
                ofi.write(wx)
                niveauup(event=0)
        i=i+1
    n=0
    while n<len(liste):
        v=liste[n]
        vx=v[1]
        vy=v[2]
        if x==vx and y==vy:
            loose=can.create_text(500,100,anchor=CENTER, text='YOU LOOSE !!!!!!!', fill='red',font='Arial 30 bold')
            flag=0
            intcrono=0
            wx='n'+str(niveau)+' '+str(ts)+' l\n'
            ofi.write(wx)
            fen.after(1500,restart)
        n=n+1
    if x<0 or x>1000 or y<0 or y>500:
        loose=can.create_text(500,100,anchor=CENTER, text='YOU LOOSE !!!!!!!', fill='red',font='Arial 30 bold')
        flag=0
        intcrono=0
        wx='n'+str(niveau)+' '+str(ts)+' l\n'
        ofi.write(wx)
        fen.after(1500,restart)


    label.configure(text='Tu as avalé ' + str(cw) + ' pommes')
    if flag!=0:
        fen.after(vs,move)

def goup(event):
    global di
    if di!=2:
        di=1
def godown(event):
    global di
    if di!=1:
        di=2
def goright(event):
    global di
    if di!=4:
        di=3
def goleft(event):
    global di
    if di!=3:
        di=4
def seconde():
    global ts
    ts=ts+1
    lcrono.configure(text='Temps écoulés : '+str(ts)+" secondes")
    crono()
def crono():
    if intcrono!=0:
        fen.after(1000,seconde)
def loosedel():
    global loose
    can.delete(loose)
def recreate():
    global nr,vs,liste,listecercle,ncarre,xo,yo,niveau,wintext,x,y,cw,ts,di,vv,dw
    x=110
    y=50
    i=0
    u=0
    ts=0
    cw=0
    ide=0
    xo=50
    yo=50
    di=3
    vv=1
    idec=0
    loosedel()
    while ide<len(liste):
        listed=liste[ide]
        cdel=listed[0]
        can.delete(cdel)
        ide=ide+1
    while idec<len(listecercle):
        lcerclede=listecercle[idec]
        cedel=lcerclede[0]
        can.delete(cedel)
        idec=idec+1
    liste=[]
    listecercle=[]
    can.itemconfigure(tniveau,text='Niveau '+str(niveau))
    fen.after(dw,windel)
    while i<ncarre:
        carre=can.create_rectangle(xo,yo,xo+15,yo+15, fill='pink')
        liste.append([carre,xo,yo])
        i=i+1
        xo=xo+15
    while u<nr:
        p=randrange(1000)
        m=randrange(500)
        cercle=can.create_oval(p,m,p+20,m+20,fill='green')
        listecercle.append([cercle,p,m])
        u=u+1
def restart(event=0):
    global nr,vs,niveau
    nr=10
    vs=140
    niveau=1
    recreate()
def flagstop(event=0):
    global flag
    if flag==1:
        flag=0
    else:
        flag=1
        move()
def windel():
    can.itemconfigure(wintext,text='')
def niveauup(event=0):
    global nr,vs,niveau,dw
    if niveau==0:
        dw=10000
        winmove()
    else:
        nr=nr+10
        vs=vs-10
        niveau=niveau+1
        recreate()
def restart_level(event=0):
    recreate()
def winmove(event=0):
    global wintext,ad
    can.coords(wintext,cos(ad)*300+500,sin(ad)*200+250)
    ad=ad+pi/60
    fen.after(80,winmove)
def helpb():
    fen2=Toplevel(fen)
    Message(fen2,width =300, aspect =200,text="Tu es un serpent, et tu a très très faim, heureusement tu peux utiliser les touches fléchées du clavier pour te diriger et manger les pommes.\n Racourcis: \n Entrer pour commencer \n P pour pause \n R pour recommencer \n L pour recommencer le niveau \n Alt + F4 pour quitter",font='Arial 15').pack()
def info():
    fen3=Toplevel(fen)
    Message(fen3,width=400,aspect=100,text="SNAKE 1.1",font="Arial 50 bold").pack()
    Message(fen3,width=300,aspect=300,text="Copyright Louis Ménigault",font='Arial 30 bold').pack()
    Message(fen3,width=310,aspect=300,text="Contact : SNAKE.menigault@yopmail.com",font='Arial 15 bold').pack()
def userf():
    global entre,fen4
    fen4=Toplevel(fen)
    label3=Label(fen4,text='Entre le nom de ton serpent : ')
    label3.pack(side=LEFT)
    entre=Entry(fen4)
    entre.pack(side=LEFT)
    fen4.bind('<Return>',fiuser)
def fiuser(event):
    global entre,user,ofi,fen4,luser
    chdir(rep)
    uti=entre.get()
    user=entre.get()+".snake"
    luser.configure(text='Utilisateurs : '+entre.get())
    fen4.destroy()
    ofi=open(user,'a')
    ofi.write('p\n')
    obfichier=open('snakeusers.snake','r')
    ofichier=open('snakeusers.snake','a')
    users=obfichier.read()
    if uti in users:
        a=0
    else:
        ofichier.write(uti+"\n")
    obfichier.close()
    ofichier.close()
def userchange():
    global ofi,flag,intcrono
    ofi.close()
    flag=0
    intcrono=0
    restart(),userf()

def fenclass():
    global fenclassement,bou9
    fenclassement=Toplevel(fen)
    bou9=Button(fenclassement,text="Générer le Classement",font='30',command=classstat)
    bou9.pack(side=BOTTOM,padx=20,pady=20)
def classstat():
    global ofi,bou9,liste2,liste3
    chdir(rep)
    objfi=open('snakeusers.snake','r')
    lniv=[]
    lusers=[]
    j=0
    ltj=[]
    while 1:
        j=objfi.readline()
        if j=="":
            objfi.close()
            break
        else:
            lusers.append(j[:len(j)-1])
    for user in lusers:
        liste=[]
        if user!="":
            userr=user+'.snake'
        ofich=open(userr,'r')
        l=0
        p=0
        tj=0
        while 1:
            n=ofich.readline()
            if n=='':
                break
            else:
                if str(n[len(n)-2:len(n)-1])!='l' and str(n[0])!='p':
                    if n[1]==0:
                        liste.append([10,n[3:len(n)-1]])
                    else:
                        liste.append([n[1],n[3:len(n)-1]])
                        tj=tj+int(n[3:len(n)-1])
            try:
                if str(n[len(n)-2:len(n)-1])=='l':
                    l=l+1
                    tj=tj+int(n[3:len(n)-3])
            except:
                rete=434
            if n[0]=='p':
                p=p+1
        liste.sort()
        liste.reverse()
        tri2(liste)
        lniv.append([liste3[0],user,p,l,tj])
        ltj.append(tj)
    lniv.sort()
    lniv.reverse()
    tri(lniv)
    rang=1
    ligne=0
    for vainqueur in liste2:
        if rang==1:
            Label(fenclassement,text='rang : ').grid(row=ligne,column=0)
            Label(fenclassement,text='serpent : ').grid(row=ligne,column=1)
            Label(fenclassement,text='niveau : ').grid(row=ligne,column=2)
            Label(fenclassement,text='temps : ').grid(row=ligne,column=3)
            Label(fenclassement,text='nombre de partie : ').grid(row=ligne,column=4)
            Label(fenclassement,text='pertes : ').grid(row=ligne,column=5)
            Label(fenclassement,text='temps de jeu : ').grid(row=ligne,column=6)
            ligne=ligne+1
        if vainqueur[4]>60:
            g=vainqueur[4]/60
            h=vainqueur[4]%60
            f=str(g)+' mn '+str(h)+' s'
        if vainqueur[4]>3600:
            q=vainqueur[4]/3600
            s=vainqueur[4]%3600
            d=s/60
            k=s%60
            f=str(q)+' h '+str(d)+' mn '+str(k)+' s'
        if vainqueur[4]<60:
            f=str(vainqueur[4])+' s'
        Label(fenclassement,text=str(rang),font='15').grid(row=ligne,column=0,pady=10)
        Label(fenclassement,text=vainqueur[1],font='15').grid(row=ligne,column=1)
        Label(fenclassement,text='niveau '+str(vainqueur[0][0]),font='15').grid(row=ligne,column=2)
        Label(fenclassement,text=str(vainqueur[0][1]),font='15').grid(row=ligne,column=3)
        Label(fenclassement,text=str(vainqueur[2]),font='15').grid(row=ligne,column=4)
        Label(fenclassement,text=str(vainqueur[3]),font='15').grid(row=ligne,column=5)
        Label(fenclassement,text=f,font='15').grid(row=ligne,column=6)
        rang=rang+1
        ligne=ligne+1
    tjt=0
    for tji in ltj:
        tjt=tjt+tji
    if tjt >60 and tjt<3600:
        q=tjt/60
        s=tjt%60
        tjts=str(q)+' mn '+str(s)+' s'
    if tjt >3600:
        q=tjt/3600
        s=tjt%3600
        d=s/60
        k=s%60
        tjts=str(q)+' h '+str(d)+' mn '+str(k)+' s'
    Label(fenclassement,text='temps total de jeux\n '+str(tjts),font='15').grid(row=ligne,column=6)
    bou9.grid(row=ligne,columnspan=6,padx=20,pady=20)
def tri(liste):
    global liste2
    liste2=[]
    while 1:
        if liste==[]:
            break
        e=0
        for a in liste:
            d=0
            for b in liste:
                if int(a[0][0])==int(b[0][0]) and int(a[0][1])<=int(b[0][1]):
                    d=d+1
                    if d==len(liste):
                        d=0
                        liste2.append(a)
                        del(liste[e])
                elif int(a[0][0])>int(b[0][0]):
                    d=d+1
                    if d==len(liste):
                        d=0
                        liste2.append(a)
                        del(liste[e])
            e=e+1
def tri2(liste):
    global liste3
    liste3=[]
    while 1:
        if liste==[]:
            break
        e=0
        for a in liste:
            d=0
            for b in liste:
                if int(a[0])==int(b[0]) and int(a[1])<=int(b[1]):
                    d=d+1
                    if d==len(liste):
                        d=0
                        liste3.append(a)
                        del(liste[e])
                elif int(a[0])>int(b[0]):
                    d=d+1
                    if d==len(liste):
                        d=0
                        liste3.append(a)
                        liste=[]
            e=e+1


vv=1
ncarre=4
x=110
y=50
i=0
liste=[]
di=3
xo=50
yo=50
u=0
nr=10
cw=0
flag=0
listecercle=[]
ts=0
vs=140
ncercle=10
niveau=1
intcrono=1
ad=pi/60
dw=2000
loose=34535
liste2=[]
ofi=open('visiteur.snake','a')
fen=Tk()
fen.title('SNAKE')
can =Canvas(fen, width=1000, height=500, bg='grey')
can.pack(side=TOP)
bou1=Button(fen, text='Start game', command=start)
bou1.pack(side=LEFT,padx=4)
bou2=Button(fen, text='Quit', command=fen.destroy)
bou2.pack(side=LEFT,padx=4)
bou3=Button(fen, text='Restart', command=restart)
bou3.pack(side=LEFT,padx=4)
bou6=Button(fen,text='Restart level',command=restart_level)
bou6.pack(side=LEFT,padx=4)
bou4=Button(fen,text='Pause',command=flagstop)
bou4.pack(side=LEFT,padx=4)
bou5=Button(fen,text='Help',command=helpb)
bou5.pack(side=LEFT,padx=4)
bou7=Button(fen, text='Info',command=info)
bou7.pack(side=LEFT,padx=4)
bou8=Button(fen,text='Changer de serpent',command=userchange)
bou8.pack(side=LEFT,padx=4)
bou10=Button(fen,text='Classement\n Statistiques',command=fenclass)
bou10.pack(side = LEFT,padx=4)
label=Label(fen)
label.pack(side=LEFT,padx=4)
lcrono=Label(fen)
lcrono.pack(side=LEFT,padx=4)
luser=Label(fen)
luser.pack(side=LEFT)

fen.bind("<Up>",goup)
fen.bind("<Down>",godown)
fen.bind("<Right>",goright)
fen.bind("<Left>",goleft)
fen.bind('<Return>',start)
fen.bind('<p>',flagstop)
fen.bind('<Alt-F12>',niveauup)
fen.bind('<r>',restart)
fen.bind('<l>',restart_level)
fen.bind('<w>',winmove)

while i<ncarre:
    carre = can.create_rectangle(xo,yo,xo+15,yo+15, fill='pink')
    liste.append([carre,xo,yo])
    i=i+1
    xo=xo+15
while u<nr:
    p=randrange(1000)
    m=randrange(500)
    cercle=can.create_oval(p,m,p+20,m+20,fill='green')
    listecercle.append([cercle,p,m])
    u=u+1

tniveau=can.create_text(500,20,anchor=CENTER,text='Niveau '+str(niveau),fill='blue',font='Arial 15')
wintext=can.create_text(500,100,anchor=CENTER,fill='blue',font='Arial 40 bold')
fen.after(50,userf)
fen.mainloop()
                                                                                                                                                                                                                                                                                                                                       
