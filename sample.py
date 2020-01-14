# Import pygame into our program
import pygame
import pygame.freetype
import time

from scene import *
from object3d import *
from mesh import *
from material import *
from color import *

class Key:
    def __init__(self):
        self.isPressed = False

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
    obj1 = Object3d("NewForm")
    obj1.scale = vector3(1, 1, 1)
    obj1.position = vector3(0, 0.5, 0)
    obj1.mesh = Mesh.create_form((1, 1, 1))
    obj1.material = Material(color(1,0,0,1), "TestMaterial1")
    scene.add_object(obj1)

    # Create a second object, and add it as a child of the first object
    # When the first object rotates, this one will also mimic the transform
    obj2 = Object3d("ChildObject")
    obj2.position += vector3(0, -0.75, 0)
    obj2.mesh = Mesh.create_form((0.5, -0.5, 0.5))
    obj2.material = Material(color(0,1,0,1), "TestMaterial2")
    obj1.add_child(obj2)

    #velocidade da rotacao
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
                if (event.key == pygame.K_LEFT):   
                    leftKey = True
                elif (event.key == pygame.K_RIGHT):
                    rightKey = True
                elif (event.key == pygame.K_UP):
                    upKey = True
                elif (event.key == pygame.K_DOWN):
                    downKey = True
                elif (event.key == pygame.K_PAGEUP):
                    pageUpKey = True
                elif (event.key == pygame.K_PAGEDOWN):
                    pageDownKey = True
                elif (event.key == pygame.K_a):   
                    aKey = True
                elif (event.key == pygame.K_d):
                    dKey = True
                elif (event.key == pygame.K_w):
                    wKey = True
                elif (event.key == pygame.K_s):
                    sKey = True
                elif (event.key == pygame.K_q):
                    qKey = True
                elif (event.key == pygame.K_e):
                    eKey = True
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT):
                    leftKey = False
                elif (event.key == pygame.K_RIGHT):
                    rightKey = False
                elif (event.key == pygame.K_UP):
                    upKey = False
                elif (event.key == pygame.K_DOWN):
                    downKey = False
                elif (event.key == pygame.K_PAGEUP):
                    pageUpKey = False
                elif (event.key == pygame.K_PAGEDOWN):
                    pageDownKey = False
                elif (event.key == pygame.K_a):   
                    aKey = False
                elif (event.key == pygame.K_d):
                    dKey = False
                elif (event.key == pygame.K_w):
                    wKey = False
                elif (event.key == pygame.K_s):
                    sKey = False
                elif (event.key == pygame.K_q):
                    qKey = False
                elif (event.key == pygame.K_e):
                    eKey = False

        if leftKey:
            axis = vector3(0,-1,0)  #left
        elif rightKey:
            axis = vector3(0,1,0)   #right
        elif upKey:
            axis = vector3(-1,0,0)  #up
        elif downKey:
            axis = vector3(1,0,0)   #down
        elif pageUpKey:
            axis = vector3(0,0,-1)  #zup
        elif pageDownKey:
            axis = vector3(0,0,1)   #zdown
        else:
            axis = vector3(0,0,0)   #else stop rotation
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
            obj1.position += vector3(0,0,0.01)  #front
        if eKey:
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
