
# leave the variables below are they are 
all_marks = []
class_intervals = []
class_boundaries = []
class_marks = []
frequencies = []
cumulative_frequencies = []
first_class_interval = 0
number_of_classes = 0


def extractAllNumbers(data):
    # Reading from the file
    content = data.readlines()

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
                
    all_marks = []
    for i in range(len(all_numbers)):
        all_marks.append(int(all_numbers[i]))

            
    

    # all_marks =  [2, 3, 4, 5, 7, 8, 9, 11, 15, 16]

    # print('NOT Sorted  Numbers: ', all_marks)
    all_marks.sort()

    # print('Sorted Numbers: ', all_marks)

    return all_marks

def getFirstClassInterval(all_marks):
    return all_marks[0]

def getNumberOfClasses(all_marks,csize):
    number_of_classes = round((all_marks[-1] - all_marks[0]) / csize)
    return int(number_of_classes)

def createClassIntervals(first_class_interval,csize,number_of_classes):
    class_intervals = [[first_class_interval, csize]]
    number_of_classes = number_of_classes - 1

    for i in range(number_of_classes):
        last_class_interval = class_intervals[-1][-1]
        class_intervals.append([last_class_interval,(last_class_interval+csize)])

    return class_intervals

def createClassboundaries(class_intervals):
    for i in range(len(class_intervals)):
        current_class_interval = class_intervals[i]
        lower_boundary = current_class_interval[0] - 0.5
        upper_boundary = current_class_interval[1] + 0.5
        class_boundaries.append([lower_boundary,upper_boundary])

    return class_boundaries 

def createClassMarks(class_boundaries):
    for i in range(len(class_boundaries)):
        current_class_boundary = class_boundaries[i]
        real_lower_boundary = current_class_boundary[0] 
        real_upper_boundary = current_class_boundary[1]
        class_mark = (real_lower_boundary + real_upper_boundary)/2
        class_marks.append([class_mark])

    return class_marks

def createFrequencies(class_boundaries,all_marks):
    for i in range(len(class_boundaries)):
        current_frequency = 0
        current_class_boundary = class_boundaries[i]
        real_lower_boundary = current_class_boundary[0] 
        real_upper_boundary = current_class_boundary[1]

        
        for i in range(len(all_marks)):
            if all_marks[i] > real_lower_boundary and all_marks[i] < real_upper_boundary:
                current_frequency = current_frequency + 1

        frequencies.append(current_frequency)
    
    return frequencies
        
def createCumulativeFrequencies(frequencies):
    for i in range(len(frequencies)):
        if i == 0:
            frequency = frequencies[i]
            new_cumulative_frequency = frequency
            cumulative_frequencies.append(new_cumulative_frequency)
        else:
            frequency = frequencies[i]
            last_frequency = cumulative_frequencies[-1]
            new_cumulative_frequency = (frequency + last_frequency)
            cumulative_frequencies.append(new_cumulative_frequency)

    return cumulative_frequencies 

def fdtablegd(data,csize,printable):
    all_marks = extractAllNumbers(data)
    print("Here are all the student marks Sorted :", all_marks)
    first_class_interval = getFirstClassInterval(all_marks)
    print("Here is the first Class Interval :", first_class_interval)
    number_of_classes = getNumberOfClasses(all_marks,csize)
    print("Here is the number of Classes :", number_of_classes)
    class_intervals = createClassIntervals(first_class_interval,csize,number_of_classes)
    print("Here are all the Class Intervals marks:", class_intervals)
    class_boundaries = createClassboundaries(class_intervals)
    print("Here are all the Class Boundaries :", class_boundaries)
    class_marks = createClassMarks(class_boundaries)
    print("Here are all the Class Marks :", class_marks)
    frequencies = createFrequencies(class_boundaries,all_marks)
    print("Here are all the Frequencies :", frequencies)
    cumulative_frequencies = createCumulativeFrequencies(frequencies)
    print("Here are all the Cumulative Frequencies :", cumulative_frequencies)

# Main Variables you can change these
data = open('pythonTables/98.txt', 'r')
csize = 10
printable = False

fdtablegd(data,csize,printable)