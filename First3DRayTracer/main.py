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
    objects = [Sphere(Point(0,0,0),0.5,Material(Colour.from_hex("#FF0000")))]
    lights = [Light(Point(1.5,-0.5,-10.0),Colour.from_hex('#FFFFFF'))]
    scene = Scene(camera,objects,lights,WIDTH,HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    
    with open(args.imageout,"w") as img_file:
        image.write_ppm(img_file)
    
if __name__ == "__main__":
    main()