# Python program for multiplying two matrices, using neither matrix multiplication operator '@', nor NumPy: 

print("Enter the number of rows in the first matrix: ")
p = int(input()) 
while p <= 0: 
    print("Number of rows must be a positive integer. Please enter a positive integer: ")
    p = int(input()) 

print("Enter the number of columns in the first matrix, or number of rows in the second matrix: ")
q = int(input()) 
while q <= 0: 
    print("Number of rows or columns must be a positive integer. Please enter a positive integer: ")
    q = int(input()) 

print("Enter the number of columns in the second matrix: ")
r = int(input()) 
while r <= 0: 
    print("Number of columns must be a positive integer. Please enter a positive integer: ")
    r = int(input()) 

A = [] 
print("Thank you. \n\n Please enter elements of the first matrix. It has", p, "rows and", q, "columns.") 
for i in range(p): 
    row = []
    for j in range(q): 
        print("Enter element in row", i, "and column", j, ": ")
        row.append(float(input())) 
    A.append(row) 
print("Thank you. You have entered the first matrix as below. It has", p, "rows and", q, "columns.") 
for i in range(p): 
    for j in range(q): 
        print(round(A[i][j], 3), end = '\t\t') 
    print() 

B = [] 
print("\n\n Please enter elements of the second matrix. It has", q, "rows and", r, "columns.") 
for i in range(q): 
    row = []
    for j in range(r): 
        print("Enter element in row", i, "and column", j, ": ")
        row.append(float(input())) 
    B.append(row) 
print("Thank you. You have entered the second matrix as below. It has", q, "rows and", r, "columns.") 
for i in range(q): 
    for j in range(r): 
        print(round(B[i][j], 3),  end = '\t\t') 
    print() 

C = [] 
for i in range(p): 
    row = []
    for j in range(r): 
        e = 0.0 
        for k in range(q): 
            e = e + (A[i][k] * B[k][j]) 
        row.append(e) 
    C.append(row) 

print("\n The result of multiplying these 2 matrices is the following matrix, with", p, "rows and", r, "columns: ") 
for i in range(p): 
    for j in range(r): 
        print(round(C[i][j], 3),  end = '\t\t') 
    print() 
