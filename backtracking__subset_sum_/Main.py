def print_subset(x):
	print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k):
	v_sum = 0
	list = []
	global count
	for i in range(0,k):
		if x[i] == 1:
			v_sum += A[i]
	if k == len(A):
		if v_sum == S:
				print_subset(x)
		if v_sum != S:
				count += 1
		if count == (2**k):
				print(list)
	else:
			# code for x[k] = 1 and x[k] = 0
		if v_sum + A[k] <= S:
			x[k] = 1
			subset_sum(k+1)
		x[k] = 0
		subset_sum(k+1)
count = 0 

# 아래 코드는 수정하지 말고 그대로 사용할 것
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input()) 
x = [0]*len(A)
subset_sum(0)