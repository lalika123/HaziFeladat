import math as mt
def feladat_1(n):
    oszto=0
    for i in range (1,n+1):
       if  n%i==0:
           oszto+=1
    #return oszto
    if oszto ==4:
        return True
    else:
        return False

def feladat_3(n):

    szam=0
    k=1
    while n!=True:
        szam=pow(2,k)
        if szam>=n:
            break
        k+=1

    return szam

def feladat_4():
    for i in range(100,1000):
        i=str(i)
        if i[0]!=i[1] and i[0]!=i[2] and i[1]!=i[2]:
            print(i,end=" ")


def feladat_9():
    magassag=1
    cel=300
    perc=1
    k=2
    while magassag!=cel:
        magassag=magassag+magassag*(1/k)
        k+=1
        perc+=1
    print(perc)

def feladat_8(n):
    sum=0
    i=1
    while sum<=n:
        sum=sum+i
        i+=1
    return i-1

def feladat_7(a,b):
    a=str(a)
    b=str(b)

    k="nem baratok"
    for i in range(len(a)):
        if a[i] in b:
            k="baratok"
    print(k)

def feladat_6(a,b):
    sum=0
    a=str(a)
    b=str(b)
    tmp="123456789"
    li=[]
    for i in tmp:
        if i in a:
            li.append(i)

    for i in li:
        if i in b:
            sum+=1
    #print (sum)
    if sum>=2:
        print("rokonok")
    else:
        print("nem rokonok")

def feladat_10(fajlnev):
    fajl=open(fajlnev,mode="r")
    max=0
    for sor in fajl:
        if (sor[0].isupper() and len(sor)>max):
            sor=sor.strip()
            max=len(sor)
    print(max)
    fajl.close()









def main():
    print(feladat_1(8))
    print(feladat_3(513))
    feladat_4()
    feladat_9()
    print(feladat_8(6))
    feladat_7(441,3135)
    feladat_6(1234567,122452)
    feladat_10("be.txt")


if __name__ == '__main__':
    main()

