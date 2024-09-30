"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
from math import sqrt

num_lst = [1, 2, 3, 4, 5]

#option 1: calculate the standard deviation using for loops, no functions required

def std_loops(x):
    """
    Compute standard deviation of x using loops
    
    Parameters:
        x: sequence of numbers
        std: standard deviation (float, rounded to 2 digits) of the list of numbers
    """
    sum = 0
    sum_sq = 0
    i = 0
    
    #find the sum of num_lst
    for x in num_lst:
        sum += x
        i += 1
        
    #calculate the mean
    x_mean = sum / i
    
    #compute the mean of squares
    for x in num_lst:
        sum_sq += x**2
        x_mean_sq = sum_sq / i

    #compute the variance
    variance = x_mean_sq - x_mean**2
    
    #compute the standard deviation
    std = sqrt(variance)
    
    return(std)
    
print(f'the standard deviation calculated using method 1 is {std_loops(num_lst):.2f}')
        

num_lst = [1, 2, 3, 4, 5]

#option 2: calculate the standard deviation using python's built-in functions
def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum() and ln()
    
    Parameters:
        x: sequence of numbers
        std: standard deviation (float, rounded to 2 digits) of the list of numbers
    """
    #calculate the mean
    x_mean = sum(num_lst) / len(num_lst)
    
    #compute the mean of squares
    x_mean_sq = sum(x**2 for x in num_lst) /len(num_lst)
    
    #compute the variance
    variance = x_mean_sq - x_mean**2
    
    #compute the standard deviation
    std = sqrt(variance)
    
    
    return (std)

print(f'the standard deviation calculated using method 2 is also {std_builtin(num_lst):.2f}')
    
import numpy as np

#calculate the standard deviation directly
std_np = np.std(num_lst)
print(f'the standard deviation calculated using method 3 is also {std_np:.2f}')


#check that they are all correct
if std_loops(num_lst) == std_builtin(num_lst) == std_np:
    print ('the methods are correct, all the functions give the same standard deviaton')