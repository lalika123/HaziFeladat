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





def main():
   # feladat_1()
    #feladat_2()
    #feladat_3()
    #feladat_4()
    #feladat_5()
   # feladat_6()
   feladat_7()
if __name__=='__main__':
        main()