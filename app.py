import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

# Constants
BOUNDRYINC = 5
WINDOWSIZEX = 640
WINDOWSIZEY = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Load model
MODEL = load_model("mnist_model.h5")

LABELS = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}

# Initialize pygame
pygame.init()
FONT = pygame.font.Font("freesansbold.ttf", 18)
DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))
pygame.display.set_caption("MNIST Digit Recognition")
DISPLAYSURF.fill(BLACK)

iswriting = False
number_xcord = []
number_ycord = []

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Start writing
        if event.type == MOUSEBUTTONDOWN:
            iswriting = True

        # Stop writing and predict
        if event.type == MOUSEBUTTONUP:
            iswriting = False
            if number_xcord and number_ycord:
                number_xcord = sorted(number_xcord)
                number_ycord = sorted(number_ycord)

                rect_min_x = max(number_xcord[0] - BOUNDRYINC, 0)
                rect_max_x = min(number_xcord[-1] + BOUNDRYINC, WINDOWSIZEX)
                rect_min_y = max(number_ycord[0] - BOUNDRYINC, 0)
                rect_max_y = min(number_ycord[-1] + BOUNDRYINC, WINDOWSIZEY)

                # Reset for next digit
                number_xcord = []
                number_ycord = []

                # Extract image
                image_array = np.array(pygame.PixelArray(DISPLAYSURF))[rect_min_x:rect_max_x, rect_min_y:rect_max_y].T.astype(np.float32)

                if image_array.shape[0] > 0 and image_array.shape[1] > 0:
                    # Preprocess
                    image = cv2.resize(image_array, (28, 28))
                    image = np.pad(image, ((10, 10), (10, 10)), 'constant', constant_values=0)
                    image = cv2.resize(image, (28, 28))
                    image = image / 255.0

                    # Predict
                    prediction = MODEL.predict(image.reshape(1, 28, 28, 1))
                    label = LABELS[np.argmax(prediction)]

                    # Display result
                    text_surface = FONT.render(label, True, RED, WHITE)
                    DISPLAYSURF.blit(text_surface, (rect_min_x, rect_min_y - 20))

        # Record mouse motion while writing
        if event.type == MOUSEMOTION and iswriting:
            xcord, ycord = event.pos
            pygame.draw.circle(DISPLAYSURF, WHITE, (xcord, ycord), 4, 0)
            number_xcord.append(xcord)
            number_ycord.append(ycord)

        # Clear screen
        if event.type == KEYDOWN:
            if event.unicode == "n":
                DISPLAYSURF.fill(BLACK)

    pygame.display.update()

             



                    