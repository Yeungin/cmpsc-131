n = int(input("please enter n:"))
count = 0
x = []
while count < n:
    num = int(input("please enter a number:"))
    x.append(num)
    count += 1

k = int(input("please enter k: "))

count = 0
while count < n and num != 0:
    num = k
    count2 = count + 1
    num -= x[count]
    while count2 < n:
        num -= x[count2]
        count3 = count2 + 1
        while count3 < 3 or count3 < n:
            num -= x[count3]   
            count3 += 1
        count2 += 1
    count += 1
        
if num == 0:
    print("three numbers add up to k")
else:
    print("no three numbers add up to k")

