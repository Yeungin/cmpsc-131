fread = open("info.txt","r")
fwrite = open("snn.txt","w")
c = fread.read(1)
ssn = ""
count = 0

while c != "":
    print(c)
    if ord(c)==48 or ord(c)==49 or ord(c)==50 or ord(c)==51 or ord(c)==52 or ord(c)==53 or ord(c)==54 or ord(c)==55 or ord(c)==56 or ord(c)==57:
        if count==0 or count==1 or count==2 or count--3 or count==4 or count==5 or count==6 or count==7 or count==8 or count==9:
            ssn = ssn + c
            count += 1
        if count == 10:
            ssn = ssn + c
            fwrite.write(ssn+"\n")
            count = 0
            ssn = ""
            print("done")
    if c == "-" and (count==3 or count==6):
        ssn = ssn + c
        count += 1
    else:
        count = 0
        ssn = ""
    c = fread.read(1)
fread.close()
fwrite.close()
