def myrec(x):
    if x < 0:
        raise Exception("Input number must be greater than or equal to 0.")
    elif x == 0:
        return 0
    else:
        return 2 * x - myrec(x - 1)
    
x = 1
result = myrec(x)
print(result)

result = 2

####

import os

def basic_io(path):
    # Check if the folder exists
    if not os.path.exists(path):
        print("Folder does not exist.")
        return
    
    # Initialize the lists for names and types
    names_list = []
    types_list = []
    
    # Get the list of files and folders in the directory
    with os.scandir(path) as entries:
        for entry in entries:
            names_list.append(entry.name)
            if entry.is_file():
                types_list.append('file')
            elif entry.is_dir():
                types_list.append('folder')
    
    # Sort the names list
    names_list.sort()
    
    # Create the result dictionary
    result = {
        'number_of_files_or_folders': len(names_list),
        'files_or_folders_list': names_list,
        'type_list': types_list
    }
    
    return result

########

import numpy as np

def add2and3(matrix):
    if matrix.shape[0] < 2 or matrix.shape[1] < 3:
        print("Matrix too small.")
        return
    
    second_row_sum = np.sum(matrix[1, :])
    third_column_sum = np.sum(matrix[:, 2])
    
    return second_row_sum + third_column_sum

def squareme(matrix, row_number):
    if row_number >= matrix.shape[0]:
        print("Row not found.")
        return
    
    row = matrix[row_number, :]
    squared_row = np.square(row)
    
    return squared_row

# Call add2and3() function
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result_add2and3 = add2and3(matrix)
print("Result of add2and3():", result_add2and3)

# Call squareme() function
row_number = 1
result_squareme = squareme(matrix, row_number)
print("Result of squareme():", result_squareme)

Add2and3 = 33
Squareme = [16, 25, 36]

##########

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation
import numpy as np
n = 100
x = np.linspace(0,2*np.pi,n)
y = np.sin(x)

#scatter
fig, ax = plt.subplots(1,1,figsize=(10,10))
ax.scatter(x,y, label='simplest')
ax.scatter(x,y-.3, color='b', alpha=np.linspace(0,1,len(x)), label='alpha')    # alpha
ax.scatter(x,y-.5, c=np.linspace(0,1,len(x)), label='color')                   # color
ax.scatter(x,y-.8, s=np.linspace(0,100,len(x)), label='size')                 # Size
ax.set_title("Scatter")
ax.legend()
plt.show()

#boxplot
fig, ax = plt.subplots(figsize=(10,6))
plt.title('Basic Plot')
names = ['name1', 'name2']
data = [np.random.rand(50) * 100, np.random.rand(50) * 100]
bp = plt.boxplot(data, notch=True, labels= names, patch_artist=True)
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_xlabel("Sopas")
ax.set_ylabel("Pericon")

Scatter
![image](https://github.com/user-attachments/assets/e28af3e6-a801-4619-bfb4-e5c6e567557c)

Boxplot
![image](https://github.com/user-attachments/assets/5d4adc2a-849f-49ac-82c1-df25515e5662)







