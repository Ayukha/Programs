def gcd(m,n):
	if m<n :     # assume m>=n
		(m,n) = (n,m)

	while(m%n) !=0:
		(m,n) = (n,m%n)  # m%n < n, always!

	print(n)

if __name__ == '__main__':
	gcd(input(),input())