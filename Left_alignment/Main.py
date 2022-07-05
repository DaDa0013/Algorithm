W = int(input())
words = input().split()
# code below

n = len(words)
P = [0] * n #최소 페널티 담는 DP
P[0] = (W-len(words[0]))**3 

for i in range(1,n):
	space = 0 # 차지하는 공간
	m = W ** 3
	j = i
	while j >= 0:
		space += len(words[j]) + 1 
		if j == 0:
			p = (W - space + 1) ** 3
		else:
			p = P[j - 1] + (W - space + 1) ** 3
		if space - 1 <= W:
			if m > p:
				m = p
		else:
			break
		j -= 1
	P[i] = m
print(P[-1])

# DP 점화식
# P[i] = min(P[i-1] , P[i-2], P[i-3],..,P[k])
# (단, k는 W - space + 1가 0보다 큰 마지막 인덱스)

# 알고리즘 수행시간
# 단어의 갯수를 n이라 했을 떄, for문으로 n만큼 반복하며, while문으로 n번 반복한다.
# 따라서 수행시간은 O(n^2)이다.