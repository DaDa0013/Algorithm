def find_median_five(A):
	if len(A) == 5:
		for i in range(1):
			A.remove(min(A))
		return min(A)
	elif len(A) == 4 or len(A) == 3:
		A.remove(min(A))
		return min(A)
	elif len(A)==2 or len(A) == 1:
		return min(A)
	else:
		return

	
def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴
	if len(L) == 1: # no more recursion
		return L[0]
	i = 0
	A, M, B, medians = [], [], [], []
	while i+4 < len(L):
		medians.append(find_median_five(L[i: i+5]))
		i += 5
		
	if i < len(L) and i+4 >= len(L): # 마지막 그룹으로 5개 미만의 값으로 구성
		medians.append(find_median_five(L[i:]))
	
		
	mom = MoM(medians, len(medians)/2)
	for v in L:
		if v < mom:
			A.append(v)
		elif v > mom:
			B.append(v)
		else:
			M.append(mom)
			

	if len(A) >= k: 
		return MoM(A,k)
	elif len(A)+len(M) < k: 
		return MoM(B,k-len(A)-len(M))
	else: 
		return mom

# n과 k를 입력의 첫 줄에서 읽어들인다
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
n,k = map(int,input().split())
L = list(map(int,input().split()))
print(MoM(L, k))