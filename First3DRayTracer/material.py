from colour import Colour

class Material:
    '''
    has colour and properties about how it reacts to light
    '''
    
    def __init__(self,colour = Colour.from_hex("#FFFFFF"),ambient = 0.05, diffuse = 1.0,specular = 1.0):
        
        self.colour = colour
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        
    def colour_at(self,position):
        return self.colour