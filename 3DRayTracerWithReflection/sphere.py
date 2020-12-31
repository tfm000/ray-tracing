class Sphere:
    '''
    A 3D structure.
    Has centre, radius and material
    '''
    
    def __init__(self,centre, radius,material):
        self.centre = centre
        self.radius = radius
        self.material = material
        
    def intersects(self,ray):
        '''
        Checks if a ray intersects the sphere.
        Returns either distance to intersection or None if there is no intersection.
        '''
        sphere_to_ray = ray.origin - self.centre
        
        b = 2*ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - (self.radius**2)
        discriminant = b**2 - 4*c
        
        if discriminant >= 0:
            distance = (-b - (discriminant**0.5))/2
            if distance > 0:
                return distance
        return None
        
    def normal(self,surface_point):
        '''
        returns surface normal at surface_point on the sphere
        '''
        # this is very easy to calculate for a sphere, which is why we use them for ray tracing
        return (surface_point-self.centre).norm_as_vector()