import cv2
import time
import math

p1=530
p2=300
xs=[]
ys=[]
video = cv2.VideoCapture("bb3.mp4")
tracker=cv2.TrackerMIL_create()
ret,img=video.read()
box=cv2.selectROI("tracking",img,False)
tracker.init(img,box)

def drawbox(frame,box):
    x,y,w,h=int(box[0]),int(box[1]),int(box[2]),int(box[3])
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3,1)
    cv2.putText(frame,"Tracking",(75,90),cv2.FONT_HERSHEY_TRIPLEX,0.9,(0,0,255),3)

def goal(img,box):
     x,y,w,h=int(box[0]),int(box[1]),int(box[2]),int(box[3])
     c1=x+int(w/2)
     c2=y+int(h/2)
     cv2.circle(img,(c1,c2),2,(0,0,255),5)
     cv2.circle(img,(int(p1),int(p2)),2,(0,0,255),3)
     distance=math.sqrt(((c1-p1)**2)+(c2-p2)**2)

     if distance<=20:
        cv2.putText(img,"Goal",(300,90),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(0,255,0),2)
     xs.append(c1)
     ys.append(c2)
     for i in range (len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]),2,(255,40,6),4)

while True:
    check,img = video.read()  
    success,ball=tracker.update(img) 
    if success:
        drawbox(img,ball)
    else:
        cv2.putText(img,"LOST!!",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
    goal(img,ball)
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



