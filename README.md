# FSU_ISC4221C_Fall24_Lab2

# Python basics assignment

The objective of this homework is to review some basics concepts of python, together with 
the basics of [NumPy](https://numpy.org/doc/stable/user/absolute_beginners.html) and 
[Matplotlib](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#sphx-glr-tutorials-introductory-quick-start-py).

For this assignment you need to make a markdown report file called `report.md` with the answers to the questions below and the code you used to solve them. For the auto-grading to work properly, all of your answers must be written in a file called `answers_module.py` in the 'root' folder of this repo (except the last question).

## Loops, conditionals, recursive functions (5 pts)
1) Make a function called **myrec** that computes $f(x) = 2*x - f(x-1)$ for values greater than 0 (0 if x == 0).

The function **must** raise any type of exception if the input number $x$ is < 0.
```python
def myrec(x):
```

## IO (5 pts)
2) Make a function called **basic_io** that will input a path to a folder and return the following information 
in a **dictionary**: *number of files or folders*, *a list containing the names of the files or folders*, 
and a *list containing 'file' or 'folder' depending if the corresponding file is a file or a folder*. 

Additional info:
1. Be sure that the **keys** of your dictionary are the same as the ones bellow.
2. The **files** list **must** be **sorted**. (containing the names of files or folder inside the path)
3. The function should print **"Folder does not exist."** if the input folder does not exist. 

Tip. If you do not know where to start look at `os` and `os.path`.

```python
# Example output
output= {'number_files': X,
         'files': ['name1', 'name2'],
         'file_or_folder': ['file', 'folder'],
         }
```

# Numpy (5 pts)

3) Make a function called **add2and3** that will input a matrix and **sum** all the elements of the second row and
the elements of the third column of any matrix bigger than a (2x3). 
The function will print **"Matrix too small."** if the matrix does not have the proper size.
 
4) Make a function called **squareme**. This function will receive a matrix and a row number, it will return an *ndarray* 
with the squared numbers of the specified row. The function will print **"Row not found."** if the specified row number does not exist.

# Matplolib (5 pts)

5) Take a look at the repo [https://github.com/olmozavala/matplotlib_ex](https://github.com/olmozavala/matplotlib_ex).

Select and run two examples from the file `1_Basics.py`. Paste the code and the resulting figures in your report. 
