import turtle as tt
import os
import time
'''
物值对照表：-1:'i',0：blank,1:box,2:block,[*]:Box
'''
n=3
x0=150
Dic={-1:'i',0:'blank',1:'box',2:'block'}
cDic={-1:'red',0:'white',1:'yellow',2:'black'}
dic={'r':1,'l':-1,'u':-n,'d':n}
di=dic['r']
flag=False
TABLE=[[-1,0,0,
        0,0,0,
        [0,0,0,1,1,1,2,2,2],0,2]]

# class item:
#     def __init__(self,it):
#         if isinstance(it,item):
#             self.it=it
#         else: pass
#     def __call__(self,pos):
#         return 0
# # class box(item):
# #     ?
class pos(list):
    def __init__(self,p):
#         if not isinstance(p,pos): 
        self.p=p
#         else:pass
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
    def ne(self,di=di):
        a=list(self.p)#...直接赋self.p会导致作为引用
        print('#0',a)
        for i in range(-1,-len(a)-1,-1):
            a[i]+=di
            print('#1',a)
            if (di in [-1,1] and(a[i]-di)//3 != a[i]//3)or(a[i] not in range(9)):
                a[i]=a[i]-3*di
            else:di=0
        a=pos(a)
        print('#2',a,self)
        while(a):
#             try:
                res=table[a]
                break
#             except:
                a=a[:-1]
        if a:
            return a
        else:
            print("out of range")
            return self
    def tne(self,di=di):
        A=self.ne(di)
        print('#tne',self,A)
        if isinstance(table[A],list):
            a=A.p+[4-2*di]
            a=pos(a)
            res=a.tne(di)
        else:
            print(self,'ooo',A)
            return 1
                

class Table(list):
    def __init__(self,t):
        self.t=t
    def __str__(self):
        return str(self.t)
    def __getitem__(self, key):
        t=list(self.t)
        print("QAQ",t,key)
        for i in key.p:
            t=t[i]
#             print("$" ,t)
        if isinstance(t,list):
            pass
        return t
#         t=list(self.t)
#         key=key.p
#         s=key[0]
#         if len(key)>1:
#             t=Table(t[s])
#             key=pos(key[1:])
#             res=t[key]
#         else:
#             res=self.t
#         res=list.__getitem__(self.p,key)
#         return res
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
#         print(self.t)
#         p.__setitem__(p.t,key,value)

        
def Move(di):
#     print(i_pos,di)
    global i_pos
    ne=i_pos.ne(di)
    tne=i_pos.tne(di)
    print('o',tne,i_pos,i_pos.tne(di),'o')
    ne_tne=ne.tne(di)
#     print("#Move",i_pos,ne,tne,ne_tne)
    if table[ne]==0:
        table[ne]=-1#move()
        table[i_pos]=0
        i_pos=ne
    elif len(ne)==len(i_pos):
        if table[ne]!=2:
            print("#Move",i_pos,ne,tne,ne_tne)
            if table[ne_tne]==0:
                table[ne_tne]=table[ne]#push()
                table[ne]=-1
                table[i_pos]=0
                i_pos=ne
            elif table[tne]==0:
                table[ne]=-1#move()
                table[i_pos]=0
                i_pos=ne
    tt.tracer(False)
    draw()
    tt.tracer(True)
    

def draw(p=pos([0]),d=0):
    r,c=divmod(p[-1],3)
    x=x0/3**d
    print("*",p,table[p])
    if isinstance(table[p],int): #and d<5
        tt.penup()
        temp=tt.pos()
        tt.goto(temp+((r)*x,(c-2*(d-1))*x))#tt.goto((r-1)*x,(c-1)*x)
        tt.pendown()
        color=cDic[table[p]]
        drawf(color,x)
    elif isinstance(table[p][0],list) or len(table[p])>1:
        for i in range(9):
            p.p+=[i]
            tt.penup()
            tt.goto((r)*x,(c)*x)
#             time.sleep(1)
            draw(p,d+1)
            p.p=p[:-1]
def drawf(color="white",x=x0,pattern=0):
    tt.fillcolor(color)
    tt.begin_fill()
    for _ in range(4):
      tt.forward(x)
      tt.right(90)
    tt.end_fill()

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
    for key,f in {"Up": dir_u, "Down": dir_d, "Left": dir_l, "Right": dir_r}.items():
        tt.onkeypress(f, key)
    tt.listen()



table=Table(TABLE)
i_pos=pos([0,0])
t=i_pos.tne(3)
print("@",t,i_pos,table[i_pos],table)

tt.screensize(canvwidth=800, canvheight=600, bg=None)
tt.setup(width=0.4,height=0.6)
tt.delay(delay=None)

tt.speed(0)
tt.pensize(1)
tt.pencolor("black")

tt.tracer(False)
draw()
tt.tracer(True)
register_event()

# while(1):
#     if flag:
#         Move(di)
#         flag=False
#         tt.tracer(False)
#         draw()
#         tt.tracer(True)
#     else:
#         pass



#tt.goto(tt.pos()+(60,-60))
# tt.penup()
# tt.goto(-150,-120)
# tt.pensize(5)
# tt.pencolor("yellow")
# tt.fillcolor("red")  
# tt.begin_fill()
# for _ in range(5):
#   tt.fd(150)
#   tt.left(144)
# tt.end_fill()
tt.mainloop()

'''
while(flag):
    catch key
    Move
    checkend
    v_pos
    
'''
table=Table(TABLE)
i_pos=pos([0,0])
t=i_pos.tne(3)
print("@",t,i_pos,table[i_pos],table)

tt.screensize(canvwidth=800, canvheight=600, bg=None)
tt.setup(width=0.4,height=0.6)
tt.delay(delay=None)

tt.speed(0)
tt.pensize(1)
tt.pencolor("black")

tt.tracer(False)
draw()
tt.tracer(True)
register_event()

# while(1):
#     if flag:
#         Move(di)
#         flag=False
#         tt.tracer(False)
#         draw()
#         tt.tracer(True)
#     else:
#         pass



#tt.goto(tt.pos()+(60,-60))
# tt.penup()
# tt.goto(-150,-120)
# tt.pensize(5)
# tt.pencolor("yellow")
# tt.fillcolor("red")  
# tt.begin_fill()
# for _ in range(5):
#   tt.fd(150)
#   tt.left(144)
# tt.end_fill()
tt.mainloop()

'''
while(flag):
    catch key
    Move
    checkend
    v_pos
    
'''
