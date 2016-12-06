raw = raw_input('')
raw = raw.split(' ')
nums = map(int, raw)

for i in range(1, nums[2]+1):
    says = ''
    if i % nums[0] == 0:
        says += 'Fizz'
    if i % nums[1] == 0:
        says += 'Buzz'
    elif i % nums[0] != 0:
        says += str(i)
    print says
