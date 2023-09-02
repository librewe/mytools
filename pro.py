def drop(lis,n):
    c=lis.pop(n);c1=[i for i in lis];lis.insert(n,c)
    return c1
def frange(start,stop,step):
    res=[]
    while start<=stop:
        res.append(float('%.2f'%(start)))
        start+=step
    return res

class complex:
    def __init__(self,re,im):
        self.re=re
        self.im=im
    def __str__(self):
        if self.im==0:
            return str(self.re)
        elif self.im>0:
            return str(self.re)+"+"+str(self.im)+"i"
        else:
            return str(self.re)+str(self.im)+"i"
    def __add__(self,other):
        if isinstance(other,complex):
            return complex(self.re+other.re,self.im+other.im)
        else:
            return complex(self.re+other,self.im)
    def __radd__(self,other):
        return complex(self.re+other,self.im)
    def __sub__(self,other):
        if isinstance(other,complex):
            return complex(self.re-other.re,self.im-other.im)
        else:
            return complex(self.re-other,self.im)
    def __rsub__(self,other):
        return complex(other-self.re,self.im)
    def __neg__(self):
        return 0-self
    def __mul__(self,other):
        if isinstance(other,Num):
            if isinstance(other,complex):
                return complex(self.re*other.re-self.im*other.im,self.re*self.im+other.re*other.im)
            else:
                return complex(self.re*other,self.im*other)
        else:
            res=other*self
            return res
    def __rmul__(self,other):
        if isinstance(other,complex):
            return complex(self.re*other.re-self.im*other.im,self.re*self.im+other.re*other.im)
        else:
            return complex(self.re*other,self.im*other)
    def __pow__(self, other):
        if other ==0:
            return complex(1,0)
        elif other>0:
            res=self
            for i in range(other-1):
                res=res*self
            return res
    def __truediv__(self, other):
        if isinstance(other,Num):
            if isinstance(other,complex):
    #             if other!=0:?
                res=self*other.conjugate()
                return res/((other.modulus)**2)
            else:
                return complex(self.re/other,self.im/other)
        else:
            res=other*self
            return res
    def __eq__(self,other):
        if isinstance(other,complex):
            return (self.re==other.re) and self.im==other.im
        elif self.im==0:
            return self.re==other
        else:
            return False
    def modulus(self):
        return (self.re**2+self.im**2)**0.5
    def conjugate(self):
        return complex(self.re,-self.im)

class vector:
    def __init__(self,vec=None):
        self.vec=vec
    def __str__(self):
        return str(self.vec)
    def __add__(self,avec):
        try:
            res=vector([self.vec[i]+avec.vec[i] for i in range(len(self.vec))])
            return res
        except:
            print("报错：vector规格不合适")
    def __sub__(self,avec):
        try:
            res=[self.vec[i]-avec.vec[i] for i in range(len(self.vec))]
            return vector(res)
        except:
            print("报错：vector规格不合适")
    def __mul__(self,avec):
        if not isinstance (avec,vector):
            return vector([self.vec[i]*avec for i in range(len(self.vec))])
        else:
            try:
                res=[self.vec[i]*avec.vec[i] for i in range(len(self.vec))]
                return sum(res)
            except:
                print("报错：vector规格不合适")
    def __rmul__(self,avec):
        if not isinstance (avec,vector):
            return vector([self.vec[i]*avec for i in range(len(self.vec))])
        else:print("报错：vector.__rmul__")
    def __len__(self):
        return len(self.vec)
    def __eq__(self,other):
        if isinstance(other,vector):
            return self.vec==other.vec
        elif self*self==0 and other==0:
            return True
        else:return False
    def modulus(self):
        res=[self.vec[i]**2 for i in range(len(self.vec))]
        return sum(res)
    def innerproduct(self,avec,p=lambda x,y: x*y):
        res=[p(self.vec[i],avec.vec[i]) for i in range(len(self.vec))]
        return res
    def isrelatedto(self,vectors):
        a=matrix([i.vec for i in vectors])
#         if a.det()!=0:
        c=matrix([self.vec])
        x1=c*(a.transpose())
        x2=(a*a.transpose()).verse()
