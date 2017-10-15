def fizz_buzz(x):
  """ Funtion returns 'Fizz' if number is divisible by 3,
  'Buzz' if divisible by 5 and 'FizzBuzz if divisible by both 3 and 5'
   """
   #if number is divisible by both 3 and 5 return 'FizzBuzz'
  if x % 3 == 0 and x % 5 == 0:
    return "FizzBuzz"
    
  elif x % 3 == 0: #If number is divisible by 3 return "Fizz"
    return "Fizz"
    
  elif x % 5 == 0: #and if number is divisible by 5 return 'Buzz'
    return "Buzz"
    
  else:        #Otherwise just return the number
    return x