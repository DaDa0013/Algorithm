import random, timeit

#하나의 값이 남을 때까지 분할하는 quick_sort
def quick_sort(A, first, last):
	global Qc, Qs
	if first >= last:
		return A
	left, right = first+1,last
	pivot = A[first]
	
	while left <= right:
		while left <= last and A[left]<pivot:
			Qc += 1
			left += 1
		while right > first and A[right]>pivot:
			Qc += 1
			right -= 1
		if left <= right:
			Qc += 1
			A[left] , A[right] = A[right] , A[left]
			Qs += 1
			left += 1
			right -= 1
	A[first] , A[right] = A[right] , A[first]
	Qs += 1
	quick_sort(A,first,right - 1)
	quick_sort(A,right+1,last)
	
			
def quick_insertion_sort(A,first, last):
	global Q2c, Q2s
	k = 16
	if last - first +1<=k:
		for i in range(first+1, last + 1):
			j = i-1
			while j >= first: #자리찾기
				Q2c += 1
				if  A[j]>A[j+1]:
					A[j],A[j+1]=A[j+1],A[j]# swap
					j -= 1
					Q2s += 1
				else:
					break
		return A
	
	left, right = first + 1, last
	pivot = A[first]
	while left <= right:
		while left <= last and A[left]<pivot:
			Q2c += 1
			left += 1
		while right > first and A[right]>pivot:
			Q2c += 1
			right -= 1
		if left <= right:
			Q2c += 1
			A[left] , A[right] = A[right] , A[left]
			Q2s += 1
			left += 1
			right -= 1
	A[first] , A[right] = A[right] , A[first]
	Q2s += 1
	quick_insertion_sort(A,first,right - 1)
	quick_insertion_sort(A,right+1,last)
	
def merge_sort(A,first,last):
	global Mc, Ms, Mtc, Mts
	if first >= last:
		return A
	merge_sort(A, first, (first+last)//2)
	merge_sort(A,(first+last)//2+1,last)
	merge_two_sorted_list(A,first,last)
	Mc += Mtc
	Ms += Mts
	

def merge_insertion_sort(A,first,last):
	global M2c, M2s, Mtc, Mts
	k = 16
	if (last-first+1)<=k:
		for i in range(first+1, last+1):
			j = i-1
			while j>=first:
				M2c+=1
				if A[j]>A[j+1]:
					A[j], A[j+1]= A[j+1], A[j]
					M2s+= 1
					j -= 1
				else:
					break
		return A

	merge_insertion_sort(A, first, (first+last)//2)
	merge_insertion_sort(A,(first+last)//2+1,last)
	merge_two_sorted_list(A,first,last)
	M2c += Mtc
	M2s += Mts
	
def merge_two_sorted_list(A,first,last):
	global Mtc, Mts
	Mtc , Mts = 0,0
	m = (first + last)//2
	i, j = first, m+1
	B = []
	while i <= m and j <= last:
		if A[i] <= A[j]: 
			Mtc += 1
			B.append(A[i])
			Mts += 1
			i += 1
		else: 
			Mtc += 1
			B.append(A[j])
			Mts += 1
			j += 1
	for k in range(i, m+1):
		B.append(A[k])
		Mts += 1
	for k in range(j, last+1):
		B.append(A[k])
		Mts += 1
	for i in range(first, last+1):	
		A[i] = B[i - first]
		Mts += 1

	
def heap_sort(A):
	n = len(A)
	make_heap(A)
	
	for k in range(len(A)-1,-1,-1):
		A[0],A[k] = A[k], A[0]
		global Hs
		Hs += 1
		n = n - 1
		heapify_down(A,0,n)
	
def heapify_down(A,k,n):
	global Hc, Hs
	while 2 * k + 1 <= n :
		L, R = 2 * k + 1 , 2 * k + 2
		if L < n and A[L] > A[k]:
			m = L
			Hc += 1
		else:
			m = k
			Hc += 1
		if R < n and A[R] > A[m] :
			m = R
			Hc += 1
		if m != k:
			A[k], A[m] = A[m] , A[k]
			Hs += 1
			k = m
		else:
			break

def make_heap(A):
	n = len(A)
	for k in range(n-1,-1,-1):
		heapify_down(A,k,n)

# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
Q2c, Q2s, M2c, M2s, Mts, Mtc= 0 ,0, 0, 0, 0, 0
n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:]
E = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))
print("Quick and insertion sort:")
print("time =", timeit.timeit("quick_insertion_sort(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Q2c, Q2s))
print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))
print("Merge and insertion sort:")
print("time =", timeit.timeit("merge_insertion_sort(E, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(M2c, M2s))
print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))





# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
assert(check_sorted(E))