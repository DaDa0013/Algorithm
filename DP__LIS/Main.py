def print_IS(seq, x):
	for i in range(len(seq)):
		if x[i]: 
			print(seq[i], end="")
		else:
			print("_", end="")
	print()

def LIS_DP(seq):
	x = [""] * len(seq)
	DP = [1] * len(seq)
	
	for i in range(1, len(seq)):
		for j in range(i):
			if seq[i] > seq[j]:
				DP[i] = max(DP[i], DP[j] + 1)
		m = max(DP)
		k = DP.index(m)
		A = []
		for j in range(k, -1, -1):
			if DP[k] == m:
				A.append(seq[k])
				m -= 1
				
		A.reverse()
		for j in range(len(A)):
			x[i] += A[j]
	
	index = DP.index(max(DP))
	return DP[k], x[k]

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
print(lis)

# 설명
# 위 알고리즘은 DP를 이용하여 가장 긴 증가 부문자열을 찾는 것이다.
# 먼저 DP[i] = seq[i]로 끝나는 증가 부문자열중 가장 긴 증가 부문자열의 길이를 담는다.
# 그러기 위해 seq 리스트의 값을 seq[0]를 제외하고 돌기 위해 for문으로 1부터 len(seq)차례대로 반복한다.
# 그 다음 seq[0]부터 seq[i]까지 반복하며 seq[j]가 seq[i]보다 작으면, seq[j]가 seq[i]로 끝나는 증가하는 부문자열에 들어갈 수 있으므로 DP[i]를 업데이트 한다.
# 그 다음 for문은 seq[i]로 끝나는 가장 긴 부문자열을 리스트 x에 담기 위해 하나씩 거슬러 올라가며 DP[index]가 m이면 그 문자가 seq[i]로 끝나는 가장 긴 부문자열에 포함되는 것이므로 리스트 A에 추가한다.
# 그렇게 만들어진 A는 거슬러 올라가며 문자를 받은 거이므로 reverse를 시켜 seq[i]로 끝나는 LIS를 구할 수 있다.

# 위 코드의 점화식 T(n)이라 할 떄 다음이 성립한다.
# T(n) = T(n-1) + Cn (C = 상수)
# 따라서 수행시간은 O(n^2)임을 알 수 있다.