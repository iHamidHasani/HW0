import numpy as np
from scipy import linalg


def sum_numbers(x, y):
    """
    TODO: IMPLEMENT ME
    Sum two numbers.

    Args:
        x (int, float): first number in sum
        y (int, float): second number in sum
    Returns:
        Sum of x and y.
    """
    # replace the following line with an actual implementation that returns something
    #raise NotImplementedError
    return x+y
def multiply_numbers(x, y):
    """
    TODO: IMPLEMENT ME
    Multiply two numbers.

    Args:
        x (int, float): first number in product
        y (int, float): second number in product
    Returns:
        Product of x and y.
    """
    
    # replace the following line with an actual implementation that returns something
    return x*y

def create_add_matrix(x):
    """
    TODO: IMPLEMENT ME
    Step 1. Create a 3x3 numpy array whose elements are all ones.
    Step 2. Sum the array and the input array x.
    Step 3. Return the result
    
    Args:
        x (np.ndarray): a 2D numpy array
    Returns:
        output (np.ndarray): the operation result
    """

    # replace the following line with an actual implementation that returns something
    ones3=np.ones((3,3))
    sumwith=ones3+x
    return sumwith
    
def indexing_aggregation(x, n):
    """
    TODO: IMPLEMENT ME
    Return the mean value of the first n elements of the input array x.

    Args:
        x (np.ndarray): a 1D numpy array
    Returns:
        output (float): the operation result

    """
    # replace the following line with an actual implementation that returns something
    return np.mean(np.array(x)[:n])
  
def matrix_inverse(A):
    """
    TODO: IMPLEMENT ME
    Return the inverse of Matrix A.
    
    Checks for dimension mismatch

    Args:
        x (np.ndarray): a 2D numpy array
    Returns:
        output (np.ndarray): the operation result

    """
    # replace the following line with an actual implementation that returns something
    if (A.shape[0] != A.shape[1]):
        return None
    else:
        return np.linalg.inv(A) 

