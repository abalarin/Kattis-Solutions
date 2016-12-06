def conversion(nums):
    actualN = ''
    powN = 0
    counter = 0
    lis = []
    for i in nums:
        counter +=1
        if counter == len(nums):
            powN = i
        else:
            actualN += str(i)

    lis.append(int(actualN))
    lis.append(int(powN))

    return lis

length = int(raw_input())
totalLi = []
for i in range(0, length):
    nums = raw_input()
    numL = conversion(nums)

    final = pow(numL[0], numL[1])
    totalLi.append(final)

su = sum(totalLi)

if su > 1000000000:
    print(1000000000)
else:
    print sum(totalLi)
