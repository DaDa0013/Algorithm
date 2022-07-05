class MaxHeap: # max_heap으로 정의함!
	def __init__(self):
		self.A = []
	
	def __str__(self):
		return str(self.A)

	def __len__(self):
		return len(self.A)

	def insert(self, key):
		self.A.append(key)
		self.heapify_up(len(self.A)-1)

	def heapify_up(self, k):
		while k > 0 and self.A[(k-1)//2] < self.A[k]:
			self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
			k = (k-1)//2
	
	def heapify_down(self, k):
		n = len(self.A)-1
		while n >= 2*k +1:# 자식 노드가 있는가?
			L, R= 2*k + 1, 2*k + 2
			m = k # m = (A[k], A[L], A[R]) 중 작은 값을 가지는 index
			if self.A[k] < self.A[L]:
				m = L
			if n >= R:
				if self.A[m] < self.A[R]:
					m = R
			if k == m:
				break
			else:
				self.A[k], self.A[m]= self.A[m], self.A[k]
				k = m

	def findMax(self):
		# 빈 heap이면 None 리턴, 아니면 min 값 리턴
		# code here
		if len(self.A) == 0:
			return None
		return self.A[0]

	def deleteMax(self):
		# 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴
		# code here
		if len(self.A)==0:
			return None
		key=self.A[0]
		self.A[0],self.A[-1] = self.A[-1],self.A[0]
		self.A.pop()
		self.heapify_down(0)
		

def solve(A):
	maxHeap = MaxHeap() 
	n = len(A)
	D = [0]* n # 연산 횟수 저장
	result = 0
	
	maxHeap.insert(A[0])
	
	for i in range(1, n):
		maxHeap.insert(A[i])
		m = maxHeap.findMax() # 비교 대상
		if m > A[i]: #오름차순이 아닐 때
			D[i] = m - A[i] # 연산횟수 저장
			maxHeap.deleteMax() # max값은 오름차순으로 변경한 리스트 A의 최댓값
			maxHeap.insert(A[i])
		result += D[i]
	return result

A = [int(x) for x in input().split()]
print(solve(A))

# <알고리즘 설명>
# 먼저 이 코드에서 리스트 D는 연산 횟수를 저장한다. 
# 이 알고리즘은 오름차순으로 변경했을 떄 리스트의 현재 최댓값이랑 A[i]의 값을 비교하여 연산횟수를 구하는 방식이다.
# 그렇기 떄문에 오름차순으로 변경된 리스트의 현재 최댓값을 빠르게 찾기 위해 maxHeap을 사용하였다.
# 그래서 비교했을 때 현재 값(A[i])이 MaxHeap의 max값보다 작다면 이는 오름차순이 아니므로 리스트 D에 해야하는 최소 연산 횟수인 두 수의 차를 넣는다.
# 최댓값을 삭제하고, heap에 A[i]을 넣어 새로 변경된 오름차순리스트의 최댓값을 찾는다. 이를 for문으로 n-2번 반복한다.
# 마지막으로 최소 연산횟수를 누적하여 더하여 최소 연산 횟수를 구한다.


# <수행시간 분석>
# Heap을 사용했으므로 O(logn)이고 for문으로 n-2 반복하므로 총 수행시간은 O(nlogn)이다.

