raw_in = raw_input()
raw_in = raw_in.split(" ")
start_Num = int(raw_in[0])
end_Num = int(raw_in[1])

def foo(n):
    pass
print(10(foo(n-1)+10*pow(n-2) - n +1))+n-1

print(start_Num, end_Num)
amt0s = 0
for i in range(start_Num, end_Num):
    zeros = str(i)
    for j in zeros:
        if j == '0':
            amt0s+=1

print(amt0s)
