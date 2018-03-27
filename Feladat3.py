import numpy as np
def feladat_1():
    n=0
    i=1
    n=int(input("adja meg az n erteket! "))
    szam = int(input("egesz szam: "))
    elozo=szam
    while i<=n-1:
        szam=int(input("egesz szam: "))
        if elozo==szam:
            sorszam=i+1
            elozosorszam=i

            print("a {0}. szam egyenlo a {1}. szammal".format(elozosorszam,sorszam))
            i+=1
        elozo=szam

def feladat_2():
    n=5
    i=1
    szam=0
    paros=0
    paratlan=0
    while i<=n:
        szam=int(input("adjon meg egy szamot"))

        if szam%2==0:
            paros+=1
        else:
            paratlan+=1
        i+=1
    print("{0}:{1} a paros es paratlan szamok aranya".format(paros,paratlan))

def feladat_3():
    n=int(input("adja meg az n erteket: "))
    i=1
    sum=0
    li=[]
    while i<=n:
        szam=int(input("adjon meg egy szamot: "))

        li.append(szam)
        i+=1
    print(li)
    for i in li:
        sum += abs(i)
    print( sum/n)

def feladat_4():
    kozeparanyos=0
    sum=  0
    szorzat=1
    i=1
    negativ=0
    n=int(input("adja meg az N erteket! "))
    while i <= n:
        szam=int(input("szam: "))
        if szam>0:
            szorzat*=szam
        else:
            sum+=szam
            negativ+=1
        i+=1
    print(" a pozitiv szamok szorzata: {0}. A negativ szamok szamtani kozeparanyossaga: {1}. ".format(szorzat,sum/negativ))

def feladat_5():
    n=int(input("adja meg az n erteket! "))
    i=1
    li=[]
    sum=0
    while i <=n:
        szam=int(input("szam: "))
        li.append(szam)
        i+=1
    szorzat=1
    for i in li:
        if i<7:
            szorzat*=i
        if szam>10:
            sum+=i
    print(" a 7-nel kisebb szamok szorzata {0}. a 10-nel nagyobb szamok osszege: {1}".format(szorzat,sum))

def feladat_6():
    a=int(input("adjon meg egy szamot: "))
    b=int(input("adjon meg egy szamot: "))


    while True:
        sum=a+b
        szam=int(input("adjon meg egy szamot: "))
        if szam==0:
            break

        if szam==sum:
            print("a szam megegyezik az elozo ketto osszegevel: " ,szam)
        c=b
        a=b
        b=szam
        #print(a,b,a+b)

def feladat_7():
    li=[]
    while True:
        szam=int(input("szam: "))
        if szam==0:
            break
        li.append(szam)
    #print(li)
    max1=max(li)
   # print(max1)
    ujli=[]
    harmadik=[]
    szamlalo=0
    szamlalo2=0
    for i in li:
        if i <max1:
            ujli.append(i)
        if i ==max1:
            szamlalo+=1
            if szamlalo>1:
                ujli.append(i)

    #print("ujlista: " ,ujli)
    max2=max(ujli)
    for i in ujli:
        if i < max2:
            harmadik.append(i)
        if i == max2:
            szamlalo2 += 1
            if szamlalo2 > 1 and szamlalo2<3:
                harmadik.append(i)
    #print(li)
   # print("ujlista: " ,ujli)

    #print("harmadik", harmadik)
    max3=max(harmadik)

    print("a 3 szam aminek legnagyobb az atlaga ",max1,max2,max3)
    atlag=(max1+max2+max3)/3
   # print("a 3 legnagyobb szam atlaga: ",atlag)


def feladat8_(t,n):
    for i in range(0,n-1):

        if t[i]>t[i+1]:
            return False
    return True

def lnko(m,n):
    mar=m%n
    if mar==0:
        return n
    else:
        return lnko(n,mar)

def fel9_rel_prim(t,n):
    for i in range(0,n-1):
        for j in range (i+1,n):
            if lnko(t[i],t[j])!=1:
                return 0 #False
    return 1  #True


def osztok(x):
    osztok = 1
    for i in range(1, x):
        if x % i == 0:
            osztok += 1
    return osztok


def feladat_10(t, k):
    for i in range(len(t) - 1):
        for j in range(i + 1, len(t)):
            if osztok(t[i]) > osztok(t[j]):
                temp = t[i]
                t[i] = t[j]
                t[j] = temp
    # print(t)
    e = 0
    v = len(t) - 1
    while e <= v:
        x = (e + v) // 2
        if osztok(t[x]) > k:
            return x
        else:
            e = x + 1
    return -1

def hatos(n,m):
    hatos=np.zeros((n,m))
    for i in range (0,n):
        for j in range(0,m):
            if i==0 or i==n//2 or i==n-1:
                hatos[i][j]=42
            else:
                hatos[i][j]=32
        hatos[i][0]=42
        if i>n//2:
            hatos[i][m-1]=42
    for i in range(0,n):
        for j in range(0,m):
            print(chr(int(hatos[i][j])),end='')
        print('\n')

def feladat_11(mat,n):
    for i in range(3):
        negativ=0
        nullertek=0
        for j in range(3):
            if mat[j][i]==0:
                nullertek+=1

            elif mat[j][i]<0:
                negativ+=1
       # print(negativ,nullertek)
        if negativ>=nullertek*2 and nullertek!=0:
            return j,".oszlop"

def feladat_12(tizenkettes,n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if tizenkettes[i][j]%(i+j)==0:
                return tizenkettes[i][j]


def feladat_15(tizenot,n):
    for i in range(n):
        for j in range(n):
            if tizenot[i][i]==0:
                return True
    return False

def feladat_14(tizennegy,n):
    max=tizennegy[n-1][n-1]
    print(max)
    for i in range(1,n):
        for j in range(n,1):
            if tizennegy[i][j]>max:
                max=tizennegy[i][j]
    return max

def feladat_13(tizenharom,n,m):

    for j in range(m):
        min=tizenharom[j][0]
        for j in range(n):
            if tizenharom[j][0]<=min:
                min=tizenharom[j][0]
                #print(min)
        for j in range(n):
            i=0
            #tizenharom[j][i]-=min

            print(tizenharom[j][i]-min)



def feladat_16(alap16,transzponalt,n,m):
    for i in range(n):
        for j in range(m):
            transzponalt[j][i]=alap16[i][j]
    return transzponalt



def main():
    feladat_1()
    feladat_2()
    feladat_3()
    feladat_4()
    feladat_5()
    feladat_6()
    feladat_7()

   # pull


    t = np.array([2, 3, 5, 7, 11, 13])
    print(feladat8_(t,6))
    print(fel9_rel_prim(t,6))
    feladat_10(t,2)
    print(hatos(5,4))


    mat = np.array([[1, 2, 0], [-1, -2, -3], [1, 2, -3]])
    print(feladat_11(mat, 3))


    tizenkettes = np.array([[2, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(feladat_12(tizenkettes, 3, 3))


    tizenot = np.array([[0, 1, 2], [1, 0, 2], [1, 2, 0]])
    print(feladat_15(tizenot, 3))

    tizennegy=np.array([[1,2,3],[4,5,6],[33,45,211]])
    feladat_14(tizennegy,3)

    tizenharom = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]])
    feladat_13(tizenharom, 5, 3)

    alap16 = np.array([[1, 2, 3, 4], [3, 2, 1, 5], [4, 5, 6, 9]])
    transzponalt = np.array([[1, 2, 3], [5, 4, 3], [23, 43, 11], [55, 43, 53]])
    print(feladat_16(alap16, transzponalt, 3, 4))

if __name__=='__main__':
        main()