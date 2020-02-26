class Planet(object):

    def __init__(self,mass,gravity,yearLength):
        self.mass = mass
        self.gravity = gravity
        self.yearLength = yearLength

    def __str__(self):
        return f"mass: {self.mass}, gravity: {self.gravity}, year length: {self.yearLength} days"
        
        
