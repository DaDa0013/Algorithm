def QuickSelect(L, k):
	p = L[0]
	S, B, M = [], [], []
	for x in L:
		if x < p: S.append(x)
		elif x > p: B.append(x)
		else: M.append(x)
	
	if len(S) >= k:
		return QuickSelect(S, k)
	elif len(S)+len(M) < k:
		return QuickSelect(B, k-len(S)-len(M))
	else:
		return p
	
n, k =input().split()
n = int(n)
k = int(k)
	
L = list(map(int,input().split()))
m = QuickSelect(L,k)
print(m)

