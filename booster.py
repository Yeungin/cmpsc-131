def am(x):
    sum = 0
    am_1 = []
    am_f = []

    for k in range(0, len(x)):
        if "am" in x[k]:
            v=x[k].split("am")
            for i in range(0, len(v)):
                if i%2!=0:
                    v.pop(i)
                    am_1.append(v[i-1])

    for k in range(0, len(am_1)):
        am2=am_1[k].split(":")
        for k in range(0, len(am2)):
            am2[k]=int(am2[k])
        sum=(am2[0]*60)+am2[1]
        am_f.append(sum)

    return am_f

def pm(x):
    sum=0
    pm_1=[]
    pm_f=[]
    
    for k in range(0, len(x)):
        if "pm" in x[k]:
            v=x[k].split("pm")
            for i in range (0,len(v)):
                if i%2!=0:
                    v.pop(i)
                    pm_1.append(v[i-1])

    for k in range (0,len(pm_1)):
        pm2=pm_1[k].split(":")
        for k in range(0,len(pm2)):
            pm2[k]=int(pm2[k])
        sum = (pm2[0]+12)*60+pm2[1]
        pm_f.append(sum)

    return pm_f

def check(lst1, lst2, e):
    breaks = []
    eh = True
    
    for k in range (1, len(lst2)):
        t = lst1[k] - lst1[k-1]
        breaks.append(t)
        
    for k in range (0, len(breaks)):
        if breaks[k] <= e:
            eh = False
            
    if eh == True:
        print("Break possible")
        
    else:
        print("Break not possible")
        
def main():
    times = str(input("Please enter the boost times: "))
    times = times.split()
    breaks = int(input("Please enter wanted break time: "))
    blst = []
    tlst = []

    a = am(times)
    p = pm(times)

    for k in range (0, len(a)):
        blst.append(a[k])
        
    for k in range (0, len(p)):
        blst.append(p[k])

    for k in range (0, len(blst)):
        tlst.append(blst[k]+5)

    blst.sort()
    tlst.sort()
    check(blst, tlst, breaks)

main()
    

