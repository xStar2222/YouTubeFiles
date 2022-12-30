from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("video.mp4")

videoClip.write_gif("gif.gif")
