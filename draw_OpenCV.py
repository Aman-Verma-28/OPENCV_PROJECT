import cv2
import numpy

#blank image
blank=numpy.zeros((500,500,3),dtype='uint8') #height widht color channel
cv2.imshow('blank',blank)
blank[:]=255,0,0
cv2.imshow('colored',blank)

#draw shapes - rectangle, square, circle, line 

# put text
text=cv2.putText(blank,'AMAN',(250,250),cv2.FONT_HERSHEY_COMPLEX,2.0,(0,0,255))
cv2.imshow('text',text)

#translation
# -x -->left 
# -y -->up
# +x -->right
# +y -->down

def translate(img, x, y):
    transMat = numpy.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

img=cv2.imread(r'C:\Users\verma\Desktop\Whatsapp Automation\photos\background.png')
trans=translate(img,100,-100)
cv2.imshow("translated",trans)

def rotate(img,angle,point=None):
    height,width=img.shape[:2]
    if point is None:
        point=(height//2,width//2)
    rotMat=cv2.getRotationMatrix2D(point,angle,1.0)
    dimension=(width,height)
    return cv2.warpAffine(img,rotMat,dimension)

# clockwise --> anlge -ve
# anticlockwise --> angle +ve

rotated=rotate(img,45)
cv2.imshow('rotated',rotated)

#Flipping
#Flip code  --> 1->vertically(over x axis), 0-> horizontally(over y axis), -1->both horizontally and vertically

fliped=cv2.flip(img,-1)
cv2.imshow('flipped',fliped)

cv2.waitKey(0)