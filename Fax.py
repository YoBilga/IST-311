def main(x):
	for i in range(1, x + 1):
		print((i),end = "")
	for j in reversed(range(1, x)):
		print((j), end = "")
z = int(input())
a = z 
for j in range(1, z + 1):
	print(end=" " * a)
	main(j)
	print('')
	j += 1
	a -= 1

