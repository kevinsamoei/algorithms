def find_max_min (seq):

	""" returns in an array containing the min and max number, respectively"""
  
  for items in seq:
    
    if min(seq) != max(seq):
      return [min(seq), max(seq)]
      
    else:
      return [len(seq)]