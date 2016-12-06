raw = raw_input()
raw = raw.split(" ")
r = map(int, raw)

if r[0] + r[1] == r[2]:
    print str(r[0]) + '+' + str(r[1]) + '=' + str(r[2])
elif r[0] - r[1] == r[2]:
    print str(r[0]) + '-' + str(r[1]) + '=' + str(r[2])
elif r[0] * r[1] == r[2]:
    print str(r[0]) + '*' + str(r[1]) + '=' + str(r[2])
elif r[0] != 0 and r[0] / r[1] == r[2]:
    print str(r[0]) + '/' + str(r[1]) + '=' + str(r[2])

elif r[1] + r[2] == r[0]:
    print str(r[0]) + '=' + str(r[1]) + '+' + str(r[2])
elif r[1] - r[2] == r[0]:
    print str(r[0]) + '=' + str(r[1]) + '-' + str(r[2])
elif r[1] * r[2] == r[0]:
    print str(r[0]) + '=' + str(r[1]) + '*' + str(r[2])
elif r[1] != 0 and r[1] / r[2] == r[0]:
    print str(r[0]) + '=' + str(r[1]) + '/' + str(r[2])
