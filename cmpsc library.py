#Ethan Yeung
#Sharon Liu
#Sanchita Bhusari

def in_list(name, arr):
    # quick check to see if element is in list
    for i in range(len(arr)):
        if name in arr[i]:
            return i
    return -1


def update_list(name, arr, update):
    for i in range(len(arr)):
        if name == arr[i][0]:
            arr[i] = update
    return arr


def del_entry(name, arr):
    for i in range(len(arr)):
        if name == arr[i][0]:
            arr[i] = [-1]
    return arr


def parse_booklist():
    with open("booklist.txt", "r") as booklist:
        books = []
        lines = booklist.readlines()
        for i in range(len(lines)):
            # remove tralining newlines
            lines[i] = lines[i].rstrip("/n")
            # parse around '#' and add to list
            lines[i] = lines[i].split("#")
            books += [lines[i]]
    return books

def parse_librarylog():
    with open("librarylog.txt", "r") as librarylog:
        log = []
        lines = librarylog.readlines()
        for i in range(len(lines)):
            # remove trailing newlines
            if i < len(lines)-1:
                lines[i] = lines[i][:-1]
            # parse around '#' and add to list
            log += [lines[i].split("#")]
    return log



# question 1
def can_borrow(user, book, day):
    log = parse_librarylog()
    books = parse_booklist()
    fines = 0
    cur_borrowed = []
    ele = in_list(book, books)
    if ele != -1:
        available_copies = int(books[ele][1])
    else:
        available_copies = 0

    for entry in log:
        # break if reached end of the log
        if len(entry) == 1:
            break
        # if the current day has already passed, we stop looking at the log because those events haven't happened yet
        if day < int(entry[1]):
            break
        
        if entry[2] == user:
            # looking at the user in question
            if entry[0] == 'B':
                # borrow a book, assume if logged then all criteria met
                cur_borrowed += [[entry[3], int(entry[1])+int(entry[4])]] # return date
            elif entry[0] == 'R':
                # return a book
                ele_c = in_list(entry[3], cur_borrowed)
                if cur_borrowed[ele_c][1] < int(entry[1]):
                    # if returned a book past due date
                    days_past = int(entry[1]) - cur_borrowed[ele_c][1]
                    ele_b = in_list(entry[3], books)
                    if books[ele_b][2] == 'TRUE':
                        # if a book is restricted, multiply fine by 5
                        fines += days_past*5
                    else:
                        fines += days_past
                # remove book
                cur_borrowed = del_entry(entry[3], cur_borrowed)
            else:
                # pay a fine
                fines -= int(entry[3])
        
        if book in entry:
            # update book history
            if entry[0] == 'B':
                # if book has been borrowed, remove a copy
                available_copies -= 1
            else:
                # otherwise book is either returned or new copy added, add a copy
                available_copies += 1

                # add book to booklist to prevent possible errors IMPORTANT - check if restricted default to false
                if entry[0] == 'A' and in_list(entry[2], books) == -1:
                    books += [[entry[2], '1', 'FALSE']]

    if len(cur_borrowed) < 3 and fines == 0 and available_copies > 0:
        print('can borrow')
        return True
    else:
        print('cannot borrow')
        return False



# question 2
def days_borrowed(book):
    log = parse_librarylog()
    
    users = [] # keep track of start date of users borrowing the book
    total_time = 0

    for entry in log:
        if len(entry) == 1:
            break
        
        if book in entry:
            if entry[0] == 'B':
                users += [[entry[2], int(entry[1])]]
            elif entry[0] == 'R':
                # if returned, calculate how many days it was out
                ele = in_list(entry[2], users)
                total_time += int(entry[1]) - users[ele][1]
                users = del_entry(entry[2], users)
    
    return total_time



# question 3
def days_available(book):
    books = parse_booklist()
    log = parse_librarylog()
    total_days = int(log[-1][0])-1
    days = 0
    # first find days available with default number of books
    book_element = in_list(book, books)
    if book_element>-1:
        days += int(books[book_element][1])*total_days
    # next check if any books were added in the log
    for entry in log:
        if len(entry) == 1:
            break

        if book in entry:
            # if the book was newly added, increase avalibility accordingly
            if entry[0] == 'A':
                days += total_days - int(entry[1]) + 1 # inclusive to fit example
    return days

