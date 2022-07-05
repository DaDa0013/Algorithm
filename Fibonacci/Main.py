def fibo(n):
	a, b =1,1
	while n>1:
		n-= 1
		tmp = a
		a = b
		b = tmp + b
	return b
n = int(input())
print(fibo(n))
# n을 입력받은 후
# fibo(n) 호출!
# 리턴값을 출력함