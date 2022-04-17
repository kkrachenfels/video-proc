def add_beeps():
	import moviepy.editor as mymovie



"""
list = [(2,6), (8,13), (16, 18)]

startaudio = "start.mp3"
endaudio = "end.mp3"
outputvideo = "output.mp4"
videoclip = VideoFileClip('porygon_trim2.mp4')

start, end = list[0]
audioclip = mymovie.AudioFileClip(inputaudio)

startaudioclip = mymovie.AudioFileClip(startaudio)
endaudioclip = mymovie.AudioFileClip(endaudio)

finalclip = videoclip.set_audio(CompositeAudioClip([videoclip.audio, startaudioclip.set_start(start), endaudioclip.set_start(end)]))

for x in range(1,len(list)):
  videoclip = VideoFileClip('output.mp4')
  start, end = list[x]
  finalclip = finalclip.set_audio(CompositeAudioClip([finalclip.audio, startaudioclip.set_start(start), endaudioclip.set_start(end)]))
finalclip.write_videofile(outputvideo, fps=30)
"""