import cv2
# import imutils

img = cv2.imread('img.png')
# resized = imutils.resize(img, width=50)
# cv2.imwrite('resized.png', resized)

# gaussimg = cv2.GaussianBlur(img,(21,21),0)
# cv2.imwrite('resized.png', gaussimg)


grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
tresholdimg = cv2.threshold(grayimg, 80, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('thresholdimg.png', tresholdimg)


