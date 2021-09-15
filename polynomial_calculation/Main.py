import time, random


# f(x)를 계산하고 그 값을 리턴하는데, O(n^2)시간의 계산이 필요한 함수
def evaluate_n2(A, x):
	# code for O(n^2)-time function
	answer = 0
	for i in range(len(A)):
		k = 1
		for j in range(i):
			k *= x
		answer += A[i]*k
	return answer
	
	
#f(x)를 계산하고 그 값을 리턴하는데, O(n)시간의 계산이 필요한 함수
def evaluate_n(A, x):
	# code for O(n)-time function
	answer = A[0]
	k = 1
	for i in range(1, len(A)):
		k *= x
		answer += A[i] * k
	return answer

random.seed()		# random 함수 초기화
n = int(input())
A = []
for i in range(n):
	A.append(random.randint(-1000, 1000))
	
x = random.randint(-1000,1000)
	
s = time.process_time()
evaluate_n2(A,x)
e = time.process_time()

print("evaluate_n2의 수행시간 = ", e - s)

s2 = time.process_time()
evaluate_n(A,x)
e2 = time.process_time()

print("evaluate_n의 수행시간 = ", e2 - s2)




