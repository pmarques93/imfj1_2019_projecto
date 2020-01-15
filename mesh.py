import pygame
from vector3 import *

class Mesh:
    def __init__(self, name = "UnknownMesh"):
        self.name = name
        self.polygons = []

    def offset(self, v):
        new_polys = []
        for poly in self.polygons:
            new_poly = []
            for p in poly:
                new_poly.append(p + v)
            new_polys.append(new_poly)

        self.polygons = new_polys

    def render(self, screen, matrix, material):
        c = material.color.tuple3()        

        for poly in self.polygons:
            tpoly = []
            for v in poly:
                vout = v.to_np4()
                vout = vout @ matrix
                
                tpoly.append( ( screen.get_width() * 0.5 + vout[0] / vout[3], screen.get_height() * 0.5 - vout[1] / vout[3]) )

            
            pygame.draw.polygon(screen, (255, 255, 255), tpoly, material.line_width)
            #pygame.draw.polygon(screen, c, tpoly, material.fill)



    @staticmethod
    def create_Pyramid(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("Pyramid")

        Mesh.create_triangle(vector3(-size[0] * 0.5, 0, 0), vector3(0, 0, size[2] * 0.5), vector3(0, size[1] * 0.5, 0), mesh)
        Mesh.create_triangle(vector3(size[0] * 0.5, 0, 0), vector3(0, 0, size[2] * 0.5), vector3(0, size[1] * 0.5, 0), mesh)
        Mesh.create_triangle(vector3(0, 0,  size[2] * 0.5), vector3(-size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)
        Mesh.create_triangle(vector3(0, 0, -size[2] * 0.5), vector3( size[0] * 0.5, 0), vector3(0, size[1] * 0.5, 0), mesh)

        return mesh

    @staticmethod
    def create_triangle(origin, axis0, axis1, mesh):
        if (mesh == None):
            mesh = Mesh("Faces")

        poly = []
        p1 = (origin - origin + axis1)
        p2 = (origin + axis0 - axis1)
        p3 = (origin - axis0 - axis1)
        p4 = (origin - axis0 - axis1)


        poly.append(p1)
        poly.append(p2)
        poly.append(p3)
        poly.append(p4)

        #v1 = p2 - p1
        #v2 = p3 - p1

        #n = cross_product(v1,v2)
    
        #cameraVec = vector3(0,0,1)

        #if dot_product(n, cameraVec) > 0:
        
        mesh.polygons.append(poly)

        return mesh
    

    @staticmethod
    def create_Pyramid_Bottom(size, mesh = None):
        if (mesh == None):
            mesh = Mesh("Pyramid")

        #quadrado
        Mesh.create_bottom(vector3(0, -size[1] * 0.5, 0), vector3(-size[0] * 0.5, 0), vector3(0, 0, size[2] * 0.5), mesh)


        return mesh

    @staticmethod
    def create_bottom(origin, axis0, axis1, mesh):
        if (mesh == None):
            mesh = Mesh("PyramidBottom")

        poly = []
        poly.append(origin + axis0 + axis1)
        poly.append(origin + axis0 - axis1)
        poly.append(origin - axis0 - axis1)
        poly.append(origin - axis0 + axis1)

        mesh.polygons.append(poly)

        mesh.polygons.append(poly)

        return mesh
