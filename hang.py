wdyfread = open("wordlist.txt", "r")
words = []
temp = 0
count = 0
word = ""
k = int(input("Enter the number of guesses: "))
z = "a"


while z != "":
    z = fread.readline()
    z = z.rstrip("\n")
    words.append(z)
    

for j in range (len(words)):
    char = len(words[j])
    if char > temp:
        temp = char
        word = words[j]
            
for i in range (k):
    print("Please guess a letter for the word(" + str(k-i) + " guesses left: ", end='')
    for j in range (temp):
        if j < (temp-1):
            print("_",end='')
        else:
            print("_")
    guess = input("Guess: ")
    if guess in word:
        for i in range (len(words)):
            if len(words[i]) == temp and guess not in words[i]:
                word = words[i]
                

    

    
