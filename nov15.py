def sales(year):
    fread = open("sales.txt","r")
    temp = 1
    y = 0
    for k in range (6):
        x = fread.readline()
        x = x.rstrip("\n")
        datelst = x.split("/")
        salelst = x.split(",")
        if int(datelst[2]) == year:
            temp = float(salelst[1])
            if temp > y:
                num = salelst[0]
                y = temp
    fread.close()
    return num

def names(num):
    fread = open("info.txt","r")
    for k in range (5):
        x = fread.readline()
        x = x.rstrip("\n")
        lst = x.split(",")
        if lst[1] == num:
            name = lst[0]
            return name

def main():
    year = int(input("Please enter the desired year: "))
    num = sales(year)
    name = names(num)
    print("The highest sales was made by " + name)
    

main()
