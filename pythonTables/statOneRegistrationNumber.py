 
h = open('pythonTables/data.txt', 'r')
 
# Reading from the file
content = h.readlines()
 
# Array to store the digits
all_numbers = []
first_digit = 'a'
second_digit = 'b'


# Iterating through the content
# Of the file
for line in content:
    for i in line:
        # print(i)
        if  i.isdigit() == True:
            if  first_digit == 'a' :
                first_digit = i
                
            elif  second_digit == 'b' :
                second_digit = i
                
        if  i.isdigit() == False:
            if first_digit != 'a' and second_digit != 'b':
                all_numbers.append(first_digit + second_digit)
                
            elif first_digit != 'a' and second_digit == 'b':
                second_digit = first_digit
                first_digit = 0
                all_numbers.append(second_digit)
                
            
            first_digit = 'a'
            second_digit = 'b'
            

             
        
print("Here are all the student marks:", all_numbers)


