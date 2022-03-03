def solve(A):
	DP = [0] * len(A) 
	DP[0] = A[0]
	result = 0
	
	for i in range(1, len(A)):
		if A[i] < A[i-1]: #현재 값이 더 작을떄
			p = i-1 #i보다 하나 전 값부터 시작
			n = 1 # A[i]보다 더 작은 값이 나오기 전까지의 갯수
			while A[p] > A[i]: # A[i]보다 A[j] 클 때 업데이트
				n += 1
				p -= 1
				if p<0:
					break
			DP[i] = DP[i-n] + A[i] * n 
		else: # 현재 값이 더 크거나 같으면
			DP[i] = DP[i-1] + A[i]
	for i in DP:
		result += i
	return result

A = [int(x) for x in input().split()]
print(solve(A))

# <알고리즘 설명>
# 이 문제에서 모든 인덱스 쌍 (i, j)의 m(i, j)을 다 구하려면 무조건 수행시간이 O(n^2)이 되기 때문에 동적계획법으로 각각 구하지 않고도 전의 값을 이용하여 최종 값을 얻기 위해 위와 같이 풀었다.
# 먼저 리스트 DP는  A[0] ~ A[i]까지의 m의 합을 저장하는 용도이다.
# if 문 조건으로 A[i]값이 그 전의 값보다 크거나 같으면 m(i, i)의 값이 m(i-1, i)보다 크다는 것이고, 
# 이떄 m(i, i) = A[i]이므로,  DP[i]에 DP[i-1]+ A[i]한 값을 더한다.

# 만약 A[i]가 전의 값보다 더 작으면 A[i]에서 i를 1씩 줄일 때, 처음으로 A[i]보다 작거나 같은 값이 나왔을 떄의 인덱스를 k라고 하자.
# 이떄 while문으로 m(i,i)~m(k+1, i)까지는 A[i]값이 더 작으므로 A[i]값으로 바꿔준다.
# 이를 for문으로 1부터 len(A)까지 반복 후, DP의 값을 다 더한 값을 구한다.

#<수행시간 분석>
# 먼저 for문으로 1부터 len(A)까지 반복할 떄 만약 while문을 한 번도 안돈다면 O(n)시간으로 되고, 최악의 경우 while문을 매번 다 돌게 된다면 최대 O(n^2)시간까지 된다. 


