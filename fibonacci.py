import codecs as cod
def mehecske(n):
    a=1
    b=1
    if n==1:
        print(a,end=" ")
    elif n==2:
        print(a,b,end=" ")
    else:
        c=a+b
        print(a,b,c,end=" ")
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c,end=" ")
            k+=1
def fibo2(n):
    a=1
    b=1
    k=1
    fajl=open("ki1.txt",mode="w")
    fajl.write("%.4f " % (a/b))
    while k<n:
      #  print("%.4f" % (a/b),end=" ")
        a=a+b
        b=a-b
        k+=1
    fajl.close()

def feladat1(fajl_nev):
    fajl=cod.open(fajl_nev,encoding='utf-8',mode="r")
    max=0
    for sor in fajl:
        sor=sor.strip()
        if(sor[0].isupper() and len(sor)>max):
            max=len(sor)
            max_sor=sor
    print(max,max_sor)
    fajl.close()


def feladat2():
    fajl=open("be1.txt".mode="r")
    for sor in fajl:
        if("   " in sor):
            fajl=open("ki1.txt",mode="w")
            fajl.write(sor)
            fajl.close()
            break

def fel7(lista,betu):
    li=[]
    fajl=open("ki2.txt",mode="w")
    for i in lista:
        if i[0]==betu:
            li.append(i)




def main():
    mehecske(10)
    fibo2(20)
    feladat1("be1.txt")
    #feladat2()

if __name__== '__main()__':
    main()

