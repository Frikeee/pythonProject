import numpy as np
from scipy.fft import rfft
import scipy.io.wavfile as wf
import math
import wave
import matplotlib.pyplot as plt
import librosa
import librosa.display

# D = []
# Deci = []
# Z = []
# norm = []
# M = 1024
# audio = 'sin1000.wav'
# snd, sampFreq = librosa.load(audio)
#
#
# snd = snd / (2.**15) #Convert sound array to floating point values
#                      #Floating point values range from -1 to 1
#
# s1 = snd #left channel
#
# timeArray = np.arange(0, len(snd) + 1, 2)
# timeArray = timeArray / sampFreq
# timeArray = timeArray * 1000   #scale to milliseconds
# print(len(timeArray))
#
#
# n = len(s1)
# p = fft(s1) # take the fourier transform
# print(len(p))
#
# nUniquePts = math.ceil((n+1)/2)
# p = p[0:nUniquePts]
# p = abs(p)
# print(len(p))
#
#
# '''
# Left Channel
# '''
# p = p / float(n) # scale by the number of points so that
#              # the magnitude does not depend on the length
#              # of the signal or on its sampling frequency
# p = p**2  # square it to get the power
#
#
#
# if n % 2 > 0: # we've got odd number of points fft
#     p[1:len(p)] = p[1:len(p)] * 2
# else:
#     p[1:len(p) -1] = p[1:len(p) - 1] * 2 # we've got even number of points fft
# F = 10 * np.log10(p)
# print(len(F))
# print(len(timeArray))
# plt.plot(timeArray , F, 'k')
# plt.xlabel('Frequency (kHz)')
# plt.ylabel('Power (dB)')
# plt.show()
# time = math.floor(len(snd) / sampFreq) * 8
# startMass = 0
# while (time > 0):
#     D.append(np.abs(round(F[startMass * 2935 + 44: (startMass + 1) * 2935].sum() / 2935 * 32767)))
#     time = time - 1
#     startMass += 1
# D = np.around(D)
# DecibelMAX = np.max(D)
# DecibelMIN = np.min(D)
# print(len(D))
# for i in range(len(F)):
#     print(F[i])
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












# wav_obj = wave.open(audio, 'rb')
# n_samples = wav_obj.getframerate()
# signal_wave = wav_obj.readframes(n_samples)
# signal_array = np.frombuffer(signal_wave, dtype=np.int8)
# print(signal_array)
# a = signal_array.T[0]
# audio, mass = wf.read(audio)
# time = math.floor(mass.shape[0] / audio) * 8
# startMass = 0
# while (time > 0):
#     D.append(np.abs(round(mass[startMass * 2935 + 44: (startMass + 1) * 2935].sum() / 2935 * 32767)))
#     time = time - 1
#     startMass += 1
# # a = norm.T[0]
# # b=[(ele/2**16.)*2-1 for ele in a]
# # c = rfft(mass)
# # S = np.abs(c)
# # dlin = (len(S) / 2935) - 1
# # startMass = 0
# # while (dlin > 0):
# #     D.append(round(S[startMass * 2935 + 44: (startMass + 1) * 2935].sum() / 2935))
# #     dlin = dlin - 1
# #     startMass += 1
# # D = np.abs(D)
# for index in range(len(D)):
#     if( D[index] > 0):
#         D[index] = 20 * np.log10(D[index]/np.max(D))
#         D[index] = round(D[index])
# D = np.abs(D)
# DecibelMAX = np.max(D)
# print(DecibelMAX)
# DecibelMIN = np.min(D)
# print(DecibelMIN)
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


# D = []
# Z = []
# M = 1024
# audio = 'sin1000.wav'
# snd, sampFreq = librosa.load(audio)
# S = np.abs(librosa.stft(snd, hop_length=512))
# # c = rfft(spec)
# # S = np.abs(c)
# S = 20 * np.log10(S / np.max(S))
# dlin = (len(S) / 2935) - 1
# startMass = 0
# while (dlin > 0):
#     D.append(round(S[startMass * 2935 + 44: (startMass + 1) * 2935].sum() / 2935))
#     dlin = dlin - 1
#     startMass += 1
# D = np.abs(D)
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
file = '85.wav'
y, sr = librosa.load(file)
y = abs(y)
# fig, ax = plt.subplots(nrows=1, sharex=True, sharey=True)
# librosa.display.waveshow(averagedDB, sr=sr/8, ax=ax)
# ax.set(title='Monophonic')
# ax.label_outer()
# plt.show()
S = np.abs(librosa.stft(y))
fig, ax = plt.subplots()
print(np.max(S), " ", np.min(S))
srdb = (np.max(S) - np.min(S) )/ 2 + 20
img = librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max, top_db = None), y_axis='log', x_axis='time', ax=ax)
ax.set_title('Power spectrogram')
fig.colorbar(img, ax=ax, format="%+2.0f dB")
plt.show()
Db = librosa.amplitude_to_db(S, ref=np.max, top_db = None)
print(np.max(Db), " ", np.min(Db))
print(np.shape(Db))
print(len(Db))
clearDB = []
summar = 0
for i in range(len(Db[1])):
    for z in range(len(Db)):
        summar += Db[z][i] / 1025
        # if round(srdb) < round(abs(Db[i][z])):
        #     clearDB.append(0)
        # else:
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
    renges +=1
relProb = [ ]
for i in Gistoram:
    relProb.append(float("{0:.5f}".format(i/ sum(Gistoram))))
probab = 0
finalyMass = []
for i in relProb:
    finalyMass.append(probab + i)
    probab = probab + i
userProb = float(input("Введите доверительную вероятность: "))
for index in range(len(finalyMass)):
    if finalyMass[index] > userProb:
        print(str(index + DecibelMIN) + " dB")
        break
else: print("Такой доверительности не существует")