#         print(a,c,x1,x2)#c,x*a,res)
        x=x1*x2
        res=c-x*a
        if res !=0:
            return x
        else: return False

class vecto(vector):
    def __add__(self,avec):
        m=max(len(self),len(avec))
        self.vec=self.vec+[0]*(m-len(self))
        avec.vec=avec.vec+[0]*(m-len(avec))
        res=[self.vec[i]+avec.vec[i] for i in range(len(self.vec))]
        res=vecto(res)
        return res
    def __radd__(self,n):
        if n==0:return self
    def __sub__(self,avec):
        m=max(len(self),len(avec))
        self.vec=self.vec+([0]*(m-len(self)))
        avec.vec=avec.vec+([0]*(m-len(avec)))
        res=[self.vec[i]-avec.vec[i] for i in range(len(self.vec))]
        res=vecto(res)
        return res
    def __mul__(self,avec):
        if not isinstance(avec,vecto):
            return vecto([self.vec[i]*avec for i in range(len(self.vec))])
        else:
            try:
                res=[self.vec[i]*avec.vec[i] for i in range(len(self.vec))]
                return sum(res)
            except:
                print("报错：vecto规格不合适")
    def __rmul__(self,avec):
        if not isinstance(avec,vector) and not isinstance(avec,vecto):
            return vecto([self.vec[i]*avec for i in range(len(self.vec))])
        else:print("报错：vecto.__rmul__")

#
class matrix:
    def __init__(self,mat=None):
        if isinstance (mat[0],vector):
            self.mat=[i for i in mat]
        else:
            self.mat=[vector(i) for i in mat]
    def __str__(self):
        print("[",end="",sep='');s=""
        for i in self.mat:
            s+=str(i)+"\n "
        print(s[0:-2],end="",sep='')
        print("]"+"\n",end="",sep='')
        return ""
#       我尽力了这换行空格不知道从哪里来的也不知道怎么去
#         return str([i.vec for i in self.mat])
    def __eq__(self,other):
        flag=True
        for i in self.mat:
            if i!=0:flag=False
        if isinstance(other,matrix):
            return self.mat==other.mat
        elif flag and other==0:
            return True
        elif isinstance(other,vector) and len(self.mat)==1 and other.vec==self.mat[0]:
            return True
        else:
            return False
    def __add__(self,amat):
        try:
            res=[self.mat[i]+amat.mat[i] for i in range(len(self.mat))]
            return matrix(res)
        except:
            print("报错：maxtrix规格不合适")
    def __radd__(self,n):
        if n==0:return self
    def __sub__(self,amat):
        try:
            res=[self.mat[i]-amat.mat[i] for i in range(len(self.mat))]
            return matrix(res)
        except:
            print("报错：maxtrix规格不合适")
    def __mul__(self,amat):
        if not isinstance (amat,matrix):
            if len(self.mat)>1:
                res=[[(self.mat[i].vec[j]*amat) for j in range(len(self.mat[0]))]  for i in range(len(self.mat))]
            else:
#                 print(self,amat,"mark")
                res=[[self.mat[0].vec[0]*amat]]
        else:
