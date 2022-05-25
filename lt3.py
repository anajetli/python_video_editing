import os
import cv2
import sys
import numpy as np
import moviepy.editor as mpe
import matplotlib.pyplot as plt
import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import PILasOPENCV as ImageFont


def add_transparent_image(background, foreground, x_offset=None, y_offset=None):
    bg_h, bg_w, bg_channels = background.shape
    fg_h, fg_w, fg_channels = foreground.shape

    assert bg_channels == 3, f'background image should have exactly 3 channels (RGB). found:{bg_channels}'
    assert fg_channels == 4, f'foreground image should have exactly 4 channels (RGBA). found:{fg_channels}'

    # center by default
    if x_offset is None: x_offset = (bg_w - fg_w) // 2
    if y_offset is None: y_offset = (bg_h - fg_h) // 2

    w = min(fg_w, bg_w, fg_w + x_offset, bg_w - x_offset)
    h = min(fg_h, bg_h, fg_h + y_offset, bg_h - y_offset)

    if w < 1 or h < 1: return

    # clip foreground and background images to the overlapping regions
    bg_x = max(0, x_offset)
    bg_y = max(0, y_offset)
    fg_x = max(0, x_offset * -1)
    fg_y = max(0, y_offset * -1)
    foreground = foreground[fg_y:fg_y + h, fg_x:fg_x + w]
    background_subsection = background[bg_y:bg_y + h, bg_x:bg_x + w]

    # separate alpha and color channels from the foreground image
    foreground_colors = foreground[:, :, :3]
    alpha_channel = foreground[:, :, 3] / 255  # 0-255 => 0.0-1.0

    # construct an alpha_mask that matches the image shape
    alpha_mask = np.dstack((alpha_channel, alpha_channel, alpha_channel))

    # combine the background with the overlay image weighted by alpha
    composite = background_subsection * (1 - alpha_mask) + foreground_colors * alpha_mask

    # overwrite the section of the background image that has been updated
    background[bg_y:bg_y + h, bg_x:bg_x + w] = composite


''' ***** ***** ***** ***** ***** ***** *****
Generate Video with Image Background -- Start
***** ***** ***** ***** ***** ***** ***** '''
def lower_third():
    video = cv2.VideoCapture("output.mp4")
    image = cv2.imread("bg3.jpg")

    def nothing():
        pass


    # videowriter
    framespersecond= float(video.get(cv2.CAP_PROP_FPS))
    res = (1920, 1080);
    fourcc = cv2.VideoWriter_fourcc(*'mp4v');
    out = cv2.VideoWriter("lt3333.mp4",fourcc, framespersecond, res);
    

    scale = 26
    overlay = cv2.imread("lt1_blank.png", cv2.IMREAD_UNCHANGED)
    font = ImageFont.truetype("AvenirLTStd-Black.ttf", scale)
    margin = 2
    thickness = 2
    text = "This is lower third text"
    color = (0, 0, 0)
    
    done = False;

    while not done:
     
        ret, frame = video.read()
        
        if not ret:
            done = True;
            continue;

        frame = cv2.resize(frame, (1920, 1080))
        image = cv2.resize(image, (1920, 1080))
        
        add_transparent_image(frame, overlay, 0, -20)
        
        im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(im)
        draw.text((370, 952), text, font=font, fill=(244, 172, 58))
        mask = ImageFont.getmask(text, font)
        frame = im.getim()
        
        # save
        out.write(frame)
        
    video.release()
    out.release()
''' ***** ***** ***** ***** ***** ***** *****
Generate Video with Image Background -- End
***** ***** ***** ***** ***** ***** ***** '''



lower_third()