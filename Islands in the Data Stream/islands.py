class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
		
def subList(A, J, islands):
	#while J != len(A)-2:
#		if A[J] < A[J+1]:
	J+=1
#	if J != len(A):
	anIsland = True
	for i in range(J, len(A)):
		if A[i] != A[len(A)-1]:
			if A[i] < A[i+1] and J != 1:
				anIsland = False
		if A[J] < A[i]:
			islands+=1
			print(A[J:])
			return subList(A[J:], J, islands)
		elif anIsland and i == len(A)-1:
			islands+=1
			print(A[:len(A)-1])
		 	return subList(A[:len(A)-1], J, islands)
#		else
	return islands

# elif A[stack[0]] < A[i]:
# stack.remove(0)
# islands+=1
# return subList(A, J, stack, islands)

def Treestruct(A, J, islands):
	s = []
	while J != len(A)-2:
		if A[J] < A[J+1]:
			return subList(A, J, islands)
		J+=1

runs = raw_input()
for i in range(0, int(runs)):
	sequence_in = raw_input()
	sequence = sequence_in.split(" ")
	seq_num = sequence[0]
	sequence = sequence[1:]
	#print(sequence)
	print(seq_num + ' ' + str(Treestruct(sequence, 0, 0)))
