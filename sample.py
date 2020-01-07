# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

# Define a main function, just to keep things nice and tidy
def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position -= vector3(0,0,2)

    # Create a cube and place it in a scene, at position (0,0,0)
    # This cube has 1 unit of side, and is red
    obj1 = Object3d("TestObject")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, -1, 0)
    obj1.mesh = Mesh.create_cube((1, 1, 1))
    obj1.material = Material(color(1,0,0,1), "TestMaterial1")
    scene.add_object(obj1)

    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, 0.75, 0)
    obj2.mesh = Mesh.create_cube((0.5, 0.5, 0.5))
    obj2.material = Material(color(0,1,0,1), "TestMaterial2")
    obj1.add_child(obj2)

    # Timer
    delta_time = 0
    prev_time = time.time()

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return


        #gets key pressed
        rotationKey = pygame.key.get_pressed()
        translationKey = pygame.key.get_pressed()
        
        # if rotation key is pressed
        if (rotationKey):
            angle = 50
            if rotationKey[pygame.K_LEFT]:
                axis = vector3(0,-1,0)  #left
            elif rotationKey[pygame.K_RIGHT]:
                axis = vector3(0,1,0)   #right
            elif rotationKey[pygame.K_UP]:
                axis = vector3(-1,0,0)  #up
            elif rotationKey[pygame.K_DOWN]:
                axis = vector3(1,0,0)   #down
            elif rotationKey[pygame.K_PAGEUP]:
                axis = vector3(0,0,-1)  #zup
            elif rotationKey[pygame.K_PAGEDOWN]:
                axis = vector3(0,0,1)   #zdown
            else:
                angle = 0
                axis = vector3(0,0,0)   #else stop rotation

        if angle > 0:
            axis.normalize()    #when key gets pressed (angle > 0) = axis.normalize()

        # if translationKey is pressed
        if (translationKey):
            if translationKey[pygame.K_a]:
                obj1.position += vector3(-0.01,0,0) #left
            elif translationKey[pygame.K_d]:
                obj1.position += vector3(0.01,0,0)  #right
            elif translationKey[pygame.K_w]:
                obj1.position += vector3(0,0.01,0)  #up
            elif translationKey[pygame.K_s]:
                obj1.position += vector3(0,-0.01,0)  #down
            elif translationKey[pygame.K_q]:
                obj1.position += vector3(0,0,0.01)  #front
            elif translationKey[pygame.K_e]:
                obj1.position += vector3(0,0,-0.01)  #back
            

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))

        # Rotates the object, considering the time passed (not linked to frame rate)
        q = from_rotation_vector((axis * math.radians(angle) * delta_time).to_np3())
        obj1.rotation = q * obj1.rotation

        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
