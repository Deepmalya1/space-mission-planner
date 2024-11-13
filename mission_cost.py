import numpy as np

def mission_cost_estimator(spacecraft_mass, delta_v, cost_per_kg, cost_per_kg_fuel):
    

   
    exhaust_velocity = 4500  
    fuel_mass = spacecraft_mass * (np.exp(delta_v / exhaust_velocity) - 1)
    
    # Calculate total cost
    launch_cost = spacecraft_mass * cost_per_kg
    fuel_cost = fuel_mass * cost_per_kg_fuel
    
    total_cost = launch_cost + fuel_cost
    return total_cost

# # Example usage
# spacecraft_mass = 5000  # kg
# delta_v = 3500  # m/s
# cost_per_kg = 5000  # USD per kg (example)
# cost_per_kg_fuel = 1000  # USD per kg of fuel

# total_cost = mission_cost_estimator(spacecraft_mass, delta_v, cost_per_kg, cost_per_kg_fuel)
# print(f"Estimated Mission Cost: ${total_cost:.2f}")
