logs = []
logsEmpty = True
iterations = raw_input()
for i in range(0, int(iterations)):
    i = 0
    raw_in = raw_input()
    myList = raw_in.split(" ")
    if logsEmpty:
        if myList[0] == 'entry':
            print(myList[1] + ' entered')
            logs.append(myList)
            logsEmpty = False
        else:
            print(myList[1] + ' exited (ANOMALY)')
    else:
        for employee in logs:
            if employee[1] == myList[1]: #if match
                if employee[0] == myList[0]:
                    if myList[0] == 'entry':
                        print(myList[1] + ' entered (ANOMALY)')
                    else:
                        print(myList[1] + ' exited (ANOMALY)')
                    break
                else:
                    if employee[0] == 'entry':
                        employee[0] = 'exit'
                        print(myList[1] + ' exited')
                    else:
                        employee[0]= 'entry'
                        print(myList[1] + ' entered')
                    break
            elif i == (len(logs)-1):
                if myList[0] == 'exit':
                    print(myList[1] + ' exited ' + '(ANOMALY)')
                    break
                if logsEmpty == False:
                    logs.append(myList)
                    if myList[0] == 'entry':
                        print(myList[1] + ' entered')
                    else:
                        print(myList[1] + ' exited')
                    break
            i = i + 1
