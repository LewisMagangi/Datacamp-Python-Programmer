# import library
import numpy as np

# create numpy 1d-array
array1 = np.array([0, 2, 4])
array2 = np.array([6, 8, 10])

# pearson product-moment correlation
# coefficients of the arrays
rslt = np.corrcoef(array1, array2)

print(rslt)
