from sphere import Sphere
from vector import Vector
from point import Point
from colour import Colour
from scene import Scene
from light import Light
from material import Material
from material import ChequeredMaterial
from engine import RenderEngine

WIDTH = 320 #2560 #= 320
HEIGHT =200 #1600 #= 200
RENDERED_IMG = "2balls.ppm"
CAMERA = Vector(0,-0.35,-1)
OBJECTS =[Sphere(Point(0,10000.5,1),10000,ChequeredMaterial(colour1 = Colour.from_hex("420500"),colour2=Colour.from_hex("#E6B87D"),ambient = 0.2,reflection=0.2)),
          #Blue ball
          Sphere(Point(0.75,-0.1,1),0.6,Material(Colour.from_hex("#0000FF"))),
          #Pink ball
          Sphere(Point(-0.75,-0.1,2.25),0.6,Material(Colour.from_hex("#803980"))) 
    
]
LIGHTS = [
    Light(Point(1.5,-0.5,-10),Colour.from_hex("#FFFFFF")),
    Light(Point(-0.5,-10.5,0),Colour.from_hex("#E6E6E6"))
]