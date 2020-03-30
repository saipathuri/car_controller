import pygame
import xbox
import socket_client

from pygame.locals import *
import cv2
import numpy as np

pygame.init()

# Set the width and height of the screen [width,height]
size = [640, 480]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Controller")

#Loop until the user clicks the close button.
done = False

# Initialize the joysticks
pygame.joystick.init()

try:
    socket_client.setup()
except Exception:
    socket_client.disconnect()
    socket_client.setup()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    cap = cv2.VideoCapture('http://raspberrypi:8081')
    ret, frame = cap.read()
    screen.fill([0,0,0])
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    screen.blit(frame, (0,0))
    pygame.display.update()
    
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    xbox.process_axes(socket_client, joystick)
    pygame.display.update()

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
cv2.destroyAllWindows()
socket_client.disconnect()
pygame.quit ()