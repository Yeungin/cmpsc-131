char = input(str("Enter a character: "))
num = ord(char)

if (num>=65 and num<=90):
    print(chr(num+32))
elif (num>=48 and num<=51 ):
    print("small")
elif (num>=52 and num<=54):
    print("medium")
elif (num>=55 and num<=57):
    print("large")
elif (num>=97 and num<=122):
    x = num-96
    print(chr(num)*x)
else:
    print("Invalid")
