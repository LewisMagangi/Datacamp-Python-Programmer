# height_inch is available as a regular list
height_inch = [80, 70, 65, 72, 88, 76, 93, 59]

# Import numpy
import numpy as np

# Create a numpy array from height_inch: np_height_in
np_height_inch = np.array(height_inch)

# Print out np_height_inch
print(np_height_inch)

# Convert np_height_inch to m: np_height_m
np_height_mtrs = np_height_inch * 0.0254

# Print np_height_mtrs
print(np_height_mtrs)
