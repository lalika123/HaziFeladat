import math as mt
def feladat_1(a,b):
    a= a + b
    b = a - b
    a = a - b
    print("feladat_1: ",a,b)

def feladat_3(x):
    if x>-2 and x<0:
        return 2*x
    elif x>=0 and x<0:
        return x*x
    elif x>2:
        return 10
    else:
        print("A fuggveny nem ertelmezett")
        return

def feladat_17(n):
    masolat=n
    uj_szam=0
    while n!=0:
        szj=n%10
        uj_szam=uj_szam*10+szj
        n=n//10
    return uj_szam==masolat

def feladat_16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return a

def feladat_6(a,b,c):

    a=float(a)
    b=float(b)
    c=float(c)
    if a<=0 or b<=0 or c<=0:
        print("Nem megfelelő adatok")

    if a+b>c and b+c>a and a+c>b:
        p=(a+b+c)/2
        T=mt.sqrt(p*(p-a)*(p-b)*(p-c))
        r=T/p
        R=a*b*c/(4*T)
        print("feladat6","R=%.2f es r=%.2f" % (R,r))
    else:
        print("feladat6","nem kepezhetik!")

def feladat_7(a,b,hossz):
    T=0
    T=(a+b)*2
    eredmeny=hossz-T
    if eredmeny >0 :
        print("feladat7:  ""Marad %2.f meter drot" % (eredmeny))
    if eredmeny<0:
        eredmeny=abs(eredmeny)
        print("feladat7:  ","szükséges %2.f meter drot" % (eredmeny))


def main():
    feladat_1(51,33)#feladat_1
    print("feladat3:  ",feladat_3(3))
    print("feladat17:  ",feladat_17(202))
    print("feladat16:  ",feladat_16(333,111))
    feladat_6(7,9,13)
    feladat_7(10,20,20)
if __name__=='__main__':
    main()


