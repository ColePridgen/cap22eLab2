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

import os

#check if folder exists
def basic_io(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return None
    
    result = {
        'number_of_files_or_folders': 0,
        'files_or_folders_names': [],
        'files_or_folders_types': []
    }


    items = os.listdir(folder_path)
    items.sort()

    for item in items:
        result["files_or_folders_names"].append(item)
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            result["files_or_folders_types"].append("file")
            result["files_or_folders_names"].append(os.path.basename(item_path))
            result["number_of_files_or_folders"] =+ 1
        else:
            result["file_or_folder_types"].append("folder")

    result["number_of_files_or_folders"] = len(result["files_or_folders_names"])
    return result

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

    folder_info = basic_io("/Users/colepridgen/Desktop/ISC4221")
print(folder_info)

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



