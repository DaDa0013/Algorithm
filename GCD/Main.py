def gcd_sub(a, b):
	while (a*b!=0):
		if (a>b):
			a=a-b
		else:
			b=b-a
	return a+b
def gcd_mod(a, b):
		while (a*b!=0):
			if(a>b):
				a=a%b
			else:
				b=b%a
		return a+b
def gcd_rec(a, b):
		if (a*b!=0):
			return gcd_rec(b,a%b)
		else:
			return a
		
a,b=input().split()
a=int(a)
b=int(b)


x=gcd_sub(a,b)
y=gcd_mod(a,b)
z=gcd_rec(a,b)

print(x, y, z)