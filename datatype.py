def data_type(n):
  
  """ This odule checks for different data types for a given data"""
 #check if n is of type string.If it is, return the lenght of n
  if type(n) == str:
    return len(n)
    
  elif n == None: #check if n is None, if it is return 'No value'
    return "no value"
    
  elif type(n) == bool: # if n is of type boolean return the boolean
    return n
    
  elif type(n) == int:  #check if n is an interger. Return "less than 100 if it is less than 100"
    if n < 100:
      return 'less than 100'

    elif n == 100:  # If the integer is equal to 100, "Equal to 100"
      return "equal to 100"

    else:
      return 'more than 100' #if more than 100
      
  elif type(n) == list: # if it is a list return the third element of the list if it exists
    if len(n) >= 3:
      return n[2]
    else:
      return None