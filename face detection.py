import cv2
#load the cascade
face_cascade = cv2.CascadeClassifier(r'C:\Users\icon\PycharmProjects\hadwritten digital recongnition\haarcascade_frontalface_default.xml')
#read the input image
img=cv2.imread('photo.jpg')
#convert into grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Detect Faces
faces=face_cascade.detectMultiScale(gray,1.1,4)
#draw rectangle around each faces
for (x,y,w,h)in faces:
    cv2.rectangle((img,(x,y),(x+w,y+h),(255,0,0),2))
#display the output
cv2.imshow('img',img)
cv2.waitkey()
