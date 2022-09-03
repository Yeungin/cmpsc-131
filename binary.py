x = int(input("Enter an upto 5 bit number: "))

bit1 = x//10000
bit2 = (x-(bit1*10000))//1000
bit3 = (x-(bit1*10000)-(bit2*1000))//100
bit4 = (x-(bit1*10000)-(bit2*1000)-(bit3*100))//10
bit5 = x-(bit1*10000)-(bit2*1000)-(bit3*100) - (bit4*10)
num = 0
if (x>99999):
    print("Over 5 digits")


elif (bit1 > 1 or bit2 > 1 or bit3 > 1 or bit4 > 1 or bit5 > 1):
    print("Not a valid binary number")

else:
    
    if (bit1 == 1):
        num = num + 2**4

    if (bit2 == 1):
        num = num + 2**3

    if (bit3 == 1):
        num = num + 2**2

    if (bit4 == 1):
        num = num + 2**1

    if (bit5 -- 1):
        num = num + 2**0

    print("The value in decimal is: " + str(num))






