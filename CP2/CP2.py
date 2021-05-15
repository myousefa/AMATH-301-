import numpy as np

### Problem 1
### Initialize A as a 20 by 21 matrix of zeros (Week 2 Lecture 1)
### To fill in the matrix create a nested for loop (Week 2 Lecture 1)
### Save the matrix A as the variable A1
### Don't forget to use .copy()

def initializeArray():
    rows = 20
    cols = 21
    A = np.zeros((rows,cols))
    for idx1 in range(rows):
        num1 = idx1 + 1 # row placement num
        for idx2 in range(cols):
            num2 = idx2 + 1 # col placement num
            A[idx1,idx2] = 1/(num1*num2)
    return A

A = initializeArray()
A1 = A.copy()

### Let B equal A, and set the entire 15th row as zero (Week 1 Lecture 3)
### Do the same thing for the entire 16th column
### Save the matrix B as A2
### Don't forget to use .copy()

def change_row_cols(B):
    B[:,16] = B[:,16] * 0
    B[15,:] = B[15,:] * 0
    return B

B = A.copy()
A2 = change_row_cols(B)


### For A3, since we want the last few columns/rows you want to use negative
### values to go backwards through the circular queue (Week 1 Lecture 3)

def get_rows_cols(C):
    C = C[-3:,-5:]
    return C

C = B.copy()
A3 = get_rows_cols(C)

### Set A4 as the 10th column of B (Week 1 Lecture 3)
### reshape it into a column vector

def get_col(D):
    D = D[: , 10:11]
    return D

D = B.copy()
A4 = get_col(D)

### Problem 2
### For A5 and A6 it's exactly like Week 2 Theory lecture.
def init_harmonic_series(size:int):
    harmonic = np.array([])
    for i in range(1,size+1):
        harmonic = np.append(harmonic, [1/i])
    return harmonic

A5 = init_harmonic_series(20)
A6 = init_harmonic_series(200)

### For A7 through A10 you're still doing a Sum as you did for A5 and A6
### but now you want to break out of the loop when the sum surpasses 10
### for A7 and A8, and 20 for A9 and A10
### (very similar to Week 2 Lecture 2 Fibonacci)

def harmonic_sum(size:int):
    harmonic = np.array([])
    summation =  0
    i=1
    while summation <= size:
        harmonic = np.append(harmonic, [1/i])
        i+=1
        summation += harmonic[len(harmonic) - 1]
    return i,summation

ans = harmonic_sum(10)
A7 = ans[0]
A8 = ans[1]

#ans = harmonic_sum(20)
#A9 = ans[0]
#A10 = ans[1]


### Problem 3
### Create a function here (Week 2 Lecture 3).  The function will take r,
### x0, and N as inputs and output a vector x of all N iterates starting at
### x0.  Inside the function create a loop that calculates the value of the
### logistic map and saves it in its respective entries of x.

def dds(r:float,x0:float,n:int):
    data = []
    xn = x0
    for i in range(n):
        x = r * xn * (1 - xn)
        data.append(x)
        xn = x
    row = np.array(data) # shape (100,)
    col = np.reshape(row, (1,100))
    return row,col

### Set N and x0 according to the assignment file

### For each of the next three set its respective r value.  Then set the
### vector x as the iterates of the logistic map using the output of the
### function you created.

### Write the code for A11 and A12 here

A11_row,A11 = dds(r=2.75,x0=0.2,n=100)
behavior = 1
x_std = np.std(A11)
### Do the same as above except for A13 and A14

A13_row,A13 = dds(r=3.25,x0=0.2,n=100)
behavior = 2
x_std = np.std(A13)
### Do the same as above except for A15 and A16
A15_row,A15 = dds(r=3.75,x0=0.2,n=100)
behavior = 3
x_std = np.std(A15)