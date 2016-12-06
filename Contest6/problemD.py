size = raw_input()
sapplings = raw_input()
sapplings = sapplings.split(" ")
sapList = map(int, sapplings)

sapList = sorted(sapList, reverse=True)

longestDay = 0

for i in range(0, int(size)):
    if sapList[i] + i + 1 > longestDay:
        longestDay = sapList[i] + i + 1

print longestDay + 1
