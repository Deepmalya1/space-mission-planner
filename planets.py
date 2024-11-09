class Planet:
    def __init__(self,name,semi_major_axis,eccentricity,periapsis,apoapsis):
        self.name = name
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.periapsis = periapsis
        self.apoapsis = apoapsis
    def __rapr__(self):
        return f"{self.name}: a={self.semi_major_axis} AU , e={self.eccentricity} , periapsis = {self.periapsis} AU , apoapsis = {self.apoapsis} AU"

mercury = Planet("Mercury", 0.387, 0.206, 0.307, 0.467)
venus = Planet("Venus", 0.723, 0.007, 0.718, 0.728)
earth = Planet("Earth", 1.0, 0.017, 0.983, 1.017)
mars = Planet("Mars", 1.524, 0.093, 1.381, 1.666)
jupiter = Planet("Jupiter", 5.203, 0.049, 4.951, 5.456)
saturn = Planet("Saturn", 9.582, 0.056, 9.049, 10.116)
uranus = Planet("Uranus", 19.191, 0.046, 18.287, 20.107)
neptune = Planet("Neptune", 30.067, 0.010, 29.814, 30.420)
pluto = Planet("Pluto", 39.482, 0.249, 29.658, 49.305)

# List of all planets
planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]