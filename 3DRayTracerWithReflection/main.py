#!/usr/bin/env python
""" Puray - a Pure Python Raytracer by Tyler Mitchell, 2020"""
import argparse
from scene import Scene
from engine import RenderEngine
import importlib # allows you to import
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene",help="Path to rendered image (without .py extension)")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)
    scene = Scene(mod.CAMERA,mod.OBJECTS,mod.LIGHTS,mod.WIDTH,mod.HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)
    
    os.chdir(os.path.dirname(os.path.abspath(mod.__file__))) #renders the image in the same location as the main file
    with open(mod.RENDERED_IMG,"w") as img_file:
        image.write_ppm(img_file)

if __name__ == "__main__":
    main()