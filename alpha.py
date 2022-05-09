import cv2
import moviepy.editor as mpe



lowerThird = "video/lt2.mov"
videoFile = "video/high-winds-trouble-fire-fighters.mp4"
outputFile = "alpha.mp4"




''' ***** ***** ***** ***** ***** ***** *****
Write VDO with Alpha Lower Third - Start 
***** ***** ***** ***** ***** ***** ***** '''
def vdo_with_alpha(lowerThird, videoFile, outputFile):
    tmpVid = cv2.VideoCapture(videoFile)
    framespersecond = float(tmpVid.get(cv2.CAP_PROP_FPS))
    
    video_clip = mpe.VideoFileClip(videoFile, target_resolution=(1080, 1920))
    
    overlay_clip = mpe.VideoFileClip(lowerThird, has_mask=True, target_resolution=(1080, 1920))
    
    final_video = mpe.CompositeVideoClip([video_clip, overlay_clip])
    
    final_video.write_videofile(
        outputFile,
        fps=framespersecond,
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
        threads=6
    )

''' ***** ***** ***** ***** ***** ***** *****
Write VDO with Alpha Lower Third - End
***** ***** ***** ***** ***** ***** ***** '''



vdo_with_alpha(lowerThird, videoFile, outputFile)