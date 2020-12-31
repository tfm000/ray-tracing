class Scene:
    '''
    Contains all the information required for the ray-tracing engine
    '''
    
    def __init__(self,camera,objects,lights,width,height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height
        self.lights = lights