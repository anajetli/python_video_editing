import os
import cv2
import moviepy.editor as mpe
import matplotlib.pyplot as plt
import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import PILasOPENCV as ImageFont


''' ***** ***** ***** ***** ***** ***** *****
Lower Third -- Begin
***** ***** ***** ***** ***** ***** ***** '''
def lower_third():

    text = "This is lower third text"
    cap = cv2.VideoCapture("nature1.mp4")
    
    framespersecond = float(cap.get(cv2.CAP_PROP_FPS))
    res = (1920, 1080)
    
    scale = 70
    font = ImageFont.truetype("halcyon-medium.ttf", scale)
    color = (0, 0, 0)
    thickness = 2
    margin = 2
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("lt.mp4", fourcc, framespersecond, res)
    
    done = False
    while not done:
        ret, frame = cap.read()
        
        if not ret:
            dont = True
            continue;
            
        im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(im)
        draw.text((370, 952), text, font=font, fill=(244, 172, 58))
        mask = ImageFont.getmask(text, font)
        frame = im.getim()

        out.write(frame)
        
    cap.release()
    out.release()
    
''' ***** ***** ***** ***** ***** ***** *****
Lower Third -- End
***** ***** ***** ***** ***** ***** ***** '''



lower_third()