
# Find the ideal distance for uniform irradiance bu LED array
# Usig the following formula

from math import sqrt, pi, log, cos
import numpy as np
import matplotlib.pyplot as plt

def deg2rad(value=0.0):
	return value * pi / 180

# The angle at which the irradiance is half of the irradiance at 0 deg 
thetha = 15;

# the constant m that is a factor of the dropoff of intensity
m = -log(2) / log( cos(deg2rad(thetha)))

# for a circular spaced array with radius r
r = np.arange(15, 30, 1);

# the distance at which the illuminance is most uniform is proportional to
# the radius of the array with the following factor
k = sqrt(2 / (m + 2))

# the formula for maximum distance of the uniform irradiance area is
z =  r / k;

plt.plot(r,z)
plt.show()



 
