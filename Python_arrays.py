"""
def abc(arr,elem):
    for i in range(len(arr)):
        if (arr[i]==elem):
            print(i)
    return -1
arr=[1,2,6,5,8]
elem=6
abc(arr,elem)



def maxim(arr):
    maxim=arr[0]
    for i in range(len(arr)):
        if(maxim<arr[i]):
            maxim=arr[i]
    return maxim


arr=[1,2,3,4,5]
print(maxim(arr))


"""


"""
def eveodd(arr):
    evee=0
    eveo=0
    for i in range(len(arr)):
        if(arr[i]%2==0):
            evee+=1
        else:
            eveo+=1
    return evee,eveo

arr=[1,2,3,4,5,6]
print(eveodd(arr))


 """       
"""
def eveodd(arr):
    evee=0
    eveo=0
    for item in arr:
        if(item%2==0):
            evee+=1
        else:
            eveo+=1
    return evee,eveo

arr=[1,2,3,4,5,6]
print(eveodd(arr))
"""

"""
def dectobin(n):
    sum=0
    a=1
    while(n>0):
        sum+=(n%2)*a
        a=a*10
        n=n//2
    return sum

def rep(arr):
    for item in range(len(arr)):
        arr[item]=dectobin(arr[item])
        print(arr[item])

arr=[1,5,6,8]
rep(arr)
"""
"""
def lenn(a):
     count=0
     while(a>0):
        a=a//10
        count+=1
     return count

def nlen(arr):
    for item in range(len(arr)):
        arr[item]=lenn(arr[item])
        print(arr[item])

arr=[123,1,5469.23]
nlen(arr)
"""


"""

def rev(a):
    reverse=0
    while(a>0):
        r=a%10
        reverse=reverse*10+r
        a=a//10
    return reverse

def nrev(arr):
    for item in range(len(arr)):
        arr[item]=rev(arr[item])
        print(arr[item])

arr=[123,1,546]
nrev(arr)


"""
"""
def triangle(n):
    ind=0
    for i in range(5):
        for j in range(5):
            if(i-j>=0):
                print(n[ind],end=" ")
                ind=ind+1
            else:    
                print("",end=" ")
                
        print()

def draw(arr):
    for j in range(len(arr)):
        num=j
        triangle(j)
arr=[1,2,3,4,5,6,7,8,9,10]
    
triangle(arr)
"""

"""

def asc(arr):
    for item in range(len(arr)):
        arr[item]=chr(arr[item])
        print(arr[item])

arr=[65,66,47,32,48]
asc(arr)
"""

"""

def asc(arr):
    for item in range(len(arr)):
        if(arr[item]>47 and arr[item]<56 or arr[i]>64 and arr[i]<97:
            arr[item]=chr(arr[item])
        print(arr[item])

arr=[65,66,47,32,48]
asc(arr)


"""
"""

def lenn(a):
     count=0
     while(a>0):
        a=a//10
        count+=1
     return count

def ans(arr):
    c=[]
    d=[]
    for i in range(len(arr)):
        x=arr[i]//len(arr)
        c.append(x)
        y=arr[i]%len(arr)
        d.append(y)
    return c,d

arr=[10,20,30,40,50,60]
print(ans(arr))
        

"""
"""
def lenn(a):
     count=0
     while(a>0):
        a=a//10
        count+=1
     return count

def ans(arr):
    c=[1]*len(arr)
    d=[1]*len(arr)
    for i in range(len(arr)):
        c[i]=i//len(arr)
        d[i]=i%len(arr)
    return c,d

arr=[10,20,30,40,50,60]
"""
"""

def swap1(arr):
    i=0
    while i<len(arr)-1:
         arr[i],arr[i+1]=arr[i+1],arr[i]
         i+=2
         
    return arr
    
    
arr=[1,5,6,4,2]
print(swap1(arr))
"""
"""
def swap1(arr):
    i=0
    for i in range(0,len(arr)-1,2):
         arr[i],arr[i+1]=arr[i+1],arr[i]

         
    return arr
    
    
arr=[1,5,6,4,2]
print(swap1(arr))


"""
"""
def ind(arr):
    a=[]
    
    for i in range(0,len(arr),2):
            a.append(arr[i])

    for i in range(1,len(arr),2):
            a.append(arr[i])
            


         
    return a
    
    
arr=[1,5,6,4,2]
print(ind(arr))
"""
"""

def indx(arr):
    a=[1]*len(arr)
    ind=0
    for i in range(0,len(arr),2):
            a[ind]=arr[i]
            ind+=1

    for j in range(1,len(arr),2):
            a[ind]=arr[j]
            
            ind+=1

         
    return a
    
    
arr=[1,5,6,4,2]
print(indx(arr))

"""

