def words(word):
 
 """
        Counts the occurrences or characters in a word
    """
 str_list = word.split()
 str_dict={}
 str_dict_output =[]
 for item in str_list:
   try:
     int(item)
     
   except ValueError:
     str_dict_output.append(item)
   
   else:
     str_dict_output.append(int(item))
 
 for item in str_dict_output:
   str_dict[item] = str_dict_output.count(item)
     
 return str_dict
    
