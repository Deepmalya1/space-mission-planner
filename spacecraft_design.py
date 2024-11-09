import numpy as np

class Spacecraft:
    def __init__(self, mass, propulsion_type, fuel_capacity, critical_mass_percentage=0.9):
       
        self.mass = mass  # Total mass of spacecraft in kg
        self.propulsion_type = propulsion_type  # Propulsion system type
        self.fuel_capacity = fuel_capacity  # Maximum fuel in kg
        self.fuel_remaining = fuel_capacity  # Remaining fuel in kg
        self.critical_mass_percentage = critical_mass_percentage  # Critical mass threshold (90% mass loss)
        self.delta_v = 0  # Delta-v for spacecraft
        self.exhaust_velocity = 4500  # Default exhaust velocity for chemical propulsion (m/s)
    
    def calculate_delta_v(self):
        """Calculates delta-v based on current fuel and mass using Tsiolkovsky's rocket equation."""
        if self.fuel_remaining > 0:
            self.delta_v = self.exhaust_velocity * np.log(self.mass / (self.mass - self.fuel_remaining))
        else:
            print("Out of fuel!")
    
    def mileage_before_damage(self):
       
        critical_mass = self.mass * (1 - self.critical_mass_percentage)  # Critical mass threshold
        distance_travelled = 0
        current_fuel = self.fuel_capacity

        # Simple model: Assume the spacecraft burns fuel at a constant rate depending on delta-v
        while self.mass - current_fuel > critical_mass and current_fuel > 0:
            distance_travelled += 1  # Increase mileage incrementally (simple model)
            current_fuel -= 0.01  # Burn fuel (adjust burn rate as needed)
        
        return distance_travelled * 100  # Convert to kilometers
    
    def display_specs(self):
        print(f"Spacecraft Mass: {self.mass} kg")
        print(f"Propulsion Type: {self.propulsion_type}")
        print(f"Fuel Capacity: {self.fuel_capacity} kg")
        print(f"Delta-v: {self.delta_v:.2f} m/s")

    def show_mileage_before_damage(self):
        mileage = self.mileage_before_damage()
        print(f"Estimated Mileage Before Critical Damage: {mileage:.2f} km")

# Example usage:
spacecraft = Spacecraft(mass=5000, propulsion_type='Chemical', fuel_capacity=100)
spacecraft.calculate_delta_v()
spacecraft.display_specs()
spacecraft.show_mileage_before_damage()
