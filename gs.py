import cv2
import numpy as np

videoFile = "a3.mp4"
video = cv2.VideoCapture(videoFile)
image = cv2.imread("bg2.jpg")




''' ***** ***** ***** ***** ***** *****
Video with Image Background -- Start
***** ***** ***** ***** ***** ***** '''
def write_vdo_with_image(video, image):

    def nothing():
        pass
        
    framespersecond = float(video.get(cv2.CAP_PROP_FPS))
    res = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("test.mp4", fourcc, framespersecond, res)
    
    done = False
    while not done:
        ret, frame = video.read()
        
        if not ret:
            done = True
            continue
            
        
        frame = cv2.resize(frame, (1920, 1080))
        image = cv2.resize(image, (1920, 1080))
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        l_green = np.array([29, 64, 90])
        u_green = np.array([108, 216, 255])
        
        mask = cv2.inRange(hsv, l_green, u_green)
        res = cv2.bitwise_and(frame, frame, mask = mask)
        
        f = frame - res
        green_screen = np.where(f==0, image, f)
        
        out.write(green_screen)
        
    video.release()
    out.release()
''' ***** ***** ***** ***** ***** *****
Video with Image Background -- End
***** ***** ***** ***** ***** ***** '''


write_vdo_with_image(video, image)