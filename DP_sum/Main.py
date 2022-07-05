def solve(L, S):
	D = [[0] * (S + 1) for i in range(L + 1)]
	m = S if S <= 9 else 9
	for i in range(1, L):
		for j in range(0, m + 1): 
			if i == 1:
				D[i][j] = 1
				continue
			if j == 0:
				D[i][j] = 1
				continue
			D[i][j] = D[i][j - 1] + D[i - 1][j]
			
		if S > 9:
			for j in range(m + 1, S + 1):
				if i == 1: break
				D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 10]
				
	for j in range(1, m + 1):
		D[L][j] = D[L][j - 1] + D[L - 1][j - 1]
	if S > 9:
		for j in range(m + 1, S + 1):
			D[L][j] = D[L][j - 1] + D[L - 1][j - 1] - D[L - 1][j - 10]
	return D[L][S]

L,S = input().split()

L = int(L)
S = int(S)
print(solve(L, S) % 2147483647)

# 알고리즘 설명
# 먼저 D는 행이 L+1개, 열이 S+1개인 이차원 리스트이다.
# D[i][j]는 자리 수가 i개일 때 각 자리의 합이 j가 되는 자연수의 개수를 담는다.
# 제일 큰 자리를 제외한 나머지 자리는 0부터 9까지 올 수 있기 때문에 S<=9일 땐 m=S고, S>9일 땐 m = 9로 하여 최대를 9까지로 한다.
# D[i][j]가 의미하는 바가 D[i-1][0 ~ j]인데, D[i-1][0 ~ j-1]은 D[i][j-1]에 저장되어 있기 때문에 D[i][j]는 D[i][j-1]에 D[i-1][j]만 더해주면 된다.
# 따라서 S가 9보다 작을 땐 D[i][j] = D[i][j-1]+ D[i-1][j]를 한다.
# S가 9보다 클 땐 한 자리의 값이 9를 넘으면 안되기 때문에 전체인 D[i][j-1] + D[i-1][j]에서 한 자리가 9를 초과하버리는 경우의 수로 D[i-1][j-10]를 빼준다.
# 그리고 최종적으로 구하려는 L자리일 땐 맨 앞이 0이 안되는 것을 고려하여 D[L][j-1] + D[L-1][j-1]으로 구한다.
# 마찬가지로 S가 9보다 클 때도 한 자리가 9를 초과하는 경우의 수를 빼준다는 의미로 D[L-1][j-10]을 빼준다.


# 수행시간 분석
# 첫 번째 for문에서 전체 L-1번 돌고, 안의 for문에서 S+1번 반복하고,
# 두 번째 for문과 if문 조건에 걸렸을 때 for문을 반복하는 것은 총 S번 반복하는 것이다.
# 따라서 총 수행시간은 O((L-1)*(S+1)) + O(S)이므로 O(L*(S+1))이다.




