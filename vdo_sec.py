import moviepy.editor as mpe


bg_video_file = "video/news-tv-studio-set-42.mp4"
sec_bg_video_file = "video/wind-turbines-in-the-english.mp4"

output_file = "bg_sec.mp4"
bgwidth = 546 #673 #646
bgheight = 308 #348 #338
bgtop = 126 #280 #310
bgleft = 1142 #1050 #1058



''' ***** ***** ***** ***** ***** ***** *****
Video background with Secondary Video - Start
***** ***** ***** ***** ***** ***** ***** '''
def vdo_with_bgvdo(bg_video_file, sec_bg_video_file, output_file, bgwidth, bgheight, bgtop, bgleft):
    bg_video = mpe.VideoFileClip(bg_video_file, audio=False)
    w,h = moviesize = bg_video.size
    
    sec_bg_video = (mpe.VideoFileClip(sec_bg_video_file, audio=False).
                    resize( (bgwidth, bgheight)).
                    margin(0, color=(255, 255, 255)).
                    margin(top = bgtop, left = bgleft, opacity = 0).
                    set_pos(('left', 'top')) )
                    
    final = mpe.CompositeVideoClip([bg_video, sec_bg_video])
    final.write_videofile(output_file)
''' ***** ***** ***** ***** ***** ***** *****
Video background with Secondary Video - End
***** ***** ***** ***** ***** ***** ***** '''



vdo_with_bgvdo(bg_video_file, sec_bg_video_file, output_file, bgwidth, bgheight, bgtop, bgleft)