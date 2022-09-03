def comp(str_1, str_2):
    one = []
    two = []
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []

    for i in range (0,len(str_1)):
        if str_1[i].lower() != str_1[i].upper():
            lst3.append(str_1[i])
    for i in range (0,  len(str_2)):
        if str_2[i].lower() != str_2[i].upper():
            lst4.append(str_2[i])
    if len(lst3) == len(lst4):
        for i in range (len(lst3)):
            one.append(ord(lst3[i]))
            two.append(ord(lst4[i]))
        one.sort()
        two.sort()
        print(one)
        print(two)
        if one == two:
            print("They are anagrams")
        else:
            print("They are not anagrams")
    else:
        print("They are not anagrams")

def main():
    str_1 = input("Enter a string: ")
    str_2 = input("Enter a string: ")
    str_1 = str_1.replace(" ","").lower()
    str_2 = str_2.replace(" ","").lower()
    comp(str_1, str_2)

main()
