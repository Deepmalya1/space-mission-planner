class SpacecraftResources:
    def __init__(self, food_supply, oxygen_supply, crew_space, food_per_person, oxygen_per_person):
        """
        Initializes spacecraft resources and crew allocation parameters.
        
        :param food_supply: Total food supply in kilograms (kg).
        :param oxygen_supply: Total oxygen supply in cubic meters (m³).
        :param crew_space: Total space available in cubic meters (m³) for crew.
        :param food_per_person: Food consumption per person per day in kilograms (kg).
        :param oxygen_per_person: Oxygen consumption per person per day in cubic meters (m³).
        """
        self.food_supply = food_supply
        self.oxygen_supply = oxygen_supply
        self.crew_space = crew_space
        self.food_per_person = food_per_person
        self.oxygen_per_person = oxygen_per_person
        self.people_requesting = 0  # Track how many people want to join

    def calculate_max_crew(self):
        """
        Calculates the maximum number of crew members that can be accommodated 
        based on the available food, oxygen, and space.
        
        :return: Maximum number of crew members that can be accommodated.
        """
        max_food_crew = self.food_supply // self.food_per_person
        max_oxygen_crew = self.oxygen_supply // self.oxygen_per_person
        max_space_crew = self.crew_space // 10  # Assume 10 cubic meters per person for space
        
        return min(max_food_crew, max_oxygen_crew, max_space_crew)

    def people_wanting_to_join(self, people):
        """
        Updates the number of people requesting to join the mission.
        
        :param people: Number of people requesting to join.
        """
        self.people_requesting = people

    def assign_crew_roles(self):
        """
        Assigns crew members to different positions based on available crew size.
        
        :return: Dictionary with crew roles and the number of people assigned to each role.
        """
        # Realistic crew roles including more research positions
        roles = {
            "Commander": 1,
            "Pilot": 1,
            "Flight Engineer": 2,
            "Mission Specialist / Scientist": 2,  # Scientists for research
            "Medical Officer": 1,
            "Communications Officer": 1,
            "Payload Specialist": 1,
            "Mission Control Liaison": 1,
            "Logistics Officer": 1,
            "Flight Surgeon": 1,
            "Engineer (Robotics)": 1,
            "Sustainability Officer": 1,
            "Spacecraft Technician": 2,  # Start with only essential technicians
            "Cybersecurity Specialist": 1,
            # Additional research roles
            "Astrobiologist": 1,
            "Geologist": 1,
            "Biologist": 1,
            "Physicist": 1,
            "Chemist": 1,
        }

        max_crew = self.calculate_max_crew()
        accepted_crew = min(self.people_requesting, max_crew)
        crew_distribution = {}
        remaining_crew = accepted_crew

        # First assign essential roles (Command, Pilot, Medical, etc.)
        for role, required in roles.items():
            if role != "Spacecraft Technician":  # Don't assign Spacecraft Technicians yet
                if remaining_crew >= required:
                    crew_distribution[role] = required
                    remaining_crew -= required
                else:
                    crew_distribution[role] = remaining_crew
                    remaining_crew = 0
                    break

        # Now prioritize research roles if there is room for them
        research_roles = ["Astrobiologist", "Geologist", "Biologist", "Physicist", "Chemist"]
        for role in research_roles:
            if remaining_crew > 0:
                crew_distribution[role] = 1
                remaining_crew -= 1

        # After assigning essential roles and researchers, assign technicians if space allows
        if remaining_crew > 0:
            if "Spacecraft Technician" in crew_distribution:
                crew_distribution["Spacecraft Technician"] += remaining_crew
            else:
                crew_distribution["Spacecraft Technician"] = remaining_crew
        
        return crew_distribution, accepted_crew


# Example usage
# food_supply = 1000  # Total food supply in kg
# oxygen_supply = 5000  # Total oxygen supply in m³
# crew_space = 2000  # Available space in m³
# food_per_person = 2  # Food required per person per day (kg)
# oxygen_per_person = 10  # Oxygen required per person per day (m³)

# spacecraft_resources = SpacecraftResources(food_supply, oxygen_supply, crew_space, food_per_person, oxygen_per_person)

# spacecraft_resources.people_wanting_to_join(200)

# crew_roles, accepted_crew = spacecraft_resources.assign_crew_roles()

# print(f"Number of people accepted: {accepted_crew}")
# print("Crew Roles Allocation:")
# for role, num in crew_roles.items():
#     print(f"{role}: {num} members")
