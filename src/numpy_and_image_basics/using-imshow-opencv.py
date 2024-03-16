import cv2

img = cv2.imread('my_new_picture.jpg')

while True:
    cv2.imshow('Puppy',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()