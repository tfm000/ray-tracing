class Ray:
    '''
    A half line with an origin and normalised direction
    '''
    
    def __init__(self,origin,direction):
        self.origin = origin
        self.direction = direction.norm_as_vector()