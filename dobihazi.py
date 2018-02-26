import math as mt


def feladat_1(a, b):
    a = a + b
    b = a - b
    a = a - b
    print("feladat_1: ", a, b)


def feladat_3(x):
    if x > -2 and x < 0:
        return 2 * x
    elif x >= 0 and x < 0:
        return x * x
    elif x > 2:
        return 10
    else:
        print("A fuggveny nem ertelmezett")
        return


def feladat_17(n):
    masolat = n
    uj_szam = 0
    while n != 0:
        szj = n % 10
        uj_szam = uj_szam * 10 + szj
        n = n // 10
    return uj_szam == masolat


def feladat_16(a, b):
    while True:
        r = a % b
        a = b
        b = r
        if r == 0:
            break
    return a


def feladat_6(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    if a <= 0 or b <= 0 or c <= 0:
        print("Nem megfelelő adatok")

    if a + b > c and b + c > a and a + c > b:
        p = (a + b + c) / 2
        T = mt.sqrt(p * (p - a) * (p - b) * (p - c))
        r = T / p
        R = a * b * c / (4 * T)
        print("feladat6", "R=%.2f es r=%.2f" % (R, r))
    else:
        print("feladat6", "nem kepezhetik!")


def feladat_7(a, b, hossz):
    T = 0
    T = (a + b) * 2
    eredmeny = hossz - T
    if eredmeny > 0:
        print("feladat7:  ""Marad %2.f meter drot" % (eredmeny))
    if eredmeny < 0:
        eredmeny = abs(eredmeny)
        print("feladat7:  ", "szükséges %2.f meter drot" % (eredmeny))


def feladat_12(elertpontszam, maxpontszam):
    if elertpontszam >= maxpontszam * 0.6:
        return "elegseges"
    return "elegtelen"


def feladat_13(erdemjegy):
    if erdemjegy == 1:
        return "elegtelen"
    elif erdemjegy == 2:
        return "elegseges"
    elif erdemjegy == 3:
        return "kozepes"
    elif erdemjegy == 4:
        return "jo"
    elif erdemjegy == 5:
        return "jeles"


def feladat_14(sorszam):
    if sorszam == 1:
        return "januar"
    elif sorszam == 2:
        return "februar"
    elif sorszam == 3:
        return "marcius"
    elif sorszam == 4:
        return "aprilis"
    elif sorszam == 5:
        return "majus"
    elif sorszam == 6:
        return "junius"
    elif sorszam == 7:
        return "julius"
    elif sorszam == 8:
        return "augusztus"
    elif sorszam == 9:
        return "szeptember"
    elif sorszam == 10:
        return "oktober"
    elif sorszam == 11:
        return "november"
    elif sorszam == 12:
        return "december"


def feladat_5(a, b, c, d):
    print("feladat_5:  ")
    print(a, b, c, d)
    if d >= 0:
        print(a, c, b, d)
    else:
        print(a, b, d, c)


def feladat_25(fo, terulet):
    nepsuruseg = fo / terulet
    print("feladat_25:  ", nepsuruseg, "fo/negyzetkilometer")
    if nepsuruseg < 50:
        return "ritkan lakott"
    elif nepsuruseg >= 50 and nepsuruseg <= 300:
        return "atlagosan lakott"
    else:
        return "surun lakott"


def feladat_29(n):
    if n >= 1 and n <= 12:
        if n == 0:
            return 1
        if n == 1:
            return 1
        return n * feladat_29(n - 1)


def feladat_19(n):
    prim = True
    if n == 1:
        prim = False
    for i in range(2, int(mt.sqrt(n) + 1)):
        if n % i == 0:
            prim = False
            break
    return prim


def feladat_20(n):
    print("feladat_20:  ", end=" ")
    a = 1
    b = 1
    if n == 1:
        print(a, end=" ")
    elif n == 2:
        print(a, b, end=" ")
    else:
        c = a + b
        print(a, b, c, end=" ")
        k = 3
        while k < n:
            a = b
            b = c
            c = a + b
            print(c, end=" ")
            k = k + 1
        print()


def feladat_4(a, b, c):
    min = 0
    max = 0
    print("feladat_4:  ", end=" ")
    if a < b and a < c:
        min = a
        print("minimum", min)
    elif b < a and b < c:
        min = b
        print("minimum", min)
    elif c < a and c < b:
        min = c
        print("minumum:", min)

    if abs(a) > abs(b) and abs(a) > abs(c):
        max = abs(a)
        print("maximum:", max)
    elif abs(b) > a and abs(b) > c:
        max = abs(b)
        print("maximum:", max)
    elif abs(c) > a and abs(c) > b:
        max = abs(c)
        print("maximum:", max)


def feladat_8(a, b, c, d, x):
    print("feladat_8:  ", end=" ")
    if x < 5:
        print("x-es kifejezes erteke: ", (3 * x) - 5)
    if x >= 5 and x <= 10:
        print("x-es kifejezes erteke:", 10)
    if x > 10:
        print("x-es kifejezes erteke:", (9 * x) + 1)

    if (a + c) > 2 * d and b > 0:
        print("a 3 parameteru kifejezes erteke", (d - 3 * b))
    elif (a + c) < 2 * d and b < 0:
        print("a 3 parameteru kifejezes erteke", (d + 3 * b))
    else:
        print("a 3 parameteru kifejezes erteke", 4)

def feladat_10(kezdo,veg):
    #■ A szökőév osztható 4-gyel és nem osztható 100-zal, vagy osztható 400-zal.
    szokoev=0
    for i in range(kezdo,veg+1):
        if i%4==0 and i%100!=0 or i%400==0:
            szokoev=szokoev+1
    return szokoev

def feladat_15(a,b):
    hanyados=0
    while a>=b:
        hanyados += 1
        a=a-b
    return hanyados

def feladat_21(n):
    masolat = n
    uj_szam = 0

    while n != 0:
        szj = n % 10
        uj_szam = uj_szam * 10 + szj
        n = n // 10
    return uj_szam

def feladat_24():
    het=0
    tizenharom=0
    k=1
    while k!=0:
        k=int(input("Adj egy szamot: "))
        if k%7==5:
            het+=1
        elif k%13==7:
            tizenharom+=1
    print("hettel: {0}  tizenharommal: {1}".format(het,tizenharom) )


def feladat_26():
    k=1
    pozitiv=0
    negativ=0
    ossz=0
    while k!=0:
        k=int(input("adjon meg egy szamot:"))
        if k<0:
            negativ+=1
        elif k>0:
            pozitiv+=1
        ossz=ossz+k
        print(ossz)
    print("negativ: {0}, pozitiv: {1}. ".format(negativ,pozitiv))

def feladat_32():
    k=7
    a=int(input("adja meg az a szamot:"))
    b=int(input("adja meg a b szamot:"))
    for i in range (a,b):
        if i%k==0:
            print(i,end=" ")




def feladat_31(n):
    k=n//2

    for i in range(1,k+1):
        if n%i==0:
            print(i,end=" ")
    print(n)
    print("\n")

def feladat_9():
    a=float(input("adja meg az a erteket: "))
    b=float(input("adja meg az b erteket: "))
    c=float(input("adja meg az c erteket: "))
    if a ==0:
        print("Ez nem masodfoku egyenlet, a erteke nem lehet 0.")
    else:
        d=b*b-4*a*c
        print("d erteke:",d)
        if d<0:
            print("Nincs valos megoldas.")
        if d==0:
            print("egy megoldas van: {0:8}.2f".format(-b/2/a))
        if d>0:
            gyd=math.sqrt(d)
            print("ket megoldas van: {0:8:2.f} {1:8:2f}".format(((-b+gyd)/2/a)),((-b-gyd)/2/a))

def feladat_23():
    n=int(input("adja meg az n szamot:"))
    if n<=0:
        print("ez nem pozitiv termeszetes szam")
    else:
            sum=0

            for i in range(1,n):
                if n%i==0:
                    sum+=i

            print()
            print("osztok osszege: ",sum)
            print()

            if sum==n:
                print(n,"tokeletes szam")
            else:
                print(n,"nem tokeletes szam")

def feladat_38():
    sum=0
    szam=str(input("adja meg a szamot: "))
    keresettelem=(str(input("adja meg a keresett szamjegyet: ")))
    for i in range(len(szam)):
        if szam[i]==keresettelem:
            sum=sum+1
    print("elofordulas szama:",sum)


def feladat_39():
    for i in range(1000):
        szam=i
        ossz=0
        sz=szam%10
        kob=sz*sz*sz
        ossz+=kob
        szam=szam/10
        if ossz==i:
            print(i,end=" ")

def feladat_37():
    t=70
    n=int(input("adja meg az n szamot"))


    a = 1
    b = 1
    if t == 1:
        print(a, end=" ")
    elif t == 2:
        print(a, b, end=" ")
    else:
        c = a + b
        #print(a, b, c, end=" ")
        k = 3
        while k < t:
            a = b
            b = c
            c = a + b
            #print(c, end=" ")
            if c>n:
                print("\n a legkisebb ilyen fibo szam: ",c)
                break
            k = k + 1
        print()

# 2. pullrequest

def feladat_22(x,n):
    k=0
    k=pow(x,n)
    print("a kifejezes erteke:  ",k)

def feladat_28(n):
    i=1
    while True:
        if i*i>=n:
            print((i-1)*(i-1))
            break
        i+=1

def feladat_33(n):
    #osztokszama=0
    max=0

    for i in range(1,n+1):
        osztokszama=0

        for j in range(1,n+1):

            if i%j==0:
                osztokszama+=1

                if osztokszama>=max:

                    max=osztokszama
                    szam=i




        #print(i,osztokszama)
    print("a legtöbb osztúju szam:{0} illetve osztóinak a száma: {1} ".format(szam,max))





def main():
    feladat_1(51, 33)  # feladat_1
    print("feladat3:  ", feladat_3(3))
    print("feladat17:  ", feladat_17(202))
    print("feladat16:  ", feladat_16(333, 111))
    feladat_6(7, 9, 13)
    feladat_7(10, 20, 20)
    print("feladat_12:  ", feladat_12(60, 100))
    print("feladat_13:  ", feladat_13(5))
    print("feladat_14:  ", feladat_14(4))
    feladat_5(1, 2, 3, 4)
    print(feladat_25(100000, 50))
    print("feladat_29:  ", feladat_29(3))
    print("feladat_19:  ", feladat_19(13))
    feladat_20(9)
    feladat_4(5, 2, -11)
    feladat_8(1, 2, 3, 4, 6)

    print( feladat_10(2000,2004))
    print(feladat_15(20,3))
    print(feladat_21(123456789))
    feladat_24()
    feladat_26()
    feladat_32()
    feladat_31(100)
    feladat_9()
    feladat_23()
    feladat_38()
    feladat_39()
    feladat_37()
 #2. pull reguest: ___
    feladat_22(2, 3)
    feladat_28(100)
    feladat_33(16)

if __name__ == '__main__':
    main()


