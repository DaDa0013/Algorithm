import heapq

def solve(A, k): # return k-th smallest key, 1 <= k <= n
	for i in range(k-1):
		heapq.heappop(A)
	return A[0]

k = int(input())
A = [int(x) for x in input().split()]
heapq.heapify(A) # A is now a min-heap
print(solve(A, k))
# 주석

# 코드 설명

# min heap은 루트의 값이 최솟값인 트리이다. 
# 따라서 k번째 작은 수를 구하기 위해, (k-1)번 최솟값을 없애고 min heap으로 정렬한다.
# 이를 위헤 solve 함수를 통해 for로 최솟값을 삭제하고 min heap으로 정렬하는 것을 (k-1)번 반복한다.
# k-1번 반복하면 맨 위의 값이 k번째로 작은 수이기 때문에 이를 return한다.


# 수행시간 분석

# solve 함수에선 수행시간이 O(logn)인 heappop함수를 for문으로 (k-1)번 반복한다.
# 따라서 solve 함수의 시간복잡도는 O(klogn)이고 k가 n만큼 크다면 O(nlogn)이다.
# 그 다음 k와 리스트 A를 입력받고, 시간복잡도가 O(n)인 heapify 함수를 사용하여 리스트 A를 min heap으로 만든다.
# 그러므로 코드의 수행시간은 O(n+nlogn), 즉 O(nlogn)임을 알 수 있다.


# 알고리즘 비교
#  1. 장점:
#		quick_select 알고리즘과 달리 최악의 경우에도 O(nlogn)을 유지한다.
#		또한 k값이 충분히 작아 n보다 작다면 O(n + klogn)으로, O(n)시간만에 할 수 있다.
#		그리고 힙 정렬은 추가적인 메모리가 O(1)정도로 매우 작다.


#  2. 단점:
#		실제 시간 측정시 힙정렬을 해야하므로 들어오는 데이터 값에 따라 조금 더 느린 편이다.
#		또한 반복적으로 최솟값을 삭제하고 정렬하여 k번째 값을 찾는 알고리즘이므로 들어오는 데이터 값의 순서를 유지하기 힘든 unstable한 알고리즘이다.
#		이로 인해 다른 알고리즘들과 달리 코드를 수행 후엔 원본 데이터를 따로 저장하지 않는다면 원본 데이터를 찾을 수 없다.
#		또한 k값을 여러 개로 한다면 원본 데이터값이 유지되지 않기 때문에 다른 알고리즘과 달리 찾으려는 값이 전에 계산할 떄 삭제되어 찾을 수 없는 경우도 있다.