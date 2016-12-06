def findNums(arg, case):
    telist = arg.split(" ")
    telist = telist[1:]
    smallest = int(telist[0])
    largest = int(telist[0])

    for item in telist:
        if int(item) < smallest:
            smallest = int(item)
        if int(item) > largest:
            largest = int(item)

    print 'Case '+ str(case) + ': ' + str(smallest) + ' ' + str(largest) + ' ' + str(largest - smallest)

i = 0
while True:
    i+=1
    try:
        findNums(raw_input(''), i) # Or whatever prompt you prefer to use.
    except EOFError:
        break
