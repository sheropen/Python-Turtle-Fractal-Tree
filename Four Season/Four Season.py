import turtle
import random
import math
autumn = ['deep pink','light pink','pink','hot pink']
summer = ['dark green','green','light green','medium sea green']
spring = ['orange','gold','orange red','gold','#B8860B']
winter = ['#F0F8FF','#F0FFFF','#00BFFF','#87CEEB','#87CEFA']
winterg = ['#F0F8FF','#F0FFFF','#87CEEB','#87CEFA']
ground = ['saddle brown','sienna','chocolate','peru','gold']
def move(p):
    t.pu(),t.goto(p),t.pd()

def reset(p,h):
    move(p),t.seth(h)

def flower(n,cset):
    pos = t.pos()
    hd = t.heading()
    area = l0*(8-n)/10
    cnt = (8-n)*20
    if(n == 2):
        cnt = 2*20
    for i in range(cnt):
        reset(pos,hd)
        c = random.choice(cset)
        tx = random.uniform(-area,area)
        ty = random.uniform(-area,area)
        move(pos+(tx,ty))
        if(cset == winter):
            t.pencolor = '#00BFFF'
            t.fillcolor(c)
            t.begin_fill()
            t.circle(5)
            t.end_fill()
        else:
            t.dot(5,c)
def drop_flower(x1,y1,x2,y2,cnt = 500,cset = autumn):
    for i in range(cnt):
        c = random.choice(cset)
        tx = random.uniform(x1,x2)
        ty = random.uniform(y1,y2)
        move((tx,ty))
        t.dot(5,c)
def branch(w,l,pre=True,color ="black"):
    if(pre):
        t.pencolor(color)
        t.pensize(0.1)
        hd = t.heading()
        t.right(90)
        deg = 1.5
        t.fillcolor(color)
        t.begin_fill()
        t.forward(w/2)
        t.left(90+deg)
        t.forward(l)
        t.left(90-deg)
        w2 = w - l*2*math.sin(math.radians(deg))
        t.forward(w2/2)
        pos = t.pos()
        t.forward(w2/2)
        t.lt(90-deg)
        t.forward(l)
        t.lt(90+deg)
        t.forward(w/2)
        t.end_fill()
        reset(pos,hd)
    else:
        hd = t.heading()
        t.pu()
        t.right(90)
        deg = 1.5
        t.forward(w/2)
        t.left(90+deg)
        t.forward(l)
        t.left(90-deg)
        w2 = w - l*2*math.sin(math.radians(deg))
        t.forward(w2/2)
        t.pd()
        t.seth(hd)
    
def tree(w,l,n=1,f='m',pre=True,color='peru'): 
    if n > 7:
        return
    hd = t.heading()
    l1 = l-(l0-100)/9
    pre1 = False
    if(pre):
        pre1 = True
    if n == 3:
        p1 = random.randint(1,3)
        if p1 == 1:
            pre1 = True
    if n == 4:
        p1 = random.randint(1,5)
        if p1 == 1:
            pre1 = True
    branch(w,l,pre1,color)
    pos = t.pos()
    ##Mark Down Branch pos
    if n >= 2:
        tmp = [pos,n]
        flower_pos.append(tmp)
    deg = 0
    ##Right branch
    if(n == 1):
        deg = random.randint(20,25)
    if(f=='r'):
        if(n==2):
            deg = random.randint(35,45)
        elif(n==3):
            deg = random.randint(25,30) 
        else:
            deg = random.randint(20,25)
    elif(f=='l'):
        deg = random.randint(40,45)
    rat = random.uniform(0.65,0.70)
    reset(pos,hd)
    t.right(deg)
    tree(w*rat,l1,n+1,'r',pre,color)
    ##Mid
    if(f == 'm'):
        #Right
        rat = random.uniform(0.50,0.55)
        deg = random.randint(1,2)
        reset(pos,hd)
        t.right(deg)
        tree(w*rat,l1,n+1,'r',pre,color)
        #Left
        rat = random.uniform(0.50,0.55)
        deg = random.randint(1,2)
        reset(pos,hd)
        t.left(deg)
        tree(w*rat,l1,n+1,'l',pre,color)
    ##Left Branch
    if(n == 1):
        deg = random.randint(20,25)
    if(f=='l'):
        if(n==2):
            deg = random.randint(35,45)
        elif(n==3):
            deg = random.randint(25,30) 
        else:
            deg = random.randint(20,25)
    elif(f=='r'):
        deg = random.randint(40,45)
    rat = random.uniform(0.65,0.70)    
    reset(pos,hd)
    t.left(deg)
    tree(w*rat,l1,n+1,'l',pre,color)

