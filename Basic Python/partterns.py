for i in range(4):
	for j in range(4):
		print('*', end='')

	print('i')
# Result: ****i
# 		  ****i
# 		  ****i
# 		  ****i

for i in range(4):
	for j in range(i + 1):
		print("*", end='')
	print(i)
# Result
	# 0
	# *1
	# ** 2
	# ** *3
	# ** ** 4

for i in range(4):
	for j in range(4-i):
		print("*", end='')
	print(i)

# Result:
#    ****0
#    ***1
#    **2
#    *3