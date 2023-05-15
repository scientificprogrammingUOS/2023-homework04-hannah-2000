import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array1, array2, axis = 0):
    array1 = array1.squeeze()
    array2 = array2.squeeze()
    con_array = np.concatenate((array1, array2), axis)
    try:
        np.concatenate((array1, array2), axis)
    except ValueError:
        raise ValueError("arrays can not be combined along given axis")
    
    return con_array


if __name__ == "__main__":
    # use this for your own testing!

    pass