#             print(self,amat,"mark")
            t=amat.transpose()
            res=[[self.mat[i]*t.mat[j] for j in range(len(t.mat))] for i in range(len(self.mat))]
        return matrix(res)

    def __rmul__(self,amat):
        if not isinstance (amat,matrix):
            res=matrix([(self.mat[i]*amat).vec  for i in range(len(self.mat))])
            return res
        else:
            print("报错：maxtrix规格不合适")        
    def __pow__(self, other):#[, modulo]?
        if other ==0:
            return I(len(self.mat))
        elif other>0:
            res=self
            for i in range(other-1):
                res=res*self
            return res
    def transpose(self):
        if len(self.mat)>1 or len(self.mat[0])>1:
            res=[[(self.mat[i].vec)[j] for i in range(len(self.mat))] for j in range(len(self.mat[0]))]
            return matrix(res)
        else:
            return matrix(self.mat)
    def transposed(self):
        self.mat=[vector([self.mat[i].vec[j] for i in range(len(self.mat))]) for j in range(len(self.mat[0].vec))]
    def submat(self,lis):
        if 0<len(lis[0])<=len(self.mat[0]) and 0<len(lis[1])<=len(self.mat):
            mat=[vector([self.mat[i].vec[j] for j in lis[0]]) for i in lis[1]]
            return matrix(mat)
        else:
            print("submat规格不合适")
    def det(self):
        m=len(self.mat);n=len(self.mat[0])
        if m==n:
            if m==1:
                return self.mat[0].vec[0]
            else:
                c1=[[i for i in range(n)] for i in range(n)]
                c11=[c1[i].pop(i) for i in range(n)]#which actually functions
                c2=[i for i in range(1,m)]
                res=[self.mat[0].vec[i]*((-1)**i)*(self.submat([c1[i],c2]).det()) for i in range(n)]
                return sum(res)
        else:
            print("maxtrix规格不合适")
    def company(self):
        c=[i for i in range(len(self.mat))]
        det=self.det()
        res=matrix([vector([self.submat([drop(c,i),drop(c,j)]).det()*(-1)**(i+j) for j in c]) for i in c])
        return res.transpose()
    def verse(self):
        try:
            if len(self.mat)>1:
                res=self.company()*(1/self.det())
                return res
            else:
                res=matrix([vector([1/self.mat[0].vec[0]])])
                return res
        except:
            print("不可逆")
    def eigenpol(self):
        return (I(len(self.mat))*polynomial([0,1])-self).det()

class I(matrix):
    def __init__(self,n):
        mat=[[0]*n for i in range(n)]
        for i in range(n):
            mat[i][i]=1
        matrix.__init__(self,mat)
        
class diag(matrix):
    def __init__(self,mats):
        if len(mats)==1:
            matrix.__init__(self,mats[0].mat)
        elif len(mats)>1:
            d1=mats[0]
            d2=diag(mats[1:])
            d1=[i.vec+[0]*len(d2.mat[0]) for i in d1.mat]
            d1=d1+[[0]*len(d1[0])]*len(d2.mat)
            d1=matrix(d1)
            d2=[[0]*(len(d1.mat[0])-len(d2.mat[0]))+i.vec for i in d2.mat]
            d2=[[0]*len(d1.mat)]*(len(d1.mat)-len(d2))+d2
            d2=matrix(d2)
            matrix.__init__(self,(d1+d2).mat)

#
class polynomial:
    def __init__(self,pol):
        if not isinstance(pol,vecto):
            self.pol=vecto(pol)
        else:self.pol=pol
        deg=len(self.pol)-1
        if deg>0:
            self.deg=deg
        elif self.pol.vec[0]!=0:
            self.deg=deg
        else:
            self.deg=-1e10
    def __str__(self,var="x"):
        s=""
        for i in range(len(self.pol)):
            try:flag1=self.pol.vec[i]>0
            except:flag1=self.pol.vec[i].re>0
            try:flag2=self.pol.vec[i]<0
            except:flag2=self.pol.vec[i].re<0
            if flag1:
                s="+"+str(self.pol.vec[i])+var+"^"+str(i)+s
            elif flag2:
                s=str(self.pol.vec[i])+var+"^"+str(i)+s
        if s[-3:]==var+"^0":s=s[:-3]
        if s=="":return "0"
        elif s[0]=="+":return s[1:]
        else:return s
    def __eq__(self,other):
        if isinstance(other,polynomial):
            return self.pol==other.pol
        elif self.deg<0 and other==0:
            return True
        else:return False
    def __add__(self,apol):
        if isinstance(apol,polynomial):
            res=self.pol+apol.pol
            return polynomial(res)
        else:return self+polynomial([apol])
    def __radd__(self,apol):
        return self+polynomial([apol])
    def __sub__(self,apol):
        if isinstance(apol,polynomial):
            res=self.pol-apol.pol
            return polynomial(res)
        else:return self-polynomial([apol])
    def __mul__(self,apol):
        if isinstance(apol,polynomial):
            if self.deg>=0:
