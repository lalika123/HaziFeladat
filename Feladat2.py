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



if __name__ == '__main__':
    main()