"""
def ind(arr):
    new=[0]*len(arr)
    ind=0
    for i in range(0,len(arr)):
        print(i)
        if(arr[i]%2==0):
           new[ind]=arr[i]
           ind+=1
    for j in range(len(arr)):
        print(j)
        if(arr[j]%2!=0):
            new[ind]=arr[j]
            ind+=1
    return new
    
    
arr=[1,5,6,4]
print(ind(arr))


"""
"""
def ind(arr):
    new=[]
    for i in range(0,len(arr)):
        if(arr[i]%2==0):
           new.append(arr[i])
    for j in range(len(arr)):
        if(arr[j]%2!=0):
            new.append(arr[j])
    return new
    
    
arr=[1,5,6,4]
print(ind(arr))

"""
"""
def rev(a):
    left=0
    right=len(a)-1
    while left<right:
       a[left],a[right]=a[right],a[left]
       left+=1
       right-=1
    return a

arr=[1,2,3,4,5]
print(rev(arr))
        


"""
"""

def evod(arr):
    left=0
    right=len(arr)-1
    while left<right:
       if(arr[left]%2==0):
           left+=1
       elif(arr[right]%2!=0):          
           right-=1
       else:
           arr[left],arr[right]=arr[right],arr[left]
           left+=1
           right+=1
    return arr


arr=[1,2,3,4,5]
print(evod(arr))

"""
"""
def pair(arr):
    left=0
    right=len(arr)-1
    while left<right:
        
       
    return arr


arr=[3,7,2,4,6,8]
print(evod(arr))


"""



"""
def ind(arr):
    new=[0]*len(arr)
    ind=0
    left=0
    right=len(arr)-1
    while left<=right:

            left+1=right
            left+=1
            right-=1
            new[ind]=arr[ind]
    return new
    
    
arr=[3,7,2,4,6,8]
print(ind(arr))
"""
"""
def first_last(n):
    left=0
    right=len(n)-1
    lis=[0]*len(n)
    i=0
    while(left<=right):
        lis[i]=n[left]
        i=i+1
        if left!=right:
            lis[i]=n[right]
            i=i+1
        left+=1
        right-=1           
    return lis


n=[1,2,3,4,5]

first_last(n)
"""
"""

def shift(arr,k):
    n=len(arr)
    if n<=1:
        return arr

    k=k%n
    if k==0:
        return arr

    result=[0]*n


    for i in range(k,n):
        result[i-k]=arr[i] 

    for i in range(0,k):
        result[n-k+i]=arr[i]
    return result
    


"""
"""
def shift(arr,k):
    n=len(arr)
    if n<=1:
        return arr

    k=k%n
    if k==0:
        return arr

    result=[0]*n


    for i in range(k,n):
        result[k-1-i]=arr[n-1-i] 

    for i in range(0,k):
        result[i+k]=arr[i]

    return result
"""

"""
n=list(map(int,input("Enter n values:").split(",")))
sum(n)


def sum(n):
    sum1=0
    for i in range(len(n)):
        sum1=sum1+i
    return n,sum1
"""
"""

arr=list(map(int,input("enter").split(",")))
print(arr)

def sum(n):
    sum1=0
    for i in range(len(n)):
        sum1=sum1+n[i]
    return n,sum1

sum(arr)
"""
"""
l=list(map(int,input("enter").split(",")))
print(arr)
"""
"""
# 18. 3rd max of a given array
def third_max(arr):
    m1=m2=m3=0
    for i in range(len(arr)):
        if arr[i]>m1:
            m1=m2
            m2=m3
            m3=arr[i]
        elif arr[i]>m2:
            m3=m2
            m2=arr[i]
        elif arr[i]>m3:
            m3=arr[i]
    return m3
arr=[2,10,20,30,45]
print(third_max(arr))


"""
"""
   

arr=list(map(int,input("enter").split(",")))
print(arr)


def spl(arr):
    a=[0]*(len(arr)//2)
    b=[0]*(len(arr)//2)
    mid=len(arr)//2

    for i in range(0,mid):
        a[i]=arr[i]

    for j in range(mid,len(arr)):
        b[j-mid]=arr[j]

    return a,b


print(spl(arr))



"""



