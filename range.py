def rang(start, end):
	nums = []
	count =1
	while start <= end:
		nums.append(start)
		start += count
	return nums
print rang(1,10)

def sm(ns):
	output = 0
	for n in ns:
		output += n
	return output

print sm(rang(1,10))

# operator overloading