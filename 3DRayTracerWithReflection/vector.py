#updated

class Vector:
    x: float
    y: float
    z: float
    magnitude : float
    vector : list
    norm : list
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = (x**2 + y**2 + z**2)**0.5
        self.vector = [x,y,z]
        if self.magnitude !=0:
            self.norm = [i/self.magnitude for i in self.vector]
        else: 
            self.norm = None
    
    def norm_as_vector(self):
        if self.norm is not None:
            return Vector(self.norm[0],self.norm[1],self.norm[2])
        else:
            return None
    
    def dot_product(self,v2):
        '''
        the dot product between your current vector and another vector
        v1.dot_product(v2)
        '''
        try:
            dot = 0
            if type(v2) != list:
                for i in range(len(self.vector)):
                    dot += self.vector[i] * v2.vector[i]
            else:
                for i in range(len(self.vector)):
                    dot += self.vector[i] * v2[i]
            return dot
            
        except IndexError as e:
            print("Vector lengths do not match or wrong input type")
    
    def add_vector(self,v2):
        '''
        adds two vectors together
        v1.add_vector(v2)
        '''
        try:
            if type(v2) != list:
                return Vector(self.x+v2.x,self.y+v2.y,self.z+v2.z)
            else:
                return Vector(self.x+v2[0],self.y+v2[1],self.z+v2[2])
            
        except IndexError as e:
            print("Vector lengths do not match or wrong input type")
    
    def sub_vector(self,v2):
        '''
        subtracts v2 from v1
        v1.subtract_vector(v2)
        '''
        try:
            if type(v2) != list:
                return Vector(self.x-v2.x,self.y-v2.y,self.z-v2.z)
            else:
                return Vector(self.x-v2[0],self.y-v2[1],self.z-v2[2])
            
        except IndexError as e:
            print("Vector lengths do not match or wrong input type")
    
    def mul_vector(self,v2):
        '''
        multiplies two vectors elementwise together
        v1.mul_vector(v2)
        '''
        try:
            if type(v2) != list:
                return Vector(self.x*v2.x,self.y*v2.y,self.z*v2.z)
            else:
                return Vector(self.x*v2[0],self.y*v2[1],self.z*v2[2])
            
        except IndexError as e:
            print("Vector lengths do not match or wrong input type")
    
    def div_vector(self,v2):
        '''
        divides two vectors elementwise
        v1.div_vector(v2)
        '''
        try:
            if type(v2) != list:
                return Vector(self.x/v2.x,self.y/v2.y,self.z/v2.z)
            else:
                return Vector(self.x/v2[0],self.y/v2[1],self.z/v2[2])
            
        except IndexError as e:
            print("Vector lengths do not match or wrong input type")
        except ZeroDivisionError as e:
                print("Cannot divide by 0")
            
    def add_scalar(self,c):
        '''
        adds a scalar constant to the vector
        v1.add_scalar(c)
        '''
        assert (type(c) == float or type(c) == int) , print("Incorrect input type: c is not a scalar float or int") 
        return Vector(self.x + c, self.y+c,self.z+c)
            
    def sub_scalar(self,c):
        '''
        subtracts a scalar constant from the vector
        v1.sub_scalar(c)
        '''
        assert (type(c) == float or type(c) == int) , print("Incorrect input type: c is not a scalar float or int") 
        return Vector(self.x - c, self.y - c,self.z - c)

    def mul_scalar(self,c):
        '''
        multiplies a scalar constant to the vector
        v1.mul_scalar(c)
        '''
        assert (type(c) == float or type(c) == int) , print("Incorrect input type: c is not a scalar float or int") 
        return Vector(self.x * c, self.y * c,self.z * c)
    
    def div_scalar(self,c):
        '''
        divides a scalar constant from the vector
        v1.div_scalar(c)
        '''
        assert (type(c) == float or type(c) == int) , print("Incorrect input type: c is not a scalar float or int") 
        try:
            return Vector(self.x / c, self.y / c, self.z / c)
        except ZeroDivisionError as e:
                print("Cannot divide by 0")
    
    
    #operator overloading
    
    
    def __add__(self,other):
        if type(other) == int or type(other) == float:
            return Vector(self.x + other, self.y+other,self.z+other)
        
        else:
            try:
                if type(other) != list:
                    return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
                elif type(other)==list:
                    return Vector(self.x+other[0],self.y+other[1],self.z+other[2])
                else:
                    print("Incorrect datatype")

            except IndexError as e:
                print("Vector lengths do not match")

        
            
    def __sub__(self,other):
        if type(other) == int or type(other) == float:
            return Vector(self.x - other, self.y-other,self.z-other)
        
        else:
            try:
                if type(other) != list:
                    return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
                elif type(other) == list:
                    return Vector(self.x-other[0],self.y-other[1],self.z-other[2])
                else:
                    print("Incorrect datatype")

            except IndexError as e:
                print("Vector lengths do not match")

        
            
    def __mul__(self,other):
        if type(other) == int or type(other) == float:
            return Vector(self.x * other, self.y*other,self.z*other)
        
        else:
            try:
                if type(other)!= list:
                    return Vector(self.x*other.x,self.y*other.y,self.z*other.z)
                elif type(other) == list:
                    return Vector(self.x*other[0],self.y*other[1],self.z*other[2])
                else:
                    print("Incorrect datatype")

            except IndexError as e:
                print("Vector lengths do not match")

        
            
    def __rmul__(self,other):
        return self.__mul__(other)
            
    def __truediv__(self,other):
        if type(other) == int or type(other) == float:
            try: 
                return Vector(self.x / other, self.y/other,self.z/other)
            except ZeroDivisionError as e:
                print("Cannot divide by 0")
        
        else:
            try:
                if type(other) != list:
                    return Vector(self.x/other.x,self.y/other.y,self.z/other.z)
                elif type(other) == list:
                    return Vector(self.x/other[0],self.y/other[1],self.z/other[2])
                else:
                    print("Incorrect datatype")

            except IndexError as e:
                print("Vector lengths do not match")
            except ZeroDivisionError as e:
                print("Cannot divide by 0")

        
    