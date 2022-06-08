import cv2
import numpy as np

# Variables to change:
scaling = 0.5
imagePath = 'sample_image7.jpg'

# load in face detection model
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# detect faces in the image
temp = cv2.imread(imagePath)
img = cv2.resize(temp, None, fx = scaling, fy = scaling, interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_model.detectMultiScale(gray, 1.4, 4)

# make cutouts for the faces
mask = np.full(
    (img.shape[0], img.shape[1], 1), 0, dtype=np.uint8)
face_areas = []
for (x, y, w, h) in faces:
    face_areas.append(([x, y, w, h],img[y:y+h,x:x+w]))
    center = (x + w // 2, y + h // 2)
    diameter = np.sqrt(pow(h,2) + pow(w,2))
    radius = (diameter.astype(int))//2

    # radius = max(h, w) // 2
    cv2.circle(mask, center, radius, (255), -1)

# make the faces mask
# kernel = np.ones((3, 3), np.float32) / 9
# mask = cv2.filter2D(mask, -1, kernel)
# mask = cv2.GaussianBlur(mask, (0,0), 5) 

# deep fry the faces
gaussian = cv2.GaussianBlur(img, (0,0), 100,)
temp = cv2.addWeighted(img, 2.75, gaussian, -2, 0)
temp2 = cv2.addWeighted(temp, 2.75, gaussian, -2, 0)
distorted = cv2.medianBlur(src=temp2, ksize=45)

# mask and add the images together
mask_inverted = cv2.bitwise_not(mask)
background = cv2.bitwise_and(img, img, mask=mask_inverted)
foreground = cv2.bitwise_and(distorted, distorted, mask=mask)
composite = (foreground + background)

cv2.imshow('image', composite)
cv2.waitKey(0)
cv2.destroyAllWindows()