"""

def selection(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
        return arr

"""

"""
def seclar(arr):
    if(arr[0]>arr[1]):
        max1=arr[0]
        max2=arr[1]
    else:
        max1=arr[1]
        max2=arr[0]

    for i in range(2,len(arr)):
        if(arr[i]>max1):
           max2=max1
           max1=arr[i]

        elif(arr[i]>max2):
            max2=arr[i]


        

    return max1,max2


arr=[1,3,4,6,8,24,98,5]
print(seclar(arr))
"""

"""
def binsearch(arr,target):
    low=0
    high=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return "not found"

arr=[1,5,6,4,8]
target=5
print(binsearch(arr,target))
"""
"""
def dupli(arr):
    n=len(arr)
    a=[]
    for item in arr:
         if item not in a:
             a.append(item)

    return a
arr=[11,22,33,11,22,33]
print(dupli(arr))
               
    
"""


"""


def freq(arr):
    c=[]
    for i in range(len(arr)-1):
        if i in arr[i+1::]:
            continue
        ct=0
        for j in range(len(arr)):
            if arr[j]==arr[i]:
                ct+=1
        c.append([arr[i],ct])
    print(c)
arr=[1,2,1,3,2,5,5,4,4]
freq(arr)

            
"""
"""

a=(input("enter"))
if(a==a[::-1]):
    print("palindrome")
else:
    print("not palindrome")

"""
"""
def merge(left, right):
    m = len(left)
    n = len(right)
    merge = [0] * (n + m)
    k = 0
    i = 0
    j = 0
    while i < m and j < n:
        if left[i] < right[j]:
            merge[k] = left[i]
            i += 1
        else:
            merge[k] = right[j]
            j += 1
        k += 1
    while i < m:
        merge[k] = left[i]
        i += 1
        k += 1
    while j < n:
        merge[k] = right[j]
        j += 1
        k += 1
    return merge

def merge_sort(arr, st, end):
    if st < end:
        mid = (st + end) // 2
        left = merge_sort(arr, st, mid)
        right = merge_sort(arr, mid + 1, end)
        return merge(left, right)
    return [arr[st]]

arr = [3, 5, 6, 4, 1]
print(merge_sort(arr, 0, len(arr) - 1))


def quick(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    right=[x for x in arr if x>pivot]
    akash=[x for x in arr if x==pivot]
    return quick(left)+akash+quick(right)

arr=[10,8,6,3,9,1,3]
print(quick(arr))


  """  


"""
def abc(arr,elem):
    for i in range(len(arr)):
        if (arr[i]==elem):
            print(i)
    return -1
arr=[1,2,6,5,8]
elem=6
abc(arr,elem)



def maxim(arr):
    maxim=arr[0]
    for i in range(len(arr)):
        if(maxim<arr[i]):
            maxim=arr[i]
    return maxim


arr=[1,2,3,4,5]
print(maxim(arr))


"""


"""
def eveodd(arr):
    evee=0
    eveo=0
    for i in range(len(arr)):
        if(arr[i]%2==0):
            evee+=1
        else:
            eveo+=1
    return evee,eveo

arr=[1,2,3,4,5,6]
print(eveodd(arr))


 """       
"""
def eveodd(arr):
    evee=0
    eveo=0
    for item in arr:
        if(item%2==0):
            evee+=1
        else:
            eveo+=1
    return evee,eveo

arr=[1,2,3,4,5,6]
print(eveodd(arr))
"""

"""
def dectobin(n):
    sum=0
    a=1
    while(n>0):
        sum+=(n%2)*a
        a=a*10
        n=n//2
    return sum

def rep(arr):
    for item in range(len(arr)):
        arr[item]=dectobin(arr[item])
        print(arr[item])

arr=[1,5,6,8]
rep(arr)
"""
"""
def lenn(a):
     count=0
     while(a>0):
        a=a//10
        count+=1
     return count

def nlen(arr):
    for item in range(len(arr)):
        arr[item]=lenn(arr[item])
        print(arr[item])

arr=[123,1,5469.23]
nlen(arr)
"""


