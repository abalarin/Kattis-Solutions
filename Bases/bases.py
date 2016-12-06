#not done :(

# binary conversion
def binary(arg):
    binrep = []
    while int(arg) > 0:
        print(int(arg) % 2)
        binrep.append(int(arg) % 2)
        rep = int(arg) /2
        arg = str(rep)
        print(arg)
    print(binrep)
    pass

base = raw_input()
prehash = hash(base)
print(prehash)
#binary(base)
