class Heap:
	def __init__(self, L=[]):
		self.A = L
		self.make_heap(self.A)
	def __str__(self):
		return str(self.A)

	def heapify_down(self, k, n):
		while n>= 2*k +1:# 자식 노드가 있는가?
			L, R= 2*k + 1, 2*k + 2
			m = k # m = (A[k], A[L], A[R]) 중 작은 값을 가지는 index
			if L<n and self.A[L]>self.A[k]:
				m = L
			if n > R and self.A[R]>self.A[m]:
				m = R
			if m != k:
				self.A[k], self.A[m] = self.A[m], self.A[k]
				k = m
			else:
				break
				
	def make_heap(self,A):
		n = len(self.A)
		for k in range(n-1, -1, -1):
			self.heapify_down(k,n)
			
	def heap_sort(self):
		n = len(self.A)
		self.make_heap(self.A)
		
		for k in range(len(self.A)-1 , -1, -1):
			self.A[0],self.A[k] = self.A[k], self.A[0]
			n -= 1
			self.heapify_down(0, n)
			

L = [int(x) for x in input().split()]
H = Heap(L)
H.heap_sort()
print(H)