n = int(input("Please enter n: "))
count = 0
k = n
print("Larger primes: ",end=" ")
while(count<5):
    k=k+1
    x=2
    check=1
    while(x<k):
        if k%x==0:
            check=0
        x=x+1
    if (check==1):
        count=count+1
        print(k,end=" ")
print("")
count = 0
k = n
x = 2
print("Smaller primes: ",end=" ")
while(count<5):
    k=k-1
    x=2
    check=1
    while(x<k):
        if (k%x)==0:
            check = 0
        x = x + 1
    if(check==1):
        if(k==2):
            count=5
            print(k,end=" ")
        else:
            count=count+1
            print(k,end=" ")
        

