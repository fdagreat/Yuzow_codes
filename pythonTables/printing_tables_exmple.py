# Program to append to text file using writelines() function

array1 = [1,2,3]
array2 = [0,9,0]
array3 = [0,9,0]
array4 = [0,9,0]
array5 = [0,9,0]

fullData = [array1,array2,array3,array4,array5]


with open("pythonTables/out.txt", "a") as file:
    headers = ['One ', 'Two ', 'Three']
    z = 0
    d = 0
    file.writelines(headers)
    file.writelines(' \n')
    # print(fullData)
    for i in range(len(fullData)):
        row = []
        
        for f in range(len(fullData[i])):
            cell = str(fullData[i][f])
            row.append(cell)


            if z <= len(headers):
                while d < len(headers[z]):
                    row.append(' ')
                    d = d + 1
                z = z + 1
            d = 0
            z = 0
       
        row.append('\n')
        file.writelines(row)
        

    file.close()
