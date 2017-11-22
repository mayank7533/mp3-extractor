import imageio
import os.path
imageio.plugins.ffmpeg.download()
import moviepy.editor as mp


def print_it(x, dir_name, files):
    print(dir_name)
    print(files)
'''    
clip = mp.VideoFileClip("myvideo.mp4").subclip(0,20)
clip.audio.write_audiofile("theaudio.mp3")
'''
currentDir = os.getcwd()
for path,dirs,files in os.walk(currentDir):
    for file in files:
        nameArr = file.split('.')
        forma =  nameArr[len(nameArr)-1]
        if forma.lower() == "mkv" or forma.lower() == "mp4" or forma.lower() == "flv":
            clip = mp.VideoFileClip(file)
            clip.audio.write_audiofile(nameArr[0]+".mp3")
