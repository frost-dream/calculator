from tkinter import Tk,Button,Label,mainloop
from math import sqrt,sin,cos,tan,log,factorial
l="  "
a=Tk()
t=Label(a,font=(None,30))
t.place(x=15,y=60)
a.geometry("475x500")
b=[0,1,2,3,4,5,6,7,8,9,".","=","sin","cos","C","-","+","÷","×","<=","√","yX","n!","log","tan","cot"]
c=[10,410,10,330,75,330,140,330,10,250,75,250,140,250,10,170,75,170,140,170,140,410,400,330,270,250,335,250,270,170,205,410,205,330,205,170,205,250,335,170,270,410,270,330,400,170,400,250,335,330,335,410]
d=[125,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60]
f=[75,75,75,75,75,75,75,75,75,75,75,155,75,75,75,75,75,75,75,75,75,75,75,75,75,75]
e=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,"yellow",None,None,None,None,None,None,None,None,None,None,None]
g=[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,25,20,20,20,20,20,20,20,20,20,20]
h=["<Key-^>","<Key-minus>","<Key-+>","<Key-*>","<Key-/>","<Key-.>","<Key-0>","<Key-1>","<Key-2>","<Key-3>","<Key-4>","<Key-5>","<Key-6>","<Key-7>","<Key-8>","<Key-9>","<Key-Delete>","<Key-BackSpace>","<Key-Return>"]
def v():
    c2("0")
def w():
    c2("1")
def x():
    c2("2")
def y():
    c2("3")
def z():
    c2("4")
def k():
    c2("5")
def a1():
    c2("6")
def a2():
    c2("7")
def a3():
    c2("8")
def a4():
    c2("9")
def a5():
    c2(".")
def a6():
    global l
    try:
        if l[-2]=="(":
            l=l[:-6]
        elif l[-1]in["÷","×","+","-","^","."]:
            l=l[:-1]
        l=l[2:]
        s=""
        q=""
        n=""
        a15=0
        for i in range(len(l)):
            if a15==0:
                if l[i]in["÷","×","+","-","^"]:
                    if q!="":
                        if n=="÷":
                            if float(q)==0:
                                l="0"
                            else:
                                s=str(float(s)/float(q))
                            q=""
                        elif n=="×":
                            s=str(float(s)*float(q))
                            q=""
                        elif n=="+":
                            s=str(float(s)+float(q))
                            q=""
                        elif n=="-":
                            s=str(float(s)-float(q))
                            q=""
                        else:
                            s=str(float(s)**float(q))
                            q=""
                    n=l[i]
                elif l[i]in["s","c","t","l","n","√"]:
                    if l[i]=="n":
                        i+=3
                        a15=3
                    elif l[i]=="√":
                        i+=2
                        a15=2
                    else:
                        i+=4
                        a15=4
                    a10=""
                    while True:
                        a10+=l[i]
                        i+=1
                        if l[i]==")":
                            break
                    a15+=len(a10)
                    if l[i-len(a10)-2]=="n":
                        if l[i-len(a10)-3]=="i":
                            a10=sin(float(a10))
                        else:
                            a10=tan(float(a10))
                    elif l[i-len(a10)-2]=="t":
                        a10=cos(float(a10))/sin(float(a10))
                    elif l[i-len(a10)-2]=="s":
                        a10=cos(float(a10))
                    elif l[i-len(a10)-2]=="!":
                        if float(a10)==int(float(a10)):
                            a10=factorial(int(float(a10)))
                        else:
                            0/0
                    elif l[i-len(a10)-2]=="g":
                        a10=log(int(float(a10)))
                    else:
                        a10=sqrt(float(a10))
                    if s=="":
                        s=str(a10)
                    else:
                        q=str(a10)
                else:
                    if n=="":
                        s+=l[i]
                    else:
                        q+=l[i]
            else:
                a15-=1
        if q=="":
            l=s
        elif n=="÷":
            if float(q)==0:
                l="0"
            else:
                l=str(float(s)/float(q))
        elif n=="×":
            l=str(float(s)*float(q))
        elif n=="-":
            l=str(float(s)-float(q))
        elif n=="+":
            l=str(float(s)+float(q))
        else:
            l=str(float(s)**float(q))
        if float(l)==int(float(l)):
            l=str(int(float(l)))
        l="  "+l
        if len(l)>20:
            t.configure(text=l[len(l)-20:])
        else:
            t.configure(text=l)
    except:
        l="  "
        t.configure(text="  Error")
def a7():
    c2("sin()")
def a8():
    c2("cos()")
def a9():
    global l
    l="  "
    t.configure(text=l)
def a0():
    c2("-")
def b1():
    c2("+")
def b0():
    c2("÷")
def b2():
    c2("×")
def b3():
    global l
    if len(l)!=2:
        if l[-1]==")"and l[-2]!="(":
            l=l[:-2]+")"
        else:
            l=l[:-1]
        if len(l)>20:
            t.configure(text=l[len(l)-20:])
        else:
            t.configure(text=l)
def b4():
    c2("√")
def b5():
    c2("yX")
def b6():
    c2("n!()")
def b7():
    c2("log()")
def b8():
    c2("tan()")
def b9():
    c2("cot()")
u=[v,w,x,y,z,k,a1,a2,a3,a4,a5,a6,a7,a8,a9,a0,b1,b0,b2,b3,b4,b5,b6,b7,b8,b9]
def j(k):
    if k.char=="*":
        k.char="×"
    elif k.char=="/":
        k.char="÷"
    c2(k.char)
def c2(k):
    global l
    if k in["÷","×","+","-","^"]:
        if l[-1]==")":
            if l[-2]=="(":
                l=l[:-6]+k
            else:
                l+=k
        elif l[-1]in["÷","×","+","-","^","."]:
            l=l[:-1]+k
        else:
            l+=k
    elif k in["sin()","cos()","tan()","cot()","log()","n!()","√"]:
        if l[-2]=="(":
            l=l[:-5]
        if l[-1]in["÷","×","+","-","^"]or len(l)==2:
            l+=k
        else:
            l+="×"+k
    elif k==".":
        if l[-1]in["0","1","2","3","4","5","6","7","8","9"]or l[len(l)-1]==")"and l[len(l)-2]in["0","1","2","3","4","5","6","7","8","9"]:
            l+="."
        elif l[-1]not in[".",")"]or l[-1]==")"and l[-2]!=".":
            l+="0."
    elif l[-1]==")":
        l=l[:-1]+k+")"
    else:
        l+=k
    if len(l)>20:
        t.configure(text=l[-20:])
    else:
        t.configure(text=l)
for i in range(26):
    Button(a,text=b[i],bg=e[i],font=(None,g[i]),command=u[i]).place(x=c[i*2],y=c[i*2+1],width=d[i],height=f[i])
    if i<19:
        a.bind(h[i],j)
def a12(a):
    b3()
def a13(a):
    a9()
def a14(a):
    a6()
a.bind(h[16],a13)
a.bind(h[17],a12)
a.bind(h[18],a14)
del a,b,c,d,e,f,g,h
mainloop()
