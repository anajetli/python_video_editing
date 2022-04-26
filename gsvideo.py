import cv2
import numpy as np



videoFile = "video/a4.mp4"
videoBGFile = "video/nature1.mp4"
video = cv2.VideoCapture(videoFile)
videoBG = cv2.VideoCapture(videoBGFile)



''' ***** ***** ***** ***** ***** *****
Video with Video Background -- Start
***** ***** ***** ***** ***** ***** '''
def vdo_with_vdo_bg(videoBG, video):

    framespersecond = float(video.get(cv2.CAP_PROP_FPS))
    res = (1920, 1080)
    
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("test2.mp4", fourcc, framespersecond, res)
    
    done = False
    while not done:
    
        ret, frame = video.read()
        ret2, frame2 = videoBG.read()
        
        if not ret:
            done = True
            continue
            
        if not ret2:
            videoBG.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret2, frame2 = videoBG.read()
            
        frame = cv2.resize(frame, (1920, 1080))
        frame2 = cv2.resize(frame2, (1920, 1080))
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #l_green = np.array([29, 64, 90])
        #u_green = np.array([108, 216, 255])
        
        l_green = np.array([39, 68, 68])
        u_green = np.array([96, 255, 255])
        
        mask = cv2.inRange(hsv, l_green, u_green)
        res = cv2.bitwise_and(frame, frame, mask = mask)
        f = frame - res
        gs = np.where(f==0, frame2, f)
        
        out.write(gs)
        
    video.release()
    out.release()
''' ***** ***** ***** ***** ***** *****
Video with Video Background -- End
***** ***** ***** ***** ***** ***** '''



vdo_with_vdo_bg(videoBG, video)