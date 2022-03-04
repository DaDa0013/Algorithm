def error(Ds, s, n):
	return round(Ds - (s**2)/n ,3) # 한 그룹의 오차

def Serror(D, group): # 한 묶음의 오차
	if len(group) == 0:
		return D[0][-1][2]
	error = D[0][group[0] - 1][2]
	for i in range(len(group)):
		k = group[i]
		l = len(D) - 1
		if i < len(group) - 1:
			l = group[i+1]-1
		error += D[k][l][2]
	return error

def grouping(B, F):
	D = [[[0 for i in range(3)] for i in range(len(F))] for i in range(len(F))]
	for i in range(0, len(F)):
		for j in range(i, len(F)):
			if i == j:
				D[i][j][0] = F[j]
				D[i][j][1] = F[j] ** 2
			else:
				D[i][j][0] = F[j] + D[i][j-1][0]
				D[i][j][1] = F[j] ** 2 + D[i][j-1][1]
			D[i][j][2] = error(D[i][j][1], D[i][j][0], j-i+1)
	group = []
	for i in range(1, B):
		group.append(i)
	
	m = Serror(D, group)
	
	while len(group) != 0 and group[0] + B < len(F) + 1:
		if group[-1] + 1 < len(F): #끝이 아닐 때
			group[-1] += 1 
		else: # 끝일 때
			a = 0
			for i in range(len(group) - 2, -1, -1):
				if group[i+1] - group[i] == 1:
					continue
				else:
					a= group[i] + 1
					for j in range(i, len(group)):
						group[j] = a
						a += 1
					break
		e = Serror(D, group)
		if m > e:
			m = e
	return m

B, n = input().split()
B = int(B)
n = int(n)
F = [0]* n
for i in range(n):
	F[i] = int(input())

print(grouping(B, F))

# 알고리즘 설명
# 먼저 한 그룹의 오차를 식으로 간단히 표현하면 그룹의 빈도수의 제곱의 합 - (그룹의 빈도수의 합)^2 / 그룹 길이이다.
# 따라서 여기서 사용한 이차원 리스트 D엔 그룹의 빈도수의 합, 그룹의 빈도수의 제곱의 합, 그룹의 오차를 담는다.
# 그 다음 D[i][j][0]에는 F[i]부터 F[j]까지의 합을 넣고, D[i][j][1]에는 i부터 j까지 각각 제곱의 합을 넣고, 마지막으로 D[i][j][2]에는 합과 제곱의 합을 이용하여 오차를 계산하여 넣는다.
# 그리고 while문을 통해 B개인 모든 그룹을 순회하도록 한다.
# 예를 들어 B = 3이면, 앞에 한개인 묶음을 2개로 하고 나머지를 마지막 묶음으로 하여 마지막 묶음을 하나씩 줄여가고, 하나가 될 때까지 줄였을 경우 다시 2번째 묶음의 시작을 뒤로 한칸 이동하여 똑같이 반복하는 것이다.
# 그리고 if문을 통해 최소인 오차묶음을 찾는다.

# 수행시간
# 먼저 grouping 함수에서 그룹 요소들의 합과 제곱의 합, 그리고 오차을 계산하는 것은 2중 for문은 len(F)를 n이라 하였을 때 O(n^2)이다.
# 그리고 while문에서 아까 설명과 같이 모든 그룹을 순회하도록 하기 때문에, B개의 그룹을 찾기 위해선 n-1개 중에 그룹을 나누는 기점으로 B-1개를 뽑아야 한다.
# 따라서 수행시간을 간단히 생각해보면 한번에 n번 도는 for문을 B-1번 하기 때문에 수행시간은 O(n^(B-1))시간이다.
