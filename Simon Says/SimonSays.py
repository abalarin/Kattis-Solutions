iterations = raw_input()
statements = []
for i in range(0, int(iterations)):
    raw_in = raw_input()
    if(raw_in[:10] == 'simon says'):
        statements.append(raw_in[11:])
        #print(raw_in[11:])
    else:
        statements.append('')

for i in statements:
    print i
