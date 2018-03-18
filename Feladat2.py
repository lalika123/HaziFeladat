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
    try:
        fajl=open(fajlnev,mode="r")
        max=0
        for sor in fajl:
            if (sor[0].isupper() and len(sor)>max):
                sor=sor.strip()
                max=len(sor)
        print(max)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()



#pull reguest

def feladat_11():
    try:
        fajl=open("be.txt",mode="r")
        min=5000
        for sor in fajl:
            sor=sor.strip()
            eredeti=sor
            sor=sor.split()

            if(sor[-1][-1])=="." or sor[-1] [-1]=="?" or sor[-1] [-1]=="!" and len(eredeti)<min:

                    min=len(eredeti)
        print (min)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_12():
    try:
        fajl=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        cv=1
        li=[]
        for sor in fajl:
            szam=0
            sor=sor.strip()
            szam=sor
            if cv<16:
                li.append(szam)
                cv+=1
        #print(li)
        ertek=li[-1]
        #print(ertek)
        ertek=int(ertek)
        k=1
        z=1
        for i in range(len(li)-1):
            if li[i]==li[i+1] :
                k+=1
        #print( "k erteke: ",k)
        if k >= ertek:
            fajl2.write(" %s az utolso ertek \n" % ertek)
            fajl2.write("%d  egymast koveto egyforma szam van benne " % k)
        else:
            fajl2.write(" %s az utolso ertek \n" % ertek)
            fajl2.write("nem volt benne annyi egymast koveto egyforma szam")
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()
        fajl2.close()

def feladat_13():
    try:
        fajl=open("be.txt",mode="r")
       # fajl2=open("ki.txt",mode="w")
        li=[]
        for sor in fajl:
            sor=sor.strip()
            szam=sor
            cv=2
            if cv < 16:
                li.append(szam)
                cv += 1


        ertek=int(li[-1])
        print("az utolse szam",ertek)
        bigyo=0
        raktar=0
        for i in range(len(li)-1):
                li[i]=int(li[i])
                li[i+1]=int(li[i+1])
                raktar=li[i]-li[i+1]
                raktar=abs(raktar)
                if raktar <=ertek:
                    bigyo+=1
        print("osszesen %d ilyen szampar van" % bigyo)
    except OSError as e :
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_15():
     try:
         fajl=open("be.txt",mode="r")
         fajl2=open("ki.txt",mode="w")
         for sor in fajl:
             sor=sor.strip()
             if sor=="":
                 break
             else:
                 fajl2.write("%s \n" % sor )
     except OSError as e:
         print(e)
     except Exception as e:
         print(e)
     finally:
         fajl.close()
         fajl2.close()

def feladat_16():
      try:
        fajl=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        for sor in fajl:
            sor=sor.strip()
            if sor.isupper():
                fajl2.write("%s " % sor)
                break
      except OSError as e:
          print(e)
      except Exception as e:
          print(e)
      finally:
          fajl2.close()
          fajl.close()

def feladat_17():
    try:
        li=[]
        fajl=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        cv=0
        for sor in fajl:
            sor=sor.strip()
            mentes=sor.split(" ")

            for i in mentes:

                i=str(i)
                if i.islower() and cv<1 :
                     #sor=str(sor)
                     fajl2.write(" %s " % sor)
                     cv+=1
                     break




    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl2.close()
        fajl.close()

def feladat_19():
    try:
        max=0
        mentes=""
        fajl=open("be.txt", mode="r")
        for sor in fajl:
            if sor=="":
                break
            sor=sor.split(" ")
            sor[1]=int(sor[1])
            if sor[1]>max:
                max=sor[1]
                mentes=sor[0]
        print("a nap leglatogatottabb weboldala a {0} {1}db megtekintessel".format(mentes,max))
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_20():
    try:
        fajl=open("be.txt",mode="r")
        max=0
        for sor in fajl:
            if sor =="":
                break
            sor=sor.split(";")
            sor[2]=int(sor[2])
            if sor[2]>max:
                max=sor[2]
                mentes=sor[0]
        print("a legtobb lakossal rendelkezo varos: {0} {1} db lakossal ".format(mentes,max))
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_21():
    try:
        fajl=open("be.txt",mode="r")

        for sor in fajl:
            sor=sor.strip()
            sor=sor.split(";")
            #print(sor)
            nev=sor[0]
           # print(nev)
            sum=0
            for i in range(1,len(sor)):

                sor[i]=int(sor[i])
                sum+=sor[i]


            print(nev,sum)













    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_22():
    try:
        fajl=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        min=10212
        for sor in fajl:
            if sor=="":
                break
            sor=sor.strip()
            sor=sor.split(";")

            sor[2]=int(sor[2])

            if sor[2]<min:
                min=sor[2]
                nev=sor[0]
        fajl2.write("a gyerek neve: {0} es a futamideje: {1}".format(nev,min))
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()
        fajl2.close()