# question 4
def book_list():
    log = parse_librarylog()
    books = parse_booklist()
    
    # create simple list of books
    books = [book[0] for book in books]

    for entry in log:
        if len(entry) == -1:
            break

        if entry[0] == 'A':
            # if a new book is added, add to list of books
            if entry[2] not in books:
                books += [entry[2]]
    
    return books


def sorted_usage_ratio():
    books = book_list()
    ratio = []

    for book in books:
        ratio += [(book, days_borrowed(book)/days_available(book))]
    swap = True
    while swap:
        swap = False
        for i in range(len(ratio)):
            for j in range(i+1, len(ratio)):
                if ratio[i][1] > ratio[j][1]:
                    ratio[j], ratio[i] = ratio[i], ratio[j]
                    swap = True
    return ratio


def sorted_most_borrowed():
    books = book_list()
    borrowed = []

    # find how long each unique book was borrowed
    for book in books:
        borrowed += [(book, days_borrowed(book))]
    swap = True
    while swap:
        swap = False
        for i in range(len(borrowed)):
            for j in range(i+1, len(borrowed)):
                if borrowed[i][1] > borrowed[j][1]:
                    borrowed[j], borrowed[i] = borrowed[i], borrowed[j]
                    swap = True
    return borrowed


# question 5
def pending_fines_specific(user, day):
    log = parse_librarylog()
    books = parse_booklist()
    fines = 0
    cur_borrowed = []

    for entry in log:
        if len(entry) == 1:
            break
        if day < int(entry[1]):
            break
        
        if entry[2] == user:
            # looking at the user in question
            if entry[0] == 'B':
                # borrow a book, assume if logged then all criteria met
                cur_borrowed += [[entry[3], int(entry[1])+int(entry[4])]] # return date
            elif entry[0] == 'R':
                # return a book
                ele_c = in_list(entry[3], cur_borrowed)
                if cur_borrowed[ele_c][1] < int(entry[1]):
                    # if returned a book past due date
                    days_past = int(entry[1]) - cur_borrowed[ele_c][1]
                    ele_b = in_list(entry[3], books)
                    if books[ele_b][2] == 'TRUE':
                        # if a book is restricted, multiply fine by 5
                        fines += days_past*5
                    else:
                        fines += days_past
                # remove book
                cur_borrowed = del_entry(entry[3], cur_borrowed)
            else:
                # pay a fine
                fines -= int(entry[3])
        # add book to booklist to prevent possible errors IMPORTANT - check if restricted is false
        if entry[0] == 'A' and in_list(entry[2], books) == -1:
            books += [[entry[2], '1', 'FALSE']]
    
    return fines


def user_list():
    log = parse_librarylog()
    users = []
    for entry in log:
        if len(entry) == 1:
            break

        if entry[0] == 'B':
            # add users who try to borrow but have never borrowed before
            if entry[2] not in users:
                users += [entry[2]]
    
    return users


def pending_fines_day(day):
    print(f'fines at day {day}')
    for user in user_list():
        # find specific fines based on previous function
        print(user, pending_fines_specific(user, day))

def pending_fines_end():
    print('fines at end of log')
    end = int(parse_librarylog()[-1][0])
    for user in user_list():
        # find specific fines but at the end of the log
        print(user, pending_fines_specific(user, end))



# quiz
can_borrow('Egwene', 'Intro to java', 1)
can_borrow('Rand', 'intro to csharp', 1)
can_borrow('Egwene', 'Intro to c', 2)
can_borrow('Rand', 'Cooking 101', 5)
can_borrow('Yonke', 'Dragon reborn', 3)
print(sorted_usage_ratio())
print(sorted_most_borrowed())

pending_fines_end()
can_borrow('Piotr', 'Dragon reborn', 30)

