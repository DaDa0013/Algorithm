import heapq
import re

f = [int(x) for x in input().split()]
n = len(f)
T = []
for i in range(n):
	heapq.heappush(T, (f[i], str(i)))

while len(T) > 1:
	x = heapq.heappop(T)
	y = heapq.heappop(T)
	heapq.heappush(T, (x[0] + y[0], "(" + x[1] + " " + y[1] + ")"))
	
s = heapq.heappop(T)[1]
nbits = [0] * n
bits = 0
ntokens = len(f)
i = 0
while i < len(s):
	if s[i] == "(":
		bits += 1
		i += 1
	elif s[i] == ")":
		bits -= 1
		i += 1
	elif s[i] == " ":
		i += 1
	else:
		token = re.search("[0-9]+", s[i:]).group()
		
		nbits[int(token)] = bits
		i += len(token)
	
print(sum([a * b for (a, b) in zip(f, nbits)]))