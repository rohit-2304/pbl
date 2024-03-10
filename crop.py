import cv2
import numpy as n

image = cv2.imread("output.png")
print(image.shape[0])
#height, width = image.shape[:2]

# Iterate over the pixels of the image
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        # Get the pixel value at (x, y)
        pixel = (255,0,0)
        if cv2.subtract(pixel,image[x,y]) == 0:
            image = image[x: ]
            break
    else:
        continue
    break
            


cv2.imshow('Modified Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
