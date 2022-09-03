def check(start.list, end.list, start, end):
    for i in range (len(start.list)):
        if start.list[i] == start
            p1 = i
            end2 = end.list[i]
            if end.list[i] == end:
                print("Yes it is possible to go from the starting city to the destination city using 3 or fewer roads")
                break
            else:
                for i in range(len(start.list[i])):
                    if start.list[i] == end.list[p]:   
                        p2 = i
                        if end.list[p2] == end:
                            print("Yes it is possible to go from the starting city to the destination city using 3 or fewer roads")
                            break
                        else:
                            for i in range(len(start.list[i])):
                                if start.list[i] == end.list[p]:   
                                p3 = i
                                if end.list[p3] == end:
                                    print("Yes it is possible to go from the starting city to the destination city using 3 or fewer roads")
                                    break
                                else:
                                    print("No it is not possible to go from the starting city to the destination city using 3 or fewer roads")
        

def main():
    num.roads = int(input("How many roads are there"))
    start.list = []
    end.list = []
    for i in range(num.roads):
        road = input("Enter the roads ")
        roads.list = road.split("-")
        start.list = []
    start = input("Enter starting position")
    end = input("Enter ending position")
    check(start.list, end.list, start, end)
