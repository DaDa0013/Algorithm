def merge(A, i, j, k, l):
	# i <= j and j < k <= l
	# 정렬된 두 부분 A[i..j]와 A[k..l]을 merge하는 함수
	B = []
	a,c = i,k
	while a<=j and c<=l:
		if A[a] <= A[c]:
			B.append(A[a])
			a += 1
		else:
			B.append(A[c])
			c += 1
			
	for x in range(a, j+1):
		B.append(A[x])
	for x in range(c,l+1):
		B.append(A[x])
		
	for x in range(i, l+1):
		A[x]=B[x-i]

	

def m_sort(A, first, last):
	# 3-way merge sort - merge 함수를 이용해 적절히 합병한다
	if first>=last:
		return 
	m1 = (last-first)//3+first
	m2 = 2*(last-first)//3+first
	m_sort(A, first, m1)
	m_sort(A, m1+1,m2)
	m_sort(A, m2+1,last)
	
	merge(A,first, m1, m1+1,m2)
	merge(A,first, m2, m2+1,last)

def check(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return A[0]+A[(len(A)//2)]+A[-1]

A = [int(x) for x in input().split()]
m_sort(A, 0, len(A)-1)
print(check(A))