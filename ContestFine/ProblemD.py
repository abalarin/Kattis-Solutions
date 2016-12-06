raw = raw_input('')
raw = raw.split(' ')
nums = map(int, raw)

if nums[0] > 1:
    nums[0] = '-' + str(nums[0]-1)
elif nums[0] == 0:
    nums[0]+=1
else:
    nums[0] = 0

if nums[1] > 1:
    nums[1] = '-' + str(nums[1]-1)
elif nums[1] == 0:
    nums[1]+=1
else:
    nums[1] = 0

if nums[2] > 2:
    nums[2] = '-' + str(nums[2]-2)
elif nums[2] == 0:
    nums[2]+=2
elif nums[2] == 2:
    nums[2] = 0

if nums[3] > 2:
    nums[3] = '-' + str(nums[3]-2)
elif nums[3] == 0:
    nums[3]+=2
elif nums[3] == 2:
    nums[3] = 0

if nums[4] > 2:
    nums[4] = '-' + str(nums[4]-2)
elif nums[4] == 0:
    nums[4]+=2
elif nums[4] == 2:
    nums[4] = 0

if nums[5] > 8:
    nums[5] = '-' + str(nums[5]-8)
elif nums[5] == 0:
    nums[5]+=8
elif nums[5] < 8:
    nums[5] = 8 - nums[5]
else:
    nums[5] = 0
#
# if nums[1] > 1:
#     nums[1] = int('-' + str(nums[0]-1))
# elif nums[1] == 0:
#     nums[1]+=1
#
#
# if nums[2] > 2:
#     nums[2] = int('-' + str(nums[0]-2))
# elif nums[2] == 0:
#     nums[2]+=2
final = map(int, nums)
for i in final:
    print i,
