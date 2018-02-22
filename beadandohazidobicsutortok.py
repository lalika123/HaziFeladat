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

def feladat_12(elertpontszam,maxpontszam):
    if elertpontszam>= maxpontszam*0.6:
        return "elegseges"
    return "elegtelen"

def feladat_13(erdemjegy):
    if erdemjegy==1:
        return "elegtelen"
    elif erdemjegy==2:
        return "elegseges"
    elif erdemjegy==3:
        return "kozepes"
    elif erdemjegy==4:
        return "jo"
    elif erdemjegy==5:
        return "jeles"

def feladat_14(sorszam):
    if sorszam==1:
        return "januar"
    elif sorszam==2:
        return "februar"
    elif sorszam==3:
        return "marcius"
    elif sorszam==4:
        return "aprilis"
    elif sorszam==5:
        return "majus"
    elif sorszam==6:
        return "junius"
    elif sorszam==7:
        return "julius"
    elif sorszam==8:
        return "augusztus"
    elif sorszam==9:
        return "szeptember"
    elif sorszam==10:
        return "oktober"
    elif sorszam==11:
        return "november"
    elif sorszam==12:
        return "december"

def feladat_5(a,b,c,d):
    print("feladat_5:  ")
    print(a,b,c,d)
    if d>=0:
        print(a, c, b, d)
    else:
        print( a, b, d, c)

def feladat_25(fo,terulet):
    nepsuruseg=fo/terulet
    print("feladat_25:  ",nepsuruseg,"fo/negyzetkilometer")
    if nepsuruseg<50:
        return"ritkan lakott"
    elif nepsuruseg>=50 and nepsuruseg<=300:
        return"atlagosan lakott"
    else:
        return "surun lakott"

def feladat_29(n):
    if n>=1 and n<=12:
        if n == 0:
             return 1
        if n == 1:
             return 1
        return n * feladat_29(n - 1)

def feladat_19(n):
    prim=True
    if n==1:
        prim=False
    for i in range(2,int(mt.sqrt(n)+1)):
        if n % i ==0:
            prim=False
            break
    return prim

def feladat_20(n):
    print("feladat_20:  ",end=" ")
    a=1
    b=1
    if n==1:
        print(a,end=" ")
    elif n==2:
        print(a,b,end=" ")
    else:
        c=a+b
        print(a,b,c,end= " ")
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c,end=" ")
            k=k+1
        print()

def feladat_4(a,b,c):
    min=0
    max=0
    print("feladat_4:  ",end=" ")
    if a <b and a <c:
        min=a
        print("minimum",min)
    elif b <a and b<c:
        min=b
        print( "minimum",min)
    elif c<a and c<b :
        min=c
        print("minumum:",min)

    if abs(a)>abs(b) and abs(a)> abs(c):
        max=abs(a)
        print( "maximum:",max)
    elif abs(b)>a and abs(b)>c:
        max=abs(b)
        print( "maximum:",max)
    elif abs(c)>a and abs(c)>b:
        max=abs(c)
        print("maximum:",max)

def feladat_8(a,b,c,d,x):
    print("feladat_8:  ",end=" ")
    if x<5:
        print("x-es kifejezes erteke: ", (3*x)-5)
    if x>=5 and x<=10:
        print("x-es kifejezes erteke:", 10)
    if x>10:
        print("x-es kifejezes erteke:", (9*x)+1)

    if (a+c)>2*d and b>0:
        print("a 3 parameteru kifejezes erteke",(d-3*b))
    elif (a+c)<2*d and b<0:
        print("a 3 parameteru kifejezes erteke", (d + 3 * b))
    else:
        print("a 3 parameteru kifejezes erteke",4)














def main():
    feladat_1(51,33)#feladat_1
    print("feladat3:  ",feladat_3(3))
    print("feladat17:  ",feladat_17(202))
    print("feladat16:  ",feladat_16(333,111))
    feladat_6(7,9,13)
    feladat_7(10,20,20)
    print("feladat_12:  ",feladat_12(60,100))
    print ("feladat_13:  ",feladat_13(5))
    print ("feladat_14:  ",feladat_14(4))
    feladat_5(1,2,3,4)
    print(feladat_25(100000,50))
    print("feladat_29:  ",feladat_29(3))
    print("feladat_19:  ",feladat_19(13))
    feladat_20(9)
    feladat_4(5,2,-11)
    feladat_8(1,2,3,4,6)




    
if __name__=='__main__':
    main()


