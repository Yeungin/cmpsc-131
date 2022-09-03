num = input("Enter the numbers: ")
n = num.split()
b = int(input("Enter b:"))
z = []
des = []
asc = []
x = []
descount = 0
asccount = 0

for i in range (0,len(n)):
    j = int(n[i]) % b
    if j == 0:
        x.append(1)
    else:
        x.append(0)

for k in range (0,len(n)):
    if int(n[k])%b == 0:
        asc.append(n[k])
    else:
        des.append(n[k])

up = asc.sort()
down = des.sort(reverse=True)

for l in range (0,len(n)):
    if x[l] == 1:
        z.append(up[asccount])
        asccount += 1
    if x[l] == 0:
        z.append(int(down[descount]))
        descount += 1



print("The sorted sequesnce is: " + str(z))
        
