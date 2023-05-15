import numpy as np

# implement the function strange pattern

def strange_pattern(s_tuple):

    #np array with shape of given tupel and value false
    pattern = np.full(s_tuple, False)
    start = 0
    for row in pattern:
        row[start::3] =  True
        start -=1
        if start < 0:
            start = 2
    return pattern



if __name__ == "__main__":
    # use this for your own testing!
    strange_pattern((6,8))
