import os
import re
import pydub
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

############# GUI code #############
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('integrated_transducer_mp3','Select the target folder.')
dir = tkinter.filedialog.askdirectory(initialdir = iDir)

### convert procces ### 
for i in Path(dir).glob("**/*.flac"):
    i2 = str(i)
    sound = pydub.AudioSegment.from_file(i2)
    sound.export(str(i2[:-5])+'.mp3', format="mp3",bitrate="320k")
    os.remove(i2)

for i in Path(dir).glob("**/*.wav"):
    i2 = str(i)
    sound = pydub.AudioSegment.from_file(i2)
    sound.export(str(i2[:-4])+'.mp3', format="mp3",bitrate="320k")
    os.remove(i2)

for i in Path(dir).glob("**/*.mp3"):
    i2 = str(i)
    if '~' in i2 or '-' in i2 or '_' in i2:
        os.rename(i2,i2.replace('~',' ').replace('-',' ').replace('_',' '))
        os.rename(i2,i2.replace('  ',' '))
    os.rename(i2,re.sub('[0-9]*\.', '',i2,1))