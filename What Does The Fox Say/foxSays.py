num = int(raw_input())

for i in range(0, num):
    raw = raw_input()
    result = raw.split(" ")
    #tset = set(sounds)
    #result = list(tset)

    animalSounds = []
    while True:
        i = 0
        raw = raw_input()
        if raw == "what does the fox say?":
            break
        if 'goes' in raw:
            i = raw.index('goes')
            i+=5
        animalSounds.append(raw[i:])

    finalSet = []
    for i in animalSounds:
        result[:] = [x for x in result if x != i]
        if i not in animalSounds:
            print('!contains' + i)
        else:
            pass #result.remove(i)

    print " ".join([str(x) for x in result] )
