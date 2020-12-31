#!/usr/bin/env python
""" Puray - a Pure Python Raytracer by Tyler Mitchell, 2020"""

from vector import Vector
from colour import Colour
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material
import argparse

def main():
    #argparse will allow the user to specify the file location where they want the image stored
    parser = argparse.ArgumentParser()
    parser.add_argument("imageout",help = "Path to rendered image")
    args = parser.parse_args()
    
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0,0,-1)
    #objects = [Sphere(Point(0,0,0),0.5,Material(Colour.from_hex("#FF0000")))]
    objects = [Sphere(Point(0,10000.5,1),10000,Material(Colour.from_hex("#420500"))),
               Sphere(Point(0.75,-0.1,1),0.6,Material(Colour.from_hex("#0000FF"))),
               Sphere(Point(-0.75,-0.1,2.25),0.6,Material(Colour.from_hex("#803980")))]

    
    
    #objects = [Sphere(Point(0,10000.5,1),10000,Material(Colour.from_hex("#420500"))),Sphere(Point(-1,0.5,1),0.5,Material(Colour.from_hex("#FF0000"))),Sphere(Point(-1,-0.5,1),0.5,Material(Colour.from_hex("#FFFFFF"))),Sphere(Point(0,0,1),0.5,Material(Colour.from_hex("#0000FF"))),Sphere(Point(1,-0.5,1),0.5,Material(Colour.from_hex("#00FF00"))),Sphere(Point(1,0.5,1),0.5,Material(Colour.from_hex("#FF00FF")))]
    lights = [Light(Point(1.5,-0.5,-10.0),Colour.from_hex('#FFFFFF')),
              Light(Point(-0.5,-10.5,0.0),Colour.from_hex('#E6E6E6'))]
    scene = Scene(camera,objects,lights,WIDTH,HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    
    with open(args.imageout,"w") as img_file:
        image.write_ppm(img_file)
    
if __name__ == "__main__":
    main()