def pata(n):
        n=n|1
        for i in range(n):
                for j in range(n):
                        if(i+j==n//2 or i-j==-(n//2) ):
                                print(end='*')
                        else:
                                print(end=' ')
                print()






def patb(n):
        n=n|1
        for i in range(n):
                for j in range(n):
                        if(i==0 or j==0 or (i==n//2 or j==j+1) or j==n-1 or i==n-1):
                                print(end='*')
                        else:
                                print(end=' ')
                print()




def pata(n):
    for i in range(n):
        for j in range(n):
            if i*j==0  or i==n//2 or j==n-1:
                print("*",end="")
            else:
                print("",end=" ")
        print()

def patc(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or i==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def patd(n):
    for i in range(n):
        for j in range(n):
            if i*j==0 or i==n-1 or j==n-1:
                print("*",end="")
            else:
                print("",end=" ")
        print()



def pate(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or i==n-1 or (i==n//2 or j==j+1)):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def patf(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or (i==n//2 or j==j+1)):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def path(n):
    for i in range(n):
        for j in range(n):
            if(j==n-1 or j==0 or (i==n//2 or j==j+1)):
                print("*",end="")
            else:
                print("",end=" ")
        print()



def pati(n):
    for i in range(n):
        for j in range(n):
            if((j==n//2 or i==i+1) or i==0 or i==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def patk(n):
    for i in range(n):
        for j in range(n):
            if(j==0 or i+j==n//2 or i-j==n//2):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def patl(n):
    for i in range(n):
        for j in range(n):
            if(j==0 or i==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def patn(n):
    for i in range(n):
        for j in range(n):
            if(j==0 or j==n-1 or i==j):
                print("*",end="")
            else:
                print("",end=" ")
        print()



def patm(n):
    for i in range(n):
        for j in range(n):
            if i<=n//2 and (j==0 or j==n-1 or i-j==0 or i+j==n-1) :
                print("*",end="")
            else:
                print("",end=" ")
        print()


def pato(n):
    for i in range(n):
        for j in range(n):
            if i*j==0 or i==n-1 or j==n-1:
                print("*",end="")
            else:
                print("",end=" ")
        print()


def patp(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or (i==n//2 or j==j+1) or (i<=2 and j==n-1)):
                print("*",end="")
            else:
                print("",end=" ")
        print()




def patq(n):
    for i in range(n):
        for j in range(n):
            if i*j==0 or i==n-1 or j==n-1 or (i>=n//2 and i==j):
                print("*",end="")
            else:
                print("",end=" ")
        print()




def patr(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or (i==n//2 or j==j+1) or (i<=2 and j==n-1) or (i>=n//2 and i==j)):
                print("*",end="")
            else:
                print("",end=" ")
        print()



def pats(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or (i==n//2 or j==j+1) or (i<=2 and j==0) or (i>=n//2 and j==n-1) or i==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print()



def patt(n):
    for i in range(n):
        for j in range(n):
            if((j==n//2 or i==i+1) or i==0):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def patu(n):
    for i in range(n):
        for j in range(n):
            if j==0 or i==n-1 or j==n-1:
                print("*",end="")
            else:
                print("",end=" ")
        print()




def patv(n):
    for i in range(n):
        for j in range(n):
            if(i-j==n//2 or i+j==3*(n//2) ):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def patw(n):
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1 :
                print("*",end="")
            else:
                print("",end=" ")
        print()


def patw(n):
    for i in range(n):
        for j in range(n):
            if i>=n//2 and (j==0 or j==n-1 or i-j==0 or i+j==n-1) :
                print("*",end="")
            else:
                print("",end=" ")
        print()

def patx(n):
    for i in range(n):
        for j in range(n):
            if(i==j or i+j==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print()



def patz(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or i+j==n-1 or i==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print()

def paty(n):
    for i in range(n):
        for j in range(n):
            if((i<=n//2 and i+j==n-1) or (i<=n//2 and i-j==0) or (i>=n//2 and j==n//2)):
                print("*",end="")
            else:
                print("",end=" ")
        print()

def patj(n):
    for i in range(n):
        for j in range(n):
            if((j==n//2 or i==i+1) or i==0 or (j<=n//2 and i==n-1) or (i>=n//2 and j==0)):
                print("*",end="")
            else:
                print("",end=" ")
        print()

def patg(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if ((i==0 or  j==0 or i==n-1) and j<=n//2) or (j==n//2 and i>=n//2) or (i==n//2 and j>=n//4 and j<n//2) or (j==n//4 and i>n//2 and i<=3*n//4):
                print("*",end="  ")
            else:
                print(end='   ')
        print()



def pat1(n):
        n=n|1
        for i in range(n):
                for j in range(n):
                        if(i==n-1 or (i+j==n//2) or (i==i+1 or j==n//2)):
                                print("*",end="")
                        else:
                                print("",end=" ")
                print()
                        
                        



def pat2(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1 or (i>=n//2 and j==0) or (i==n//2 or j==j+1) or (i<=2 and j==n-1)):
                print("*",end="")
            else:
                print("",end=" ")
        print()



def pat3(n):
    for i in range(n):
        for j in range(n):
            if i==n-1 or i==0 or j==n-1 or (i==n//2 or j==j+1) :
                print("*",end="")
            else:
                print("",end=" ")
        print()


def pat4(n):
    for i in range(n):
        for j in range(n):
            if(j==n-1 or i+j==n//2 or (i==n//2 or j==j+1))  :
                print("*",end="")
            else:
                print("",end=" ")
        print()



def pat4(n):
    for i in range(n):
        for j in range(n):
            if(j==n-1 or i+j==n//2 or (i==n//2 or j==j+1))  :
                print("*",end="")
            else:
                print("",end=" ")
        print()

def pat5(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or (i==n//2 or j==j+1) or (i<=2 and j==0) or (i>=n//2 and j==n-1) or i==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print()




def pat6(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1 or j==0 or (i==n//2 or j==j+1) or (i>=n//2 and j==n-1)):
                print("*",end="")
            else:
                print("",end=" ")
        print()




def pat7(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def pat8(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1 or i+j==n-1 or i==j):
                print("*",end="")
            else:
                print("",end=" ")
        print()



def pat9(n):
    for i in range(n):
        for j in range(n):
            if j==n-1 or i==n-1 or i==0 or i==n//2 or (i<=n//2 and j==0):
                print("*",end="")
            else:
                print("",end=" ")
        print()





def wave(n):
        for i in range(n):
                for j in range(n):
                        for k in range(3):
                            if((j<=n//2 and i==n-1) or (i>=n//2 and j==n//2) or (i==n//2 and j>=n//2) or (i>=n//2) and j==n-1 ):
                                print("*",end="")
                            else:
                                print("",end="")
                        print("",end=" ")
                print()

                


def name(n):
    n=n|1
    for i in range(n):
        for j in range(n):
           for j in range(n):
            if(i==0 or (i==n//2 or j==j+1) or (i<=2 and j==0) or (i>=n//2 and j==n-1) or i==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print(end="  ")

        for j in range(n):
            if(j==0 or i+j==n//2 or i-j==n//2):
                print("*",end="")
            else:
                print("",end=" ")
        print(end="  ")


        for j in range(n):
            if(((j==n//4 or j==3*n//4) and i>n//4 )or (i==n//2) and (j>=n//4 and j<=3*n//4)) or (i+j==n//2 and j>=n//4) or (i-j==-(n//2) and j<=3*n//4):
                print("*",end="")
            else:
                print("",end=" ")
        print(end="  ")


        
        for j in range(n):
            if(i==0 or (i==n//2 or j==j+1) or (i<=2 and j==0) or (i>=n//2 and j==n-1) or i==n-1):
                print("*",end="")
            else:
                print("",end=" ")
        print(end="  ")

        
        for j in range(n):
            if(j==n-1 or j==0 or (i==n//2 or j==j+1)):
                print("*",end="")
            else:
                print("",end=" ")
        print()
        






def wave(n):
        for i in range(n):
                for k in range(3):
                        for j in range(n):
                                
                                    if((j<=n//2 and i==n-1) or (i>=n//2 and j==n//2) or (i==n//2 and j>=n//2) or (i>=n//2) and j==n-1 ):
                                        print("*",end="")
                                    else:
                                        print("",end="")
                        print("",end=" ")



"""
def muti(n):
        
        for i in range(1,n+1):
                m=n%2
                if(m==0):
                        return n
                n=m-1
                
  """      
                        
                       
def multi(n):
    for i in range(1, n + 1):
        if n % 2 == 0:  
            return n  
        n -= 1  
    return n  




        

"""
def smallest_multiple(n):
    num = n  
    while True:
        divisible = True  
        for i in range(1, n + 1):
            if num % i != 0:  
                divisible = False
                break  
        if divisible:
            return num  
        num += 1  
"""
def patoo(n):
    for i in range(n):
        for j in range(n):
            if i*j==0 or i==n-1 or j==n-1:
                print("*",end="")
            else:
                print("#",end="")
        print()


def fun(n):
        n=n|1
        for i in range(n):
                for j in range(n):
                        if((j==n//2 or i==i+1) or (i==n//2 or j==j+1) or  i-j==n//2 or i++j==n//2 or i+j==3*(n//2) or i-j==-(n//2))  :
                                print("*",end="")
                        else:
                                print("",end=" ")
                print()
        


def des(n):
        n=n|1
        for i in range(n):
                for j in range(n):
                        if((i==n//2 or j==j+1) or i-j==-(n//2) or i+j==3*(n//2)):
                                print("*",end="")
                        else:
                                print("",end=" ")
                print()



def tri(n):
        n=n|1
        for i in range(n):
                for j in range(n):
                        if(j==0 or i==n-1 or i==j):
                                print("*",end=" ")
                        else:
                                print("",end="")
                print()




def wave(n):
        for i in range(n):
                for k in range(6):
                        for j in range(n):                                
                                if((j<=n//2 and i==n-1) or (i>=n//2 and j==n//2) or (i==n//2 and j>=n//2) or (i>=n//2) and j==n-1 ):
                                        print("*",end="")
                                else:
                                        print(" ",end="")
                print()









def waves(n):
    for i in range(n):  
        for k in range(6):  
            for j in range(n): 
                if ((j <= n // 2 and i == n - 1) or 
                    (i >= n // 2 and j == n // 2) or 
                    (i == n // 2 and j >= n // 2) or 
                    (i >= n // 2 and j == n - 1)):
                    print("*", end="")
                else:
                    print(" ", end="")
        print()  





def dia(n):
        n=n|1
        for i in range(n):
                for j in range(n):
                        if((i+j==n//2 or i-j==n//2 or i-j==-(n//2) or i+j==3*(n//2)) or (i+j<=n//2) or (i+j>=3*(n//2)) or (i-j>=n//2) or (i-j<=-n//2)) :
                                print("*",end="")
                        else:
                                print("",end=" ")
                print()



def nowave(n):
        for i in range(n):
                for k in range(6):
                        for j in range(n):                                
                                if((j<=n//2 and i==n-1) or (i>=n//2 and j==n//2) or (i==n//2 and j>=n//2) or (i>=n//2) and j==n-1 ):
                                        print(i+1,end="")
                                else:
                                        print(" ",end="")
                print()




def dd(n):
    num=1   
    for i in range(n+1):
        for j in range(n+1):
            if(i-j>=0):
                print(num,end="")
                num+=1
            else:
                print("",end=" ")
        print()



def de(n):
    for i in range(n):
        num=i
        d=n-1
        for j in range(n+1):
            if(i-j>=0):
                print(num,end="")
                num+=d
                d=d-1
            else:
                print(" ",end=" ")
        print()




def nowave(n):
        for i in range(n):
                for k in range(6):
                        for j in range(n):                                
                                if((j<=n//2 and i==n-1) or (i>=n//2 and j==n//2) or (i==n//2 and j>=n//2) or (i>=n//2) and j==n-1 ):
                                        print("*",end="")
                                else:
                                        print(" ",end="")
                print()

 
               


def dg(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if(j==0 or (i-j>=0 and i<=n//2) or (i+j<=n-1 and i>=n//2) ):
                print(chr(65+j),end="")
            else:
                print("",end=" ")
                
        print()


def fc(n):
    for i in range(n):
        for j in range(n):
            if j==0 or (  i-j>=0 and  i<=n//2)or (i+j<=n-1 and i>=n//2) :
                print(chr(65+j),end='')
            else:
                print("",end=' ')
        print()






def fut(n):
    for i in range(n):
        for j in range((2*n)-1):
            if not(i==n-1 or i+j<=n-1 or i-j<=-(n-1) ):
                print("*",end='')
            else:
                print("",end=' ')
        print()










def ef(n):
    num=1   
    for i in range(n+1):
        for j in range(n+1):
            if(i-j>=0):
                if i==0:
                   print(num%9)
                else:
                   print(abs(num%9+1),end=" ")
                   num+=1
            else:
                print("",end=" ")
        print()




def waves(n):
    for i in range(n):  
        for k in range(6):  
            for j in range(n): 
                if ((j <= n // 2 and i == n - 1) or 
                    (i >= n // 2 and j == n // 2) or 
                    (i == n // 2 and j >= n // 2) or 
                    (i >= n // 2 and j == n - 1)):
                    print("*", end="")
                else:
                    print(" ", end="")
        print()  





##  HOMEWORK


def hw1(n):
    n=n|1
    for i in range(n):
        for j in range(n):
            if(j==n//2 or 1-j==-(n//2) or i+j==3*(n//2)):
                print("*",end="")
            else:
                print("",end=" ")
        print()


def rx(n):
     
        for i in range(n):
                for j in range(n):
                        if not(j<=n//2 or i-j<=-(n//2) or i+j>=3*(n//2)):
                                print(n-j-1,end=' ')
                        else:
                                print(" ",end=' ')
                print()




def ry(n):
        n=n|1
        for i in range(n+1):
                for j in range(n+1):
                        if not(j<=n//2 or i-j<=-(n//2) or i+j>=3*(n//2)):
                                print(chr(65+n-1-j),end=' ')
                        else:
                                print(" ",end=' ')
                print()




def ra(n):
        
        for i in range(n):

                        for j in range(n):
                                if not(j>=n//2 or i-j>=n//2 or i+j<=n//2):
                                        print(chr(65+j-1),end="")
                                        j=i+1
                                else:
                                        print("",end=" ")
                        print()


def rb(n):
    num=1   
    for i in range(n+1):
        for j in range(n+1):
            if(i-j>=0):
                print((num-1)%9+1,end="")
                
                
                num=num+1
            else:    
                print("",end=" ")
                
        print()







def rc(n):
        
        for i in range(n):
                        letter=65
                                
                        for j in range((2*n)-1):
                                if not(i==n-1 or i+j<=n-1 or i-j<=-(n-1)):
                                        print(chr(letter),end="")
                                        letter=letter+1
                                else:
                                        print("",end=" ")
                        print()








def rd(n):
        n=n|1
        for i in range(n):
                letter=65
                for j in range(n):
                        if not((i+j==n//2 or i-j==n//2 or i-j==-(n//2) or i+j==3*(n//2)) or (i+j<=n//2) or (i+j>=3*(n//2)) or (i-j>=n//2) or (i-j<=-n//2)) :
                                print(chr(letter),end="")
                                letter+=1
                        
                        else:
                                print("",end=" ")
                print()




def re(n):
   
        for i in range(n):
                for k in range(5):
                        letter=65
                        for j in range(n):
                                if  ((j==0 and i>0) or (i==0 and j>0 and j<n//2) or (j==3*(n//4) and i>0 and i<n-1) or (i==n-1 and j>3*(n//4) and j<n-1)):
                                        print(chr(letter),end='')
                                        letter=letter+1
                                else:
                                        print(" ",end='')
                print( ) 
               


re(9)


