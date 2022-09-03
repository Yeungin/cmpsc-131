x = str(input("Please enter the string: "))
count = 1
y = len(x)
temp = 0
char = ""

for i in range(0, y):
    if i != (y-1):
        if x[i] == x[i+1]:
            count += 1
            if count > temp:
                char = x[i]
                temp = count
        else:
            count = 1

print("The longest sequence is " + char + " repeated " + str(temp) + " times")
