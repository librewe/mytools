import turtle as tt
import os
import time
'''
物值对照表：-1:'i',0：blank,1:box,2:block,[*]:Box
'''
n=3
d0=300;x0=y0=-0.5*d0
Dic={-1:'i',0:'blank',1:'box',2:'block',-2:'i_end',-3:'box_end'}
cDic={-1:'red',0:'white',1:'yellow',2:'black',-2:'red',-3:'yellow'}
dic={'r':1,'l':-1,'u':-n,'d':n}
di=dic['r']
flag=False;flag1=0
TABLE=[[-1,0,0,
        0,1,0,
        [0,0,[0,0,0,1,1,1,2,2,2],0,0,0,2,2,2],0,2],2]
TABLE1=[[[2,2,2,0,-1,0,0,0,0],[2,-2,-3,0,2,0,0,2,0],2,
        [0,[2,2,2,0,0,2,2,0,2],0,0,0,0,2,2,2],[0,2,0,0,0,0,2,2,0],2,
        2,2,2],2]
TABLE2=[[[2,2,2,0,-1,0,0,0,0],[2,-2,-3,0,2,0,0,2,0],2,
        [0,[2,2,2,0,0,2,2,0,2],0,0,0,0,2,2,2],[0,2,0,0,0,0,2,2,0],2,
        2,2,2],2]

class pos(list):
    def __init__(self,p):
        self.p=p
    def __str__(self):
        return str(self.p)
    def __len__(self):
        return len(self.p)
    def __getitem__(self,key):
        res=list.__getitem__(self.p,key)
        return res
    def __setitem__(self,key,value):
        res=list.__setitem__(self.p,key,value)
        return res #?
    def __iadd__(self,other):
        res=list.__iadd__(self.p,other)
        return res
    def ne(self,di=di,mode=0):
        a=list(self.p)#...直接赋self.p会导致作为引用,毕竟还在自己里面
        for i in range(-1,-len(a)-1,-1):
            if i !=-len(a):
                a[i]+=di
            else:
                res=pos([1])#是pos
                return res
            if (di in [-1,1] and(a[i]-di)//3 != a[i]//3):
                if mode==0:
                    a[i]=a[i]-3*di
                elif mode==1:#?
                    break
            elif(a[i] not in range(9)):
                a[i]=a[i]-3*di#超出范围不应该响应吗(at while)
            else:di=0;break
        a=pos(a)
        res=table[a]
        if isinstance(res,str):#echo：Table.getitem时超出层级
            res=int(res)
            a=a[:res]
            a=pos(a)
            res=table[a]
        if a:
            return a
        else:
            print("ne_out of range",a)
            return self
    def tne(self,di=di,mode=0):
        A=self.ne(di,mode)#?
        if isinstance(table[A],list):
            a=A.p+[4-2*di]
            a=pos(a)
            res=a.tne(di,1)
            return res
        else:
            return A

class Table(list):
    def __init__(self,t):
        self.t=t
    def __str__(self):
        return str(self.t)
    def __getitem__(self, key):
        t=list(self.t)
        cnt=0
        for i in key.p:
            if isinstance(t[i],list)and cnt<=len(key):
                t=t[i];cnt+=1
            else:t=t[i];cnt+=1;break
        if len(key)>cnt:
            return str(cnt)
        return t
    def __setitem__(self, key, value):
        p=self.t;key=key.p
        s=key[0]
        p=Table(p[s])
        if len(key)>1:
            key=pos(key[1:])
            p[key]=value
            self.t[s]=p.t
        else:
            self.t[s]=value

        
def Move(di):
    global i_pos
    print('#M',i_pos)
    ne=i_pos.ne(di)
    tne=i_pos.tne(di)
    ne_tne=ne.tne(di)
    if table[ne]==0:
        table[i_pos]=0
        table[ne]=-1#move()
        i_pos=ne
    elif len(ne)==len(i_pos):
        if table[ne]!=2:
            if table[ne_tne]==0:
                table[ne_tne]=table[ne]#push()
                table[ne]=-1
                table[i_pos]=0
                i_pos=ne
            elif table[tne]==0:
                table[tne]=-1#move()tne
                table[i_pos]=0
                i_pos=tne#tne
            else:print("neither",ne,tne)
    tt.tracer(False)
    draw()
    tt.tracer(True)

def draw(p=pos([0]),d=0):
    r,c=divmod(p[-1],3)
    x=d0/3**d
    if isinstance(table[p],int): #and d<5
        tt.penup()
        temp=tt.pos()
        tt.goto(temp+((r)*x,(c)*x))#tt.goto((r-1)*x,(c-1)*x)
        tt.pendown()
        color=cDic[table[p]]
        if isinstance(ctable[p],int)and ctable[p]<=-2 and table[p]!=-1:
            drawf(cDic[ctable[p]],x,ctable[p])
            global flag1
            if flag1<3:#...
                table[p]=0;flag1+=1
        else:
            drawf(color,x)
    elif isinstance(table[p][0],list) or len(table[p])>1:
        temp=tt.pos()
        for i in range(9):
            p.p+=[i]
            tt.penup()
            tt.goto(temp+((r)*x,(c)*x))
            draw(p,d+1)
            p.p=p[:-1]
        tt.penup()
        tt.goto(temp)
def drawf(color="white",x=d0,pattern=0):
    if pattern==0:
        tt.fillcolor(color)
        tt.begin_fill()
        for _ in range(4):
          tt.forward(x)
          tt.right(-90)
        tt.end_fill()
    elif pattern<=-2:
        tt.fillcolor("white")
        tt.begin_fill()
        for _ in range(4):
          tt.forward(x)
          tt.right(-90)
        tt.end_fill()
        tt.pencolor(color)
        temp=tt.pos()
        tt.penup()
        tt.goto(temp+(0.25*x,0.25*x))
        tt.pendown()
        for _ in range(4):
          tt.forward(x/2)
          tt.right(-90)
        tt.penup()
        tt.goto(temp)
        tt.pencolor('black')

def dir_r():
    global di
    di=dic['r']
    flag=True
    Move(di)
def dir_l():
    global di
    di=dic['l']
    flag=True
    Move(di)
def dir_u():
    global di
    di=dic['u']
    flag=True
    Move(di)
def dir_d():
    global di
    di=dic['d']
    flag=True
    Move(di)
def register_event():
    for key,f in {"Up": dir_r, "Down": dir_l, "Left": dir_u, "Right": dir_d}.items():
        tt.onkeypress(f, key)
    tt.listen()



table=Table(TABLE1)
ctable=Table(TABLE2)
i_pos=pos([0,0,4])
print("@",table)

tt.screensize(canvwidth=800, canvheight=600, bg=None)
tt.setup(width=0.4,height=0.6)
tt.delay(delay=None)

tt.speed(0)
tt.pensize(1)
tt.pencolor("black")

tt.penup()
tt.goto(x0,y0)

tt.tracer(False)
draw()
register_event()

tt.mainloop()