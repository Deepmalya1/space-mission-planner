import numpy as np
from astropy import units as u
from astropy.constants import au,G,M_sun
def calculate_hohmann_transfer(distance_1,distance_2):
    distance_1 = distance_1 * au
    distance_2 = distance_2 * au

    velocity_1 = np.sqrt(G*M_sun/distance_1)
    velocity_2 = np.sqrt(G*M_sun/distance_2)

    delta_v = np.abs(velocity_2 - velocity_1)
    return delta_v.to(u.km/u.s)
# print(calculate_hohmann_transfer(1, 1.5))