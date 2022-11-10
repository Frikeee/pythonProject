import numpy as np
from scipy.fft import rfft
import scipy.io.wavfile as wf
import math
import wave
import matplotlib.pyplot as plt
import librosa
import librosa.display
import tkinter as tk
from tkinter import *
import re

mainWindow = Tk()

mainWindow['bg'] = '#AFEEEE'
mainWindow.title('Доверительная программа')
mainWindow.geometry('300x300')
mainWindow.resizable(width=False, height=False)

file = 'Чириков_ZT-333_208_35_2022_08_22.wav'
y, sr = librosa.load(file)
y = abs(y)
S = np.abs(librosa.stft(y))
fileLoad = False
finalyMass = []
DecibelMIN = 0
def openPowerSpec():
    fig, ax = plt.subplots()
    img = librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max, top_db=None), y_axis='log', x_axis='time', ax=ax)
    ax.set_title('Power spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    plt.show()

def openFile():
    global fileLoad, finalyMass, DecibelMIN
    fileLoad = False
    finalyMass = []
    DecibelMIN = 0
    foldername = tk.filedialog.askdirectory()
    print(foldername)

def is_valid(newval):
    re.match("^\d{0,1}\.{0,1}\d{0,2}$", newval) is not None


def audioSpec():
    fig, ax = plt.subplots(nrows=1, sharex=True, sharey=True)
    librosa.display.waveshow(y, sr=sr, ax=ax)
    ax.set(title='Monophonic')
    ax.label_outer()
    plt.show()
def probabFunc():
    global fileLoad, DecibelMIN, finalyMass
    userProb = (float)(userProbTF.get())
    if fileLoad == False:
        Db = librosa.amplitude_to_db(S, ref=np.max, top_db=None)
        print(np.max(Db), " ", np.min(Db))
        print(np.shape(Db))
        print(len(Db))
        clearDB = []
        summar = 0
        for i in range(len(Db[1])):
            for z in range(len(Db)):
                summar += Db[z][i] / 1025
            print(summar)
            clearDB.append(round(abs(summar)))
            summar = 0
        D = clearDB
        D.sort()
        DecibelMAX = np.max(D)
        DecibelMIN = np.min(D)
        renges = 0
        Gistoram = []
        i = 0
        iterat = 0
        while renges <= DecibelMAX - DecibelMIN:
            for i in D:
                if DecibelMIN + renges == i:
                    iterat += 1
            Gistoram.append(iterat)
            iterat = 0
            renges += 1
        relProb = []
        for i in Gistoram:
            relProb.append(float("{0:.5f}".format(i / sum(Gistoram))))
        probab = 0
        for i in relProb:
            finalyMass.append(probab + i)
            probab = probab + i
        fileLoad = True
    for index in range(len(finalyMass)):
        if finalyMass[index] > userProb:
            textProb["text"] = "Доверительная громкость: " + str(index + DecibelMIN) + " dB"
            print(str(index + DecibelMIN) + " dB")
            break
    else:
        print("Такой доверительности не существует")



check = (mainWindow.register(is_valid), "%P")

canvas = Canvas(mainWindow, height=300, width= 300)
canvas.pack()
frame = Frame(mainWindow, bg='#ADD8E6')
frame.place(relx=0.025, rely=0.025, relheight=0.95, relwidth=0.95)
btn = Button(frame, text='Open File', command=openFile)
btn.pack(anchor="nw", padx=5, pady=5)
textProb = Label(frame, text='Введите доверительную вероятность:', bg='#ADD8E6')
textProb.pack(anchor="w", padx=5)
userProbTF = Entry(frame, validatecommand=check, validate="key")
userProbTF.pack(anchor="w", padx=5)
textProb = Label(frame, bg='#ADD8E6')
textProb.pack(anchor="w", padx=5)
btn = Button(frame, text='Спектр аудиофайла', command=audioSpec)
btn.pack(anchor="w", padx=5, pady=15)
btn = Button(frame, text='Спектрограмма аудиофайла', command=openPowerSpec)
btn.pack(anchor="w", padx=5)
btn = Button(frame, text='Какой-то грапфик')
btn.pack(anchor="w", padx=5, pady=15)
btn = Button(frame, text='Рассчитать', command=probabFunc)
btn.pack(anchor="se", padx=5, pady=15)



mainWindow.mainloop()


# Db = librosa.amplitude_to_db(S, ref=np.max, top_db = None)
# print(np.max(Db), " ", np.min(Db))
# print(np.shape(Db))
# print(len(Db))
# clearDB = []
# summar = 0
# for i in range(len(Db[1])):
#     for z in range(len(Db)):
#         summar += Db[z][i] / 1025
#         # if round(srdb) < round(abs(Db[i][z])):
#         #     clearDB.append(0)
#         # else:
#     print(summar)
#     clearDB.append(round(abs(summar)))
#     summar = 0
# D = clearDB
# D.sort()
# DecibelMAX = np.max(D)
# DecibelMIN = np.min(D)
# renges = 0
# Gistoram = []
# i = 0
# iterat = 0
# while renges <= DecibelMAX - DecibelMIN:
#     for i in D:
#         if DecibelMIN + renges == i:
#             iterat += 1
#     Gistoram.append(iterat)
#     iterat = 0
#     renges +=1
# relProb = [ ]
# for i in Gistoram:
#     relProb.append(float("{0:.5f}".format(i/ sum(Gistoram))))
# probab = 0
# finalyMass = []
# for i in relProb:
#     finalyMass.append(probab + i)
#     probab = probab + i
# userProb = float(input("Введите доверительную вероятность: "))
# for index in range(len(finalyMass)):
#     if finalyMass[index] > userProb:
#         print(str(index + DecibelMIN) + " dB")
#         break
# else: print("Такой доверительности не существует")





