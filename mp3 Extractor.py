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
dirList = []
for path,dirs,files in os.walk(currentDir):
    for file in files:
        dirList.append(str(file))
for path,dirs,files in os.walk(currentDir):
    for file in files:
        nameArr = file.split('.')
        forma =  nameArr[len(nameArr)-1]
        if forma.lower() == "mkv" or forma.lower() == "mp4" or forma.lower() == "flv":
            try:
                clip = mp.VideoFileClip(file)
                newName = ".".join(nameArr[:-1])+".mp3"
                if newName not in dirList:
                    clip.audio.write_audiofile(".".join(nameArr[:-1])+".mp3")
            except:
                print("cannot convert ",file)