#                 print(self.pol.vec[0])
                res=[vecto(([0]*i)+(self.pol.vec[i]*apol.pol).vec) for i in range(len(self.pol))]
                return polynomial(sum(res))
            else:return polynomial([0])
        elif isinstance(apol,matrix):
            return apol.__mul__(self)
        else:return polynomial([self.pol.vec[i]*apol for i in range(len(self.pol))])
    def __rmul__(self,apol):
        return polynomial([self.pol.vec[i]*apol for i in range(len(self.pol))])
    def __pow__(self, other):
        if other ==0:
            return polynomial([0,1])
        elif other>0:
            res=self
            for i in range(other-1):
                res=res*self
            return res
    def div(self,other):
        if other.pol.vec!=[0]:
            if isinstance(self.deg,int):
                if self.pol.vec==[0]*(self.deg+1):
                    return tuple([polynomial([0]),polynomial([0])])
                elif self.deg<other.deg:
                    return tuple([polynomial([0]),self])
                else:
                    k=self.pol.vec[-1]/other.pol.vec[-1]
                    q=[0]*(self.deg-other.deg+1)
                    q[-1]=k;q=polynomial(q)
                    res=tuple([q+(self-q*other).div(other)[0],(self-q*other).div(other)[1]])
                    return res
            else: return tuple([polynomial([0]),polynomial([0])])
    def at(self,x):
        res=[x**i*self.pol.vec[i] for i in range(self.deg+1)]
        return sum(res)
    def differentiate(self):
        res=[i*self.pol.vec[i] for i in range(self.deg+1)]
        if len(res)==1:return polynomial([0])
        else: return polynomial(res[1:])
    def solve(self,sp=0.1,de=0.001):
        if self.deg>1:
            for i in [-1,1]:
                for j in frange(0,50*i*sp,i*sp):
                    for k in frange(-1,1,sp):
                        res=complex(k,j)
                        if abs(self.at(res).modulus())<=10*de:
                            re=(self.div(polynomial([-res,1]))[0].solve())
                            re.append(res)
                            return re
        elif self.deg==1: return [-self.pol.vec[0]]
        else: print("unexpected")
    def __getattribute__(self,name):
        if name!="deg":
            return object.__getattribute__(self,name)
        else:
            vec=self.pol.vec
    #         if len(vec)==0:?
            if vec!=[0]*len(self.pol):
                i=len(self.pol)-1
                while(vec[i]==0): i-=1
                newvec=vec[:i+1]
                res=len(self.pol)-1
            else:
                newvec=[0]
                res=-1e10
            self.pol.vec=newvec
            self.deg=res
            return res

def maxgroup(vectors):
    for i in range(len(vectors)):
        if vectors[i].vec==[0]*len(vectors[0]):
            vectors.drop(i)
    res=[];res.append(vectors[0]);cnt=0
#         print(vectors[0].isrelatedto(res))
    while(len(res)<len(vectors[0]) and cnt<=len(vectors)):
        cnt+=1
        for i in range(max(len(res),len(vectors))):
            if vectors[i].isrelatedto(res):
                res.append(vectors[i])
                break
    return res

class LinearSpace:
    def __init__(self,base):
        if isinstance(base,int):
            self.dim=base
            self.base=[i for i in I(base).mat]
        else:
            b=[len(i) for i in base]
            if max(b)==min(b):
                self.dim=b[0]
                self.base=maxgroup(base)
            else:
                print("报错：base规格不合适")
    def __str__(self):
        for i in self.base:
            print(i)
        return ""
    def __add__(self,other):
        res=maxgroup(self.base+other.base)
        if len(res)==self.dim+other.dim:
            print("直和")
        return res
    

Num=(int,float,complex)
a=matrix([[2,1],[0,1]])
b=matrix([[1,2],[1,2]])
v1=vector([1,2,0])
v2=vector([1,0,0])
v3=vector([1,2,1])
x=polynomial([0,1])
c=complex(1,0)
f=x**2-2*x+1
print(f.div(x-1)[0])
print(f.solve())
for i in f.solve():
            print(i)
# print(f.solve())
# print(v1*v1,LinearSpace([v1,v2,v3]))

# d1,d2=complex(1,-2),complex(1,-2)
# print(a*(a.verse()))
# print(a.eigenpol().at(a))

# e=polynomial([1,2,1,-3]);print(e*e);print(e.differentiate().at(a))
# print(a**2+b**2+a*b+b*a,(a+b)**2)

