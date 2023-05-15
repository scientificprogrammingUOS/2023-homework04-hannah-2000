import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):

    if not all(isinstance(param, (int, float)) for param in [loc, scale, lower_bound, upper_bound]):
        raise ValueError("loc, scale, lower_bound, and upper_bound must be integers or floats.")
    
    if lower_bound > upper_bound:
        raise ValueError("lower_bound should be smaller than upper_bound")

    distributions = np.random.normal(loc, scale, 100)

    valid_distributions = distributions[(distributions >= lower_bound) & (distributions <= upper_bound)]

    mean = np.mean(valid_distributions)
    std = np.std(valid_distributions)

    return (mean,std)

if __name__ == "__main__":
    # use this for your own testing!

    gaussian_analysis(2,2.2,4.5,1.2)