# 3. pullrequest
def feladat_18():
    try:
        egyik=""
        masik=""
        elsopont=0
        masikpont=0
        k=0
        gyoztes=""

        fajl=open("be.txt",mode="r")
        for sor in fajl:
            sor=sor.split(" ")
            if k==1:
                break
            egyik=sor[0]
            masik=sor[2]
        #print("egyik es a masik_______",egyik,masik)
        fajl.close()
        fajl=open("be.txt",mode="r")
        for sor in fajl:
            if sor =="":
                break
            sor=sor.strip()
            sor=sor.split(" ")
            sor[3]=sor[3].split(":")
            #print(sor[3])
            sor[3][0]=int(sor[3][0])
            sor[3][1]=int(sor[3][1])

            if egyik==sor[0] and masik==sor[2]:

                elsopont+=sor[3][0]
                masikpont+=sor[3][1]
               # print(elsopont,masikpont,"philadelphia   toronto")
            elif masik==sor[0] and egyik==sor[2]:

                elsopont += sor[3][1]
                masikpont += sor[3][0]
                #print(elsopont,masikpont)

            if elsopont>masikpont:
                gyoztes=sor[0]
            elif elsopont<masikpont:
                gyoztes=sor[2]
        print("a donto gyoztese a :",gyoztes)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

#4.pull
def feladat_5_osztokszama(szam):
    db=2
    for i in range(2, szam//2+1):
        if szam%i==0:
            db+=1
    return db
def feladat_5(n):
    max=1
    for i in range(2,n+1):
        if max <feladat_5_osztokszama(i):
            max=feladat_5_osztokszama(i)
            print(i)

def feladat_23():
    try:
        allapot="Yes"
        elozo=0
        fajl=open("be.txt",mode="r")
        for sor in fajl:
            if sor == "":
                break
            sor=sor.strip()
            sor=sor.split(" ")
            ertek=int(sor[1])
            #print(ertek)
            if ertek<elozo:
                allapot="No"
                break
            elozo=ertek


        print(allapot)





    except OSError as e:
        print(e)
    #except Exception as e:
       # print(e)
    finally:
        fajl.close()

#5. pull
def feladat_24():
    try:
        fajl=open("be.txt",mode="r")
        li=[]
        for sor in fajl:
            if sor =="":
                break
            sor=sor.strip()
            sor=sor.split()
            li.append(sor)

        #print(li)
        teki=0
        for i in li[1]:
            i=int(i)
            teki+=i
        #print(teki)
        csiga=0
        for i in li[2]:
            i=int(i)
            csiga+=i
        #print(csiga)

        hossz=max(csiga,teki)*2
        #print("hossz: ",hossz)
        if teki>csiga:
            print(hossz)
            print("TURTLE")
        elif teki<csiga:
            print(hossz)
            print("SNAIL")
        elif teki==csiga:
            print(hossz)
            print("DRAW")

    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_25():
    try:
        fajl=open("be.txt",mode="r")
        li=[]
        angol=[]
        magyar=[]
        for sor in fajl:
            if sor=="":
                break
            sor=sor.strip()
            sor=sor.split(":")
            li.append(sor)
        ertek=li[0]
        nincsbenne=0
        for i in range(1,len(li)):
            angol.append(li[i][0])
        #print(angol)

        for i in range(1,len(li)):
            magyar.append(li[i][1])
        #print(magyar)


        angoltmp=[]
        magyartmp=[]
        for i in angol:
            if i not in angoltmp:
                angoltmp.append(i)
        #print(angoltmp)

        for i in magyar:
            if i not in magyartmp:
                magyartmp.append(i)
        #print(magyartmp)
        sum_m=len(magyartmp)
        print(sum_m)
        sum_a=len(angoltmp)
        print(sum_a)









    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_26(fajl1,fajl2):
    try:
        fajl1=open(fajl1,mode="r")
        fajl2=open(fajl2,mode="r")
        fajl3=open("ki.txt",mode="w")
        li=[]
        li2=[]
        for sor in fajl1:
            if sor=="":
                break
            sor=sor.strip()
            li.append(sor)

        print(li)
        for sor in fajl2:
            if sor=="":
                break
            sor=sor.strip()
            li2.append(sor)
        print(li2)
        elso=len(li)
        masodik=len(li2)
        print(elso,masodik)

        fajl3.write("%d %d \n" %(elso, masodik))
        for i in li:
            if i not in li2:
                fajl3.write("%s \n" %i)


    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl1.close()
        fajl2.close()
        fajl3.close()


def main():
    print(feladat_1(8))
    print(feladat_3(513))
    feladat_4()
    feladat_9()
    print(feladat_8(6))
    feladat_7(441,3135)
    feladat_6(1234567,122452)
    feladat_10("be.txt")

 # pull reguest

    feladat_11()
    feladat_12()
    feladat_13()
    feladat_15()
    feladat_16()
    feladat_17()
    feladat_19()
    feladat_20()
    feladat_21()
    feladat_22()

#3. pullrequest
    feladat_18()

#4. pull

    feladat_5(101)
    feladat_23()
# 5. pull
    feladat_24()
    feladat_25()
    feladat_26("be.txt", "be2.txt")
if __name__ == '__main__':
    main()


