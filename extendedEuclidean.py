r1 = input("Z : ")
r2 = input("number to find inverse : ")
t1 =0
t2 =1
r  =0
t  =0

stri    =""
z       = r1
inv     = r2

print("q\tr1\tr2\tr\tt1\tt2\tt")
while(r2>0):

    q=r1/r2
    stri=stri + str(q) + "\t" + str(r1) + "\t" + str(r2) + "\t"
    r=r1-(q*r2)
    r1=r2
    r2=r
    
    t=t1-(q*t2)
    stri=stri + str(r) + "\t" + str(t1) + "\t" + str(t2) + "\t" + str(t) 
    t1=t2
    t2=t

    print(stri)
    stri = ""
    
stri="\t"+ str(r1) + "\t" + str(r2) + "\t" + "\t" + str(t1) + "\t" + str(t2) 
print(stri)
stri=str(t1) + " mod " + str(z) + " = " + str(t1%z)
print(stri)
stri="inverse of " + str(inv) + " in Z" + str(z) + " is ---> " + str(t1%z)
print(stri)

