import imageio
import os.path
imageio.plugins.ffmpeg.download()
import moviepy.editor as mp
import time
from tkinter.filedialog import askdirectory
currentDir = os.getcwd()
dirList = []
for path,dirs,files in os.walk(currentDir):
    for file in files:
        dirList.append(str(file))
for path,dirs,files in os.walk(currentDir):
    for file in files:
        nameArr = file.split('.')
        forma = nameArr[len(nameArr)-1]
        if forma.lower() in ['mkv','mp4','flv','webm','avi']:
            try:
                clip = mp.VideoFileClip(file)
                newName = str(file)[:-4]+".mp3"
                if newName not in dirList:
                    clip.audio.write_audiofile(newName)
            except:
                print("cannot convert", file)
time.sleep(5)