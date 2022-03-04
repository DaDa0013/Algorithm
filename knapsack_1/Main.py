def quickSort(l):
	if len(l) <= 1:
		return l
	
	pivot = l[0][1] / l[0][0]
	L, M, R = [], [], []
	
	for i in range(len(l)):
		if l[i][1] / l[i][0] < pivot:
			L.append(l[i])
		elif l[i][1] / l[i][0] > pivot:
			R.append(l[i])
		else:
			M.append(l[i])
	
	return quickSort(R) + M + quickSort(L)
	
def fractional_knapsack(i, size):
	global c, n
	
	if i >= n or size <= 0:
		return 0
	
	cost = quickSort(c[i:])
	MP = 0
	a = 0
	
	while size > 0 and a < len(cost):
		number = min(size, cost[a][0])
		MP += number * cost[a][1]/ cost[a][0]
		size -= number
		a += 1
		
	return MP

def Knapsack(i,size):
	global MP, x, n, s, p
	
	if i>=n or size<=0:
		return
	
	P = 0
	for j in range(i):
		if x[j] == 1:
			P += p[j]
	
	if s[i] <= size:
		B = fractional_knapsack(i+1, size - s[i])
		if P + p[i] + B >MP:
			MP = max(P + p[i], MP)
			x[i] = 1
			Knapsack(i+1, size - s[i])
	
	x[i] = 0
	B= fractional_knapsack(i+1, size)
	if P + B>MP:
		Knapsack(i+1, size)
	
	return MP

K = int(input())
n = int(input())
s = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]

MP = 0
x = [0] * n

c = [0] * n
for i in range(n):
	c[i] = [s[i],p[i]]
	
print(Knapsack(0,K))





