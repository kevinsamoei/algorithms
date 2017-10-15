# recursion

def power(a,b):
  if b == 0:
    return 1
  else:
  	return a * power(a, b - 1)
    # return eval(((str(a)+"*")*b)[:-1])

# Iteration
def power(a, b):
	result = 1
	for i in range(b):
		result *= a
	return result


print power(2,10)