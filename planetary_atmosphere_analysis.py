def atmospheric_drag(velocity, area, density, drag_coefficient):
   
    return 0.5 * drag_coefficient * density * area * velocity**2

def thermal_analysis(velocity, area, density, heat_capacity):
    
    return 0.5 * density * velocity**3 * heat_capacity * area

# Example usage for Mars entry
velocity = 5000  # m/s (example for Mars atmospheric entry)
area = 10  # m² (example for spacecraft)
density = 0.02  # kg/m³ (Mars atmospheric density at 20 km altitude)
drag_coefficient = 1.5  # typical value for blunt bodies in atmosphere
heat_capacity = 1000  # J/kg·K (approx. for Mars)

drag_force = atmospheric_drag(velocity, area, density, drag_coefficient)
heat_load = thermal_analysis(velocity, area, density, heat_capacity)

print(f"Drag Force: {drag_force} N")
print(f"Heat Load: {heat_load} Joules")