##Subtree
def subtree(w,l,n=1,f='m',pre=True,color='peru'): 
    if n > 7:
        return
    hd = t.heading()
    l1 = l-(l0-100)/9
    pre1 = False
    branch(w,l,pre1,color)
    pos = t.pos()
    ##Mark Down Branch pos
    if n >= 3:
        tmp = [pos,n]
        flower_pos.append(tmp)
    deg = 0
    ##Right branch
    if(n == 1):
        deg = random.randint(15,20)
    if(f=='r'):
        if(n==2):
            deg = random.randint(25,30)
        elif(n==3):
            deg = random.randint(20,25) 
        else:
            deg = random.randint(15,20)
    elif(f=='l'):
        deg = random.randint(25,30)
    rat = random.uniform(0.50,0.65)
    reset(pos,hd)
    t.right(deg)
    subtree(w*rat,l1,n+1,'r',pre,color)
    ##Mid
    if(f == 'm'):
        #Right
        rat = random.uniform(0.40,0.45)
        deg = random.randint(1,2)
        reset(pos,hd)
        t.right(deg)
        subtree(w*rat,l1,n+1,'r',pre,color)
        #Left
        rat = random.uniform(0.40,0.45)
        deg = random.randint(1,2)
        reset(pos,hd)
        t.left(deg)
        subtree(w*rat,l1,n+1,'l',pre,color)
    ##Left Branch
    if(n == 1):
        deg = random.randint(15,20)
    if(f=='l'):
        if(n==2):
            deg = random.randint(25,30)
        elif(n==3):
            deg = random.randint(20,25) 
        else:
            deg = random.randint(15,20)
    elif(f=='r'):
        deg = random.randint(25,30)
    rat = random.uniform(0.50,0.65)    
    reset(pos,hd)
    t.left(deg)
    subtree(w*rat,l1,n+1,'l',pre,color)
    

##Initialize        
border = 2500 #Size of the picture
turtle.setworldcoordinates(-border,-border,border,border)
t = turtle.Turtle()
turtle.tracer(0)
l0 = border/5

##Root pos
reset((0,-border/2),90)
flower_pos = []
origin = [0,0]
tree(l0/5,l0,1,'m',True,'saddle brown')
for i in flower_pos:
    cs = []
    xp = i[0][0] - origin[0]
    yp = i[0][1] - origin[1]
    theta = math.degrees(math.atan(abs(yp)/xp))
    if(-90 < theta < -30):
        cs = summer
    elif(-30 <= theta < 0):
        cs = autumn
    elif(0 <= theta < 30):
        continue
    elif(30 <= theta < 90):
        cs = spring
    move(i[0])
    flower(i[1],cs)
    
##Subtree
reset((0,-border/2),90)
flower_pos = []
subtree(l0/15,l0,1,'m',True,'saddle brown')
for i in flower_pos:
    cs = []
    xp = i[0][0] - origin[0]
    yp = i[0][1] - origin[1]
    theta = math.degrees(math.atan(abs(yp)/xp))
    if(-90 < theta < -30):
        cs = summer
    elif(-30 <= theta < 0):
        cs = autumn
    elif(0 <= theta < 30):
        continue
    elif(30 <= theta < 90):
        cs = spring
    move(i[0])
    flower(i[1],cs)
#branch(border/25,border/5)
'''
reset((0,-border/2),90)
flower_pos = []
subtree(l0/15,l0,1,'m',False,'peru')'''
a1 = -3*l0
b1 = -border/2 
a2 = 3*l0
b2 = -border/2 +l0*2 
drop_flower(a1,b1,a1/2,b2+l0*2-40,90,autumn)
drop_flower(a1/2,b1,0,b2+l0*2-40,90,summer)
drop_flower(0,b1,a2/2,b2+l0*2-40,90,spring)
drop_flower(a2/2,b1,a2,b2+l0*2-40,90,winter)

##Floor
a1 = -3*l0
b1 = -border/2-l0/3
a2 = 3*l0
b2 = -border/2 
#drop_flower(-border-20,-border/2-l0/3,-3*l0,-border/2,300)
drop_flower(a1,b1,a2,b2,2000,ground)
drop_flower(a1,b1,a1/2,b2,30,autumn)
drop_flower(a1/2,b1,0,b2,30,summer)
drop_flower(0,b1,a2/2,b2,30,spring)
drop_flower(a2/2,b1,a2,b2,30,winterg)
#drop_flower(3*l0,-border/2-l0/3,border,-border/2,300)

##Finish
t.hideturtle()
turtle.update()
turtle.done()