"""

def rev(a):
    reverse=0
    while(a>0):
        r=a%10
        reverse=reverse*10+r
        a=a//10
    return reverse

def nrev(arr):
    for item in range(len(arr)):
        arr[item]=rev(arr[item])
        print(arr[item])

arr=[123,1,546]
nrev(arr)


"""
"""
def triangle(n):
    ind=0
    for i in range(5):
        for j in range(5):
            if(i-j>=0):
                print(n[ind],end=" ")
                ind=ind+1
            else:    
                print("",end=" ")
                
        print()

def draw(arr):
    for j in range(len(arr)):
        num=j
        triangle(j)
arr=[1,2,3,4,5,6,7,8,9,10]
    
triangle(arr)
"""

"""

def asc(arr):
    for item in range(len(arr)):
        arr[item]=chr(arr[item])
        print(arr[item])

arr=[65,66,47,32,48]
asc(arr)
"""

"""

def asc(arr):
    for item in range(len(arr)):
        if(arr[item]>47 and arr[item]<56 or arr[i]>64 and arr[i]<97:
            arr[item]=chr(arr[item])
        print(arr[item])

arr=[65,66,47,32,48]
asc(arr)


"""
"""

def lenn(a):
     count=0
     while(a>0):
        a=a//10
        count+=1
     return count

def ans(arr):
    c=[]
    d=[]
    for i in range(len(arr)):
        x=arr[i]//len(arr)
        c.append(x)
        y=arr[i]%len(arr)
        d.append(y)
    return c,d

arr=[10,20,30,40,50,60]
print(ans(arr))
        

"""
"""
def lenn(a):
     count=0
     while(a>0):
        a=a//10
        count+=1
     return count

def ans(arr):
    c=[1]*len(arr)
    d=[1]*len(arr)
    for i in range(len(arr)):
        c[i]=i//len(arr)
        d[i]=i%len(arr)
    return c,d

arr=[10,20,30,40,50,60]
"""
"""

def swap1(arr):
    i=0
    while i<len(arr)-1:
         arr[i],arr[i+1]=arr[i+1],arr[i]
         i+=2
         
    return arr
    
    
arr=[1,5,6,4,2]
print(swap1(arr))
"""
"""
def swap1(arr):
    i=0
    for i in range(0,len(arr)-1,2):
         arr[i],arr[i+1]=arr[i+1],arr[i]

         
    return arr
    
    
arr=[1,5,6,4,2]
print(swap1(arr))


"""
"""
def ind(arr):
    a=[]
    
    for i in range(0,len(arr),2):
            a.append(arr[i])

    for i in range(1,len(arr),2):
            a.append(arr[i])
            


         
    return a
    
    
arr=[1,5,6,4,2]
print(ind(arr))
"""
"""

def indx(arr):
    a=[1]*len(arr)
    ind=0
    for i in range(0,len(arr),2):
            a[ind]=arr[i]
            ind+=1

    for j in range(1,len(arr),2):
            a[ind]=arr[j]
            
            ind+=1

         
    return a
    
    
arr=[1,5,6,4,2]
print(indx(arr))

"""

"""
def ind(arr):
    new=[0]*len(arr)
    ind=0
    for i in range(0,len(arr)):
        print(i)
        if(arr[i]%2==0):
           new[ind]=arr[i]
           ind+=1
    for j in range(len(arr)):
        print(j)
        if(arr[j]%2!=0):
            new[ind]=arr[j]
            ind+=1
    return new
    
    
arr=[1,5,6,4]
print(ind(arr))


"""
"""
def ind(arr):
    new=[]
    for i in range(0,len(arr)):
        if(arr[i]%2==0):
           new.append(arr[i])
    for j in range(len(arr)):
        if(arr[j]%2!=0):
            new.append(arr[j])
    return new
    
    
arr=[1,5,6,4]
print(ind(arr))

"""

def rev(a):
    left=0
    right=len(a)-1
    while left<right:
       a[left],a[right]=a[right],a[left]
       left+=1
       right-=1
    return a

arr=[1,2,3,4,5]
print(rev(arr))
        










































