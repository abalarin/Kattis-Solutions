def contains(fname, roster):
    i = 0
    for name in roster:
        if fname == name[0]:
            i+=1

    if i == 2:
        return True
    return False

def sortLast(roster):
    final = sorted(roster, key=lambda x: (x[1], x[0]))
    
    for name in final:
        if contains(name[0], final):
            print name[0] + ' ' +name[1]
        else:
            print name[0]

names = []
while True:
    try:
        tupl = raw_input()
        tupl = tuple(tupl.split(' '))
        names.append(tupl)

    except EOFError:
        sortLast(names)
        break
