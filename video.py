import cv2 as cv
video=cv.VideoCapture(0)
while(video.isOpened()):
    ret,frame=video.read()#ret framein boş olup olmadığını kontrol
    print(ret)
    if ret:
        cv.imshow("video",frame)
        if cv.waitKey(33)==ord('q'):
            break