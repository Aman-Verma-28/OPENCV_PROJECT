import cv2 

img=cv2.imread(r'photos/a.jpg') #read
cv2.imshow('a',img) #show
# cv2.waitKey(0)

# resize 
resized=cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)
cv2.imshow('resized',resized)

# crop
crop=img[100:900,300:1200]
cv2.imshow('crop',crop)

# gray scale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
# cv2.waitKey(0)

#blur
blur=cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT) #kernel size has to be a positive odd integer
cv2.imshow('blur',blur)

#Blur can be done by using 4 different technique --> avergae, bilateral, median, GaussianBlur

#Edge detection

edge=cv2.Canny(blur,100,200)
cv2.imshow('edge',edge)

#Dilated --> borders become thick and dilated
dilated=cv2.dilate(edge,(5,5),iterations=3)
cv2.imshow('dilated',dilated)

cv2.waitKey(0)

#Different color codes --> LAB BGR RGB GRAYSCALE HSV 
#All of these can be interconverted by using BGR image first 




