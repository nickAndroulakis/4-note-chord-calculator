import random 

file = open("output.txt") 
text_list = file.readlines() 

random.shuffle(text_list)

file = open("output_suffled.txt", 'w') 
file.writelines(text_list) 
file.close() 

file = open("output_simple.txt") 
text_list = file.readlines() 

random.shuffle(text_list)

file = open("output_simple_suffled.txt", 'w') 
file.writelines(text_list) 
file.close() 