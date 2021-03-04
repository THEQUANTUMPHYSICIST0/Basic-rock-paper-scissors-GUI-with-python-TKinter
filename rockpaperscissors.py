import tkinter as tk
tkroot=tk.Tk()
import time
root=tk.Canvas(tkroot, width=500, height=500)
root.pack()
errortext=None
backbutton=None
backtext=None
import random
onstartscreen=True
madlibscreen=False
startscreen=root.create_rectangle(120, 189,382, 236, fill='#ADD8E6')
starttext=root.create_text(252, 215, text='Welcome to Rock-Paper-Scissors!',font=("Helvetica", "11", 'bold'))
playbutton=root.create_rectangle(182, 267,323, 299, fill='#ADD8E6')
playtext=root.create_text(253, 285,text='Play',font=("Helvetica", "11", 'bold'))
madlibsbutton=root.create_rectangle(405, 413,491, 445, fill='#ADD8E6')
madlibstext=root.create_text(446, 430, text='Play Madlibs instead',font=("Helvetica", "6", 'bold'))
startscreenobjs=[startscreen,starttext,playbutton,playtext,madlibsbutton,madlibstext]
onplayscreen=False
r1=None
r2=None
r3=None
def playscreen():
    global onplayscreen,r1,r2,r3
    r1=root.create_oval(173, 165, 173+50, 165+50, fill='gray')
    r2=root.create_oval(272, 164,272+50, 164+50, fill='black')
    r3=root.create_oval(227, 254,227+50, 254+50,  fill='white')
    onplayscreen=True
gameover=False
import math
def click(event):
    global onstartscreen,madlibscreen,errortext,backbutton,backtext,startscreenobjs,onplayscreen,r1,r2,r3
    x=event.x
    y=event.y
    print(str(x)+','+' '+str(y))
    if onplayscreen:
        gameover=False
        if math.sqrt((173+25-x)**2+(165+25-y)**2)<=25:
            r=1
        if math.sqrt((272+25-x)**2+(164+25-y)**2)<=25:
            r=2
        if math.sqrt((227+25-x)**2+(254+25-y)**2)<=25:
            r=3
        else:
            return
        x=random.randint(1,3)
        # 1 beats 2, 2 beats 3, 3 beats 1
        if r==1 and x==2:
            gameovertext=root.create_rectangle(0,0,501,501,fill='white')
            gameovertext2=root.create_text(250,250,text="You win!")
            root.update()
            time.sleep(2)
            gameover=True
            
        if r==2 and x==1:
            gameovertext=root.create_rectangle(0,0,501,501,fill='white')
            gameovertext2=root.create_text(250,250,text="You lose!")
            root.update()
            time.sleep(2)
            gameover=True
            
        if r==2 and x==3:
            gameovertext=root.create_rectangle(0,0,501,501,fill='white')
            gameovertext2=root.create_text(250,250,text="You win!")
            root.update()
            time.sleep(2)
            gameover=True
            
        if r==3 and x==2:
            gameovertext=root.create_rectangle(0,0,501,501,fill='white')
            gameovertext2=root.create_text(250,250,text="You lose!")
            root.update()
            time.sleep(2)
            gameover=True
            
        if r==3 and x==1:
            gameovertext=root.create_rectangle(0,0,501,501,fill='white')
            gameovertext2=root.create_text(250,250,text="You win!")
            root.update()
            time.sleep(2)
            gameover=True
            
        if r==1 and x==3:
            gameovertext=root.create_rectangle(0,0,501,501,fill='white')
            gameovertext2=root.create_text(250,250,text="You lose!")
            root.update()
            time.sleep(2)
            gameover=True
        
        if gameover:
            onstartscreen=True
            madlibscreen=False
            startscreen=root.create_rectangle(120, 189,382, 236, fill='#ADD8E6')
            starttext=root.create_text(252, 215, text='Welcome to Rock-Paper-Scissors!',font=("Helvetica", "11", 'bold'))
            playbutton=root.create_rectangle(182, 267,323, 299, fill='#ADD8E6')
            playtext=root.create_text(253, 285,text='Play',font=("Helvetica", "11", 'bold'))
            madlibsbutton=root.create_rectangle(405, 413,491, 445, fill='#ADD8E6')
            madlibstext=root.create_text(446, 430, text='Play Madlibs instead',font=("Helvetica", "6", 'bold'))
            startscreenobjs=[startscreen,starttext,playbutton,playtext,madlibsbutton,madlibstext]
            onplayscreen=False
            root.delete(gameovertext)
            root.delete(gameovertext2)
            root.delete(r1)
            root.delete(r2)
            root.delete(r3)
        
    if onstartscreen:
        if 182<x<323 and 267<y<299:
            onstartscreen=False
            for x in startscreenobjs:
                root.delete(x)
        if 405<x<491 and 413<y<445:
            for x in startscreenobjs:
                root.delete(x)
            madlibscreen=True
            errortext=root.create_text(253, 235,text='Sorry! That has not been implemented yet.',font=("Helvetica", "11", 'bold'))
            backbutton=root.create_rectangle(182, 267,323, 299, fill='#ADD8E6')
            backtext=root.create_text(253, 285,text='Back',font=("Helvetica", "11", 'bold'))
    if not onstartscreen:
        if madlibscreen:
            onstartscreen=True
            root.delete(errortext)
            root.delete(backbutton)
            root.delete(backtext)
            startscreen=root.create_rectangle(120, 189,382, 236, fill='#ADD8E6')
            starttext=root.create_text(252, 215, text='Welcome to Rock-Paper-Scissors!',font=("Helvetica", "11", 'bold'))
            playbutton=root.create_rectangle(182, 267,323, 299, fill='#ADD8E6')
            playtext=root.create_text(253, 285,text='Play',font=("Helvetica", "11", 'bold'))
            madlibsbutton=root.create_rectangle(405, 413,491, 445, fill='#ADD8E6')
            madlibstext=root.create_text(446, 430, text='Play Madlibs instead',font=("Helvetica", "6", 'bold'))
            startscreenobjs.append(startscreen)
            startscreenobjs.append(starttext)
            startscreenobjs.append(playbutton)
            startscreenobjs.append(playtext)
            startscreenobjs.append(madlibsbutton)
            startscreenobjs.append(madlibstext)
            madlibscreen=False
            
        else:
            playscreen()
            


root.bind("<Button-1>", click)
