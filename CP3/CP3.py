import numpy as np
import scipy.linalg as la

A = np.genfromtxt('bridge_matrix.csv', delimiter=',') ### Don't delete this line

################################################################################

### Problem 1
### A is already initialized above from a separate file (don't delete line 4).
### Initialize the data (right hand side) b.





### Solve for the force vector and save it as A1




### Compute the PA = LU factorization of A
### You may want to use some of these variables later on so don't forget to
### use .copy() wherever appropriate
### Save L AS A2, and c as A3.






### Create a loop that breaks when one of the forces is greater than 20 tons
### Save A4 as the weight of the truck in position 8
### Save A5 as the entry of the force vector that exceeds 20 tons






### Problem 2
### Initialize, alpha, omega, and A, and compute the PA = LU factorization





### The initializations can get a little tricky so definitely ask for help
### if you're stuck.
### Initialize a matrix made up of the position vector at each time
### Set the first x and y coordinates at time = 0 in your matrix
### to the values instructed in the assignment file.
### Create a loop that loops through each time given in the assignment file.
### Compute the new right hand side c using P, L, and/or U.
### You may need to recall that the inverse of P is P transpose
### Solve for the position by solving the Ux = c equation.
### Save all x coordinates as A6
### Save all y coordinates as A7
### Save the distance from the origin as A8





### Initialize a position vector
### Initialize a distance variable
### Initialize a time variable
### Create a loop that breaks when the distance from the origin is
### less than 0.06.
### In the loop compute the position using P, L, and/or U and
### compute the distance from the origin.
### Iterate time at each iteration of the loop.
### Save the time the loop breaks as A9.
### Save the distance from the origin as A10.





### Problem 3
### Create a function here for the rotation matrix that
### takes an input in radians and returns the matrix.




    
    
### Save A11 as R(pi/8)
### Rotate the vector given in the assignment file and save it as A12.






### Find the vector x that was rotated to give you vector b.
### Save the vector x as A13






### Invert the R(3*pi/4) and save it as A14.
### Find the angle theta that would give you this inverse
### without having to do matrix operations, and save the angle
### as A15.




