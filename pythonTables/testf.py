 
h = open('pythonTables/98.txt', 'r')
 
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
            
             
new_numbers = []
for i in range(len(all_numbers)):
    new_numbers.append(int(all_numbers[i]))

        
# print("Here are all the student marks:", new_numbers)


def interval_extract(list):
    length = len(list)
    i = 0
    while (i< length):
        low = list[i]
        while i <length-1 and list[i]+1 == list[i + 1]:
            i += 1
        high = list[i]
        if (high - low >= 1):
            yield [low, high]
        elif (high - low == 1):
            yield [low, ]
            yield [high, ]
        else:
            yield [low, ]
        i += 1

# new_numbers =  [2, 3, 4, 5, 7, 8, 9, 11, 15, 16]

print('NOT Sorted  Numbers: ', new_numbers)
new_numbers.sort()

print('Sorted Numbers: ', new_numbers)

print('here are the class intervals : ', list(interval_extract(new_numbers)))

