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

    # Create a pyramid and place it in a scene, at position (0, 0.5, 0)
    # This pyramid has 1 unit of side, and is white
    obj1 = Object3d("Pyramid")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, 0.5, 0)
    obj1.mesh = Mesh.create_Pyramid((1, 1, 1))
    obj1.material = Material(color(1,1,1,1), "TestMaterial1")
    scene.add_object(obj1)

    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, -0.75, 0)
    obj2.mesh = Mesh.create_Pyramid((0.5, -0.5, 0.5))
    obj2.material = Material(color(0,1,1,1), "TestMaterial1")
    obj1.add_child(obj2)

    #rotação
    angle = 50

    # Timer
    delta_time = 0
    prev_time = time.time()

    # keys
    leftKey = False
    rightKey = False
    upKey = False
    downKey = False
    pageUpKey = False
    pageDownKey = False
    aKey = False
    dKey = False
    wKey = False
    sKey = False
    qKey = False
    eKey = False

    # keys list
    keys = [
        leftKey, rightKey, upKey, downKey, pageUpKey, pageDownKey,
        aKey, dKey, wKey, sKey, qKey, eKey
    ]
    
    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return
                if (event.key == pygame.K_LEFT):   
                    leftKey = True
                if (event.key == pygame.K_RIGHT):
                    rightKey = True
                if (event.key == pygame.K_UP):
                    upKey = True
                if (event.key == pygame.K_DOWN):
                    downKey = True
                if (event.key == pygame.K_PAGEUP):
                    pageUpKey = True
                if (event.key == pygame.K_PAGEDOWN):
                    pageDownKey = True
                if (event.key == pygame.K_a):   
                    aKey = True
                if (event.key == pygame.K_d):
                    dKey = True
                if (event.key == pygame.K_w):
                    wKey = True
                if (event.key == pygame.K_s):
                    sKey = True
                if (event.key == pygame.K_q):
                    qKey = True
                if (event.key == pygame.K_e):
                    eKey = True

            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT):
                    leftKey = False
                if (event.key == pygame.K_RIGHT):
                    rightKey = False
                if (event.key == pygame.K_UP):
                    upKey = False
                if (event.key == pygame.K_DOWN):
                    downKey = False
                if (event.key == pygame.K_PAGEUP):
                    pageUpKey = False
                if (event.key == pygame.K_PAGEDOWN):
                    pageDownKey = False
                if (event.key == pygame.K_a):   
                    aKey = False
                if (event.key == pygame.K_d):
                    dKey = False
                if (event.key == pygame.K_w):
                    wKey = False
                if (event.key == pygame.K_s):
                    sKey = False
                if (event.key == pygame.K_q):
                    qKey = False
                if (event.key == pygame.K_e):
                    eKey = False

        axis = vector3(0,0,0) #stop rotation

        if leftKey:
            axis += vector3(0,-1,0)  #left
        if rightKey:
            axis += vector3(0,1,0)   #right
        if upKey:
            axis += vector3(-1,0,0)  #up
        if downKey:
            axis += vector3(1,0,0)   #down
        if pageUpKey:
            axis += vector3(0,0,-1)  #zup
        if pageDownKey:
            axis += vector3(0,0,1)   #zdown

        for key in keys:
            if key:
                axis.normalize()    #when key gets pressed (angle > 0) = axis.normalize()

        if aKey:
            obj1.position += vector3(-0.01,0,0) #left
        if dKey:
            obj1.position += vector3(0.01,0,0)  #right
        if wKey:
            obj1.position += vector3(0,0.01,0)  #up
        if sKey:
            obj1.position += vector3(0,-0.01,0)  #down
        if qKey:
            obj1.position += vector3(0,0,0.01)  #back
        if eKey:
            obj1.position += vector3(0,0,-0.01)  #front


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
