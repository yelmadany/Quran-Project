#Libraries
import os
from pydub import AudioSegment

#Variables
numOfCRs = input() #Number of Continous Recitations

#Data Setup
folder_path = 'Data'
file_list = os.listdir(folder_path)
quranDict = {str(i).zfill(3): [] for i in range(1, 115)}
for file in file_list:
    chapter = file[0:3]
    quranDict[chapter].append(file)

#commenr