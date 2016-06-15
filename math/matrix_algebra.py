# Matrix Algebra

import numpy as np

A = np.array( ([1,2,3],
               [2,7,4])
            )
B = np.array( ([1,-1],
               [0,1])
            )
C = np.array( ([5,-1],
               [9,1],
               [6,0])
            )
D = np.array( ([3,-2,-1],
               [1,2,3])
            )
u = np.array( ([6,2,-3,5]) )
v = np.array( ([3,5,-1,4]) )
w = np.array( ([1],[8],[0],[5]) )


# Matrix Dimensions

print("Shape of A is {}".format(A.shape))
print("Shape of B is {}".format(B.shape))
print("Shape of C is {}".format(C.shape))
print("Shape of D is {}".format(D.shape))
print("Shape of u is {}".format(u.shape))
print("Shape of v is {}".format(v.shape))
print("Shape of w is {}".format(w.shape))

    # Shape of A is (2, 3)
    # Shape of B is (2, 2)
    # Shape of C is (3, 2)
    # Shape of D is (2, 3)
    # Shape of u is (4,)
    # Shape of v is (4,)
    # Shape of w is (4, 1)

# Vector Operations

print (u + v)
print (u - v)
print (6*u)
print (np.dot(u,v))
print (np.linalg.norm(u))

    # [ 9  7 -4  9]
    # [ 3 -3 -2  1]
    # [ 36  12 -18  30]
    # 51
    # 8.60232526704

# Matrix Operations

print("A+C")
try:
    print (A + C)
except ValueError:
    print ("Not Defined")

print("A-C.T")
print (A - C.T)

print ("C.T + 3D")
print (C.T + 3*D)

print("BA")
try:
    print (B.dot(A))
except ValueError:
    print ("Not Defined")

print("BA.T")
try:
    print (B.dot(A.T))
except ValueError:
    print ("Not Defined")

    # A+C
    # Not Defined
    # A-C.T
    # [[-4 -7 -3]
    #  [ 3  6  4]]
    # C.T + 3D
    # [[14  3  3]
    #  [ 2  7  9]]
    # BA
    # [[-1 -5 -1]
    #  [ 2  7  4]]
    # BA.T
    # Not Defined

# Optional

try:
    print(B.dot(C))
except:
    print("Not Defined")
print (C.dot(B))
print(B.dot(B).dot(B).dot(B))
print (A.dot(A.T))
print (D.T.dot(D))

    # Not Defined
    # [[ 5 -6]
    #  [ 9 -8]
    #  [ 6 -6]]
    # [[ 1 -4]
    #  [ 0  1]]
    # [[14 28]
    #  [28 69]]
    # [[10 -4  0]
    #  [-4  8  8]
    #  [ 0  8 10]]
