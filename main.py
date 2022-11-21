import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from tkinter import *
import os
import re
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import time
from threading import *


class Probability():
    """Расчёт доверительной вероятности"""
    def __init__(self):
        self.file = ''
        self.y = []
        self.sr = 0
        self.S = []
        self.fileLoad = False
        self.finalyMass = []
        self.DecibelMIN = 0
        self.DecibelArr = []
        self.DoLoading = False
    def FFT(self, filename):
        """Рассчёт Фурье"""
        self.y, self.sr = librosa.load(filename)
        self.y = abs(self.y)
        self.S = np.abs(librosa.stft(self.y))
    def openFile(self):
        """
        Открытие файла в программу
        """
        self.__init__()
        self.fileLoad = False
        self.DecibelMIN = 0
        filename = askopenfilename()
        self.loading()
        file = os.path.basename(filename)
        print(file)
        self.FFT(filename)
        self.loading_stop()
    def openPowerSpec(self):
        """График спектрограммы мощности"""
        fig, ax = plt.subplots()
        img = librosa.display.specshow(librosa.amplitude_to_db(self.S, ref=np.max, top_db=None), y_axis='log', x_axis='time',
                                       ax=ax)
        ax.set_title('Cпектрограмма мощности')
        fig.colorbar(img, ax=ax, format="%+2.0f dB")
        ax.set_xlabel("Время")
        ax.set_ylabel("Герц")
        plt.show()

    def is_valid(self, newval):
        """Проверка написания доверительной вероятности"""
        return re.match("^\d{0,1}\.{0,1}\d{0,2}$", newval) is not None

    def audioSpec(self):
        """Постройка временной диаграммы файла"""
        fig, ax = plt.subplots(nrows=1, sharex=True, sharey=True)
        librosa.display.waveshow(self.y, sr=self.sr, ax=ax)
        ax.set(title='Временной спектр аудиофайла')
        ax.set_xlabel("Время")
        ax.set_ylabel("Амплитуда")
        ax.label_outer()
        plt.show()

    def calcdB(self):
        Db = librosa.amplitude_to_db(self.S, ref=np.max, top_db=None)
        clearDB = []
        summar = 0
        for i in range(len(Db[1])):
            for z in range(len(Db)):
                summar += Db[z][i] / 1025
            clearDB.append(round(abs(summar)))
            summar = 0
        D = clearDB
        D.sort()
        DecibelMAX = np.max(D)
        self.DecibelMIN = np.min(D)
        renges = 0
        Gistoram = []
        iterat = 0
        for i in range(DecibelMAX - self.DecibelMIN + 1):
            self.DecibelArr.append(self.DecibelMIN + i)
        while renges <= DecibelMAX - self.DecibelMIN:
            for i in D:
                if self.DecibelMIN + renges == i:
                    iterat += 1
            Gistoram.append(iterat)
            iterat = 0
            renges += 1
        print(Gistoram)
        prevValue = 0
        for i in Gistoram:
            prevValue = prevValue + i / sum(Gistoram)
            self.finalyMass.append(float("{0:.5f}".format(prevValue)))
        print(self.finalyMass)
        self.fileLoad = True


    def probabFunc(self):
        """Высчитывание доверительной информации"""
        userProb = (float)(userProbTF.get())
        if self.fileLoad == False:
            self.calcdB()
        for index in range(len(self.finalyMass)):
            if self.finalyMass[index] > userProb:
                textProb["text"] = "Доверительная громкость: " + str(index + self.DecibelMIN) + " dB"
                break
        else:
            messagebox.showerror(title='Некорректные данные',
                                 message='Проверьте пожалуйста введённое значение доверительной вероятности. \nФормат '
                                         'ввода: "x.xx" , где x - цифра.\nДиапазон значений от 0.01 до 0.99')

    def decibelFunc(self):
        """Постройка доверительного спектра"""
        fig, ax = plt.subplots()
        print(self.DecibelArr)
        print(self.finalyMass)
        ax.plot(self.DecibelArr, self.finalyMass)
        ax.set(title='Доверительный спектр')
        ax.grid(color='black', linewidth=0.5)
        ax.set_xlabel("Акустическая мощность, Дб")
        ax.set_ylabel("Доверительная вероятность")
        ax.label_outer()
        plt.show()

    def dow(self):
        """Функция имитации загрузки"""
        while self.DoLoading:
            textProb["text"] = "Загрузка."
            time.sleep(1)
            textProb["text"] = "Загрузка.."
            time.sleep(1)
            textProb["text"] = "Загрузка..."
            time.sleep(1)
            textProb["text"] = "Загрузка...."
            time.sleep(1)
            textProb["text"] = "Успешно загружено"

    def loading(self):
        """Старт загрузки"""
        self.DoLoading = True
        Thread(target=self.dow).start()

    def loading_stop(self):
        """Окончание загрузки"""
        self.DoLoading = False

if __name__ == '__main__':
    mainWindow = Tk()
    prob = Probability()
    mainWindow['bg'] = '#AFEEEE'
    mainWindow.title('Trust Sound')
    mainWindow.geometry('300x300')
    mainWindow.resizable(width=False, height=False)
    canvas = Canvas(mainWindow, height=300, width=300)
    canvas.pack()
    frame = Frame(mainWindow, bg='#ADD8E6')
    frame.place(relx=0.025, rely=0.025, relheight=0.95, relwidth=0.95)
    check = (mainWindow.register(prob.is_valid), "%P")
    btn = Button(frame, text='Открыть файл', command=prob.openFile)
    btn.pack(anchor="nw", padx=5, pady=5)
    textProb = Label(frame, text='Введите доверительную вероятность:', bg='#ADD8E6')
    textProb.pack(anchor="w", padx=5)
    userProbTF = Entry(frame, validatecommand=check, validate="key")
    userProbTF.pack(anchor="w", padx=5)
    textProb = Label(frame, bg='#ADD8E6')
    textProb.pack(anchor="w", padx=5)
    btn = Button(frame, text='Временной спектр аудиофайла', command=prob.audioSpec)
    btn.pack(anchor="w", padx=5, pady=15)
    btn = Button(frame, text='Cпектрограмма мощности', command=prob.openPowerSpec)
    btn.pack(anchor="w", padx=5)
    btn = Button(frame, text='Доверительный спектр', command=prob.decibelFunc)
    btn.pack(anchor="w", padx=5, pady=15)
    btn = Button(frame, text='Рассчитать', command=prob.probabFunc)
    btn.pack(anchor="se", padx=5, pady=15)
    mainWindow.mainloop()
