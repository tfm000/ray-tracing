from vector import Vector

class Colour(Vector):
    '''
    Stores colour as RGB vectors
    '''
    @classmethod
    def from_hex(cls,hexcolour = "#000000"):
        '''
        Converts a hex-colour string to an RGB vector
        '''
        x = int(hexcolour[1:3],16)/255.0
        y = int(hexcolour[3:5],16)/255.0
        z = int(hexcolour[5:7],16)/255.0
        
        return cls(x,y,z)