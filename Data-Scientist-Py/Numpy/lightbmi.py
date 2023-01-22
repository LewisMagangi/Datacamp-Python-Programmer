# height_inch and weight_lb are available as regular lists
height_inch = [80, 70, 65, 72, 88, 76, 93, 59]
weight_lb = [180, 170, 165, 172, 188, 176, 193, 159]

# Import numpy
import numpy as np

# Create array from height_inch with metric units: np_height_m
np_height_m = np.array(height_inch) * 0.0254

# Create array from weight_lb with metric units: np_weight_kg
np_weight_kg = np.array(weight_lb) * 0.453592

#bmi
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = np.array(bmi < 21)

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
