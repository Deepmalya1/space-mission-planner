import math

def estimate_fuel(mass_initial,mass_final,specific_impulse):
    g0 = 9.81
    delta_v= specific_impulse * g0 * math.log(mass_initial/mass_final)
    fuel_consumed = mass_initial - mass_final
    return fuel_consumed
# print(estimate_fuel(5000, 3000, 100))  # Example values