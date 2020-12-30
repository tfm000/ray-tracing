class Image:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]
    
    def set_pixel(self,x,y,col):
        self.pixels[y][x] = col 
    
    def write_ppm(self,img_file):
        def to_byte(c):
            return round( max(min(c*255,255),0) )
        
        img_file.write("P3 {} {}\n255\n".format(self.width,self.height)) #our image header
        for row in self.pixels:
            for col in row:
                img_file.write("{} {} {} ".format(to_byte(col.x),to_byte(col.y),to_byte(col.z)))
            img_file.write("\n")