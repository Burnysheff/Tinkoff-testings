import csv
import tkinter as tk
from tkinter.ttk import Combobox
def provint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False 
def delenie (n):
    with open ('C:\\Users\\Павел\\Desktop\\123.csv', encoding = 'utf-8') as f_file:
        f_reader = csv.reader(f_file, delimiter = ",")
        count = 0
        numb = 0
        LocalMin = n[3]
        for row in f_reader:
            if (count > 0):
                if ((float(row[0]) >= n[1]) and (float(row[1]) >= n[2]) and (float(row[0]) <= n[4]) and (float(row[1]) <= n[5])):
                    if (numb == 0):
                        n.append(float(row[4])) # n[12] - локальный минимум
                        n.append(float(row[0])) # n[13] - дата локального минимума
                        n.append(float(row[1])) # n[14] - время локального минимума
                        n.append(float(row[3])) # n[15] - локальный максимум
                        n.append(float(row[0])) # n[16] - дата локального максимума
                        n.append(float(row[1])) # n[17] - время локального максимума
                        localMax = n[15]
                        dif = n[15]- n[12]
                    if (numb > 0):
                        if (LocalMin >= float(row[4])):
                            LocalMin = float(row[4])
                            n[13] = float(row[0])
                            n[14] = float(row[1])
                        if (float(row[3]) > localMax):
                            localMax = float(row[3])
                            localMaxDate = float(row[0])
                            localMaxTime = float(row[1])
                        if (n[0] > localMaxDate and (localMax - LocalMin > dif)):
                            n[15] = localMax
                            n[16] = localMaxDate
                            n[17] = localMaxTime
                            dif = localMax - LocalMin
                    numb = numb + 1
            count = count + 1
        n[12] = LocalMin
def poiskdo(n):
    with open ('C:\\Users\\Павел\\Desktop\\123.csv', encoding = 'utf-8') as f_file:
        f_reader = csv.reader(f_file, delimiter = ",")
        count = 0
        differ = 0
        for row in f_reader:
            if (count > 0 and (float(row[0]) < n[1]) and (float(row[1]) < n[2])):
                if (count == 1):
                    n.append(float(row[4])) # n[18] - локальный минимум до
                    n.append(float(row[0])) # n[19] - дата локального минимума до
                    n.append(float(row[1])) # n[20] - время локального минимума до
                    n.append(float(row[3])) # n[21] - локальный максимум до
                    n.append(float(row[0])) # n[22] - дата локального максимума до
                    n.append(float(row[1])) # n[23] - время локального максимума до
                    n.append(float(row[4])) # n[24] - минимальное значение за все время до
                    n.append(float(row[0])) # n[25] - дата минимального за все время до
                    n.append(float(row[1])) # n[26] - время минимального за все время до
                    differ = float(row[3]) - float(row[4])
                if (count > 1):
                    if (n[24] > float(row[4])):
                        n[24] = float(row[4])
                        n[25] = float(row[0])
                        n[26] = float(row[1])
                    if (float(row[3]) >= n[21]):
                        if (float(row[4]) <= n[18]):
                            n[18] = float(row[4])
                            n[19] = float(row[0])
                            n[20] = float(row[1])
                            n[21] = float(row[3])
                            n[22] = float(row[0])
                            n[23] = float(row[1])
                            differ = float(row[3]) - float(row[4])
                        if (float(row[4]) > n[18]):
                            n[21] = float(row[3])
                            n[22] = float(row[0])
                            n[23] = float(row[1])
                            differ = float(row[3]) - n[18]
                    if (float(row[3]) < n[21]):
                        if (float(row[4]) < n[18]):
                            if (float(row[3]) - float(row[4]) > differ):
                                n[18] = float(row[4])
                                n[19] = float(row[0])
                                n[20] = float(row[1])
                                n[21] = float(row[3])
                                n[22] = float(row[0])
                                n[23] = float(row[1])
                                differ = float(row[3]) - float(row[4])
                    if (float(row[3]) - n[24] > differ):
                        n[18] = n[24]
                        n[19] = n[25]
                        n[20] = n[26]
                        n[21] = float(row[3])
                        n[22] = float(row[0])
                        n[23] = float(row[1])
                        differ = float(row[3]) - n[24]
            count = count + 1
def poiskposle(n):
    with open ('C:\\Users\\Павел\\Desktop\\123.csv', encoding = 'utf-8') as f_file:
        f_reader = csv.reader(f_file, delimiter = ",")
        differ = 0
        count = 0
        numb = 0
        for row in f_reader:
            if (count > 0 and (float(row[0]) > n[4]) and (float(row[1]) > n[5])):
                if (numb == 0):
                    n.append(float(row[4])) # n[27] - локальный минимум после
                    n.append(float(row[0])) # n[28] - дата локального минимума после
                    n.append(float(row[1])) # n[29] - время локального минимума после
                    n.append(float(row[3])) # n[30] - локальный максимум после
                    n.append(float(row[0])) # n[31] - дата локального максимума после
                    n.append(float(row[1])) # n[32] - время локального максимума после
                    n.append(float(row[4])) # n[33] - минимальное значение за все время после
                    n.append(float(row[0])) # n[34] - дата минимального за все время после
                    n.append(float(row[1])) # n[35] - время минимального за все время после
                    differ = float(row[3]) - float(row[4])
                if (numb > 0):
                    if (n[33] > float(row[4])):
                        n[33] = float(row[4])
                        n[34] = float(row[0])
                        n[35] = float(row[1])
                    if (float(row[3]) >= n[30]):
                        if (float(row[4]) <= n[27]):
                            n[27] = float(row[4])
                            n[28] = float(row[0])
                            n[29] = float(row[1])
                            n[30] = float(row[3])
                            n[31] = float(row[0])
                            n[32] = float(row[1])
                            differ = float(row[3]) - float(row[4])
                        if (float(row[4]) > n[27]):
                            n[30] = float(row[3])
                            n[31] = float(row[0])
                            n[32] = float(row[1])
                            differ = float(row[3]) - n[27]
                    if (float(row[3]) < n[30]):
                        if (float(row[4]) < n[27]):
                            if (float(row[3]) - float(row[4]) > differ):
                                n[27] = float(row[4])
                                n[28] = float(row[0])
                                n[29] = float(row[1])
                                n[30] = float(row[3])
                                n[31] = float(row[0])
                                n[32] = float(row[1])
                                differ = float(row[3]) - float(row[4])
                    if (float(row[3]) - n[33] > differ):
                        n[27] = n[33]
                        n[28] = n[34]
                        n[29] = n[35]
                        n[30] = float(row[3])
                        n[31] = float(row[0])
                        n[32] = float(row[1])
                        differ = float(row[3]) - n[33]
                numb = numb + 1
            count = count + 1
def poiskone(n):
    diff = 0
    with open ('C:\\Users\\Павел\\Desktop\\123.csv', encoding = 'utf-8') as f_file:
        f_reader = csv.reader(f_file, delimiter = ",")
        count = 0
        for row in f_reader:
            if (count == 1):
                n.append(float(row[4])) # n[0] - минимум
                n.append(float(row[0])) # n[1] - дата минимума
                n.append(float(row[1])) # n[2] - время минимума
                n.append(float(row[3])) # n[3] - максимум
                n.append(float(row[0])) # n[4] - дата максимума
                n.append(float(row[1])) # n[5] - время максимума
                n.append(float(row[4])) # n[6] - минимальное значение за все время
                n.append(float(row[0])) # n[7] - дата минимального за все время
                n.append(float(row[1])) # n[8] - время минимального за все время
                n.append(float(row[3])) # n[9] - максимум за все время
                n.append(float(row[0])) # n[10] - дата максимума за все время
                n.append(float(row[1])) # n[11] - время максимума за все время
                diff = float(row[3]) - float(row[4])
            if (count > 1):
                if (float(row[3]) > n[9]):
                    n[9] = float(row[3])
                    n[10] = float(row[0])
                    n[11] = float(row[1])
                if (n[6] > float(row[4])):
                    n[6] = float(row[4])
                    n[7] = float(row[0])
                    n[8] = float(row[1])
                if (float(row[3]) >= n[3]) :
                    if (float(row[4]) <= n[0]):
                        n[0] = float(row[4])
                        n[1] = float(row[0])
                        n[2] = float(row[1])
                        n[3] = float(row[3])
                        n[4] = float(row[0])
                        n[5] = float(row[1])
                        diff = float(row[3]) - float(row[4])
                    if (float(row[4]) > n[0]):
                        n[3] = float(row[3])
                        n[4] = float(row[0])
                        n[5] = float(row[1])
                        diff = float(row[3]) - n[0]
                if (float(row[3]) < n[3]):
                    if (float(row[4]) < n[0]):
                        if (float(row[3]) - float(row[4]) > diff):
                            n[0] = float(row[4])
                            n[1] = float(row[0])
                            n[2] = float(row[1])
                            n[3] = float(row[3])
                            n[4] = float(row[0])
                            n[5] = float(row[1])
                            diff = float(row[3]) - float(row[4])
                if (float(row[3]) - n[6] > diff):
                    n[0] = n[6]
                    n[1] = n[7]
                    n[2] = n[8]
                    n[3] = float(row[3])
                    n[4] = float(row[0])
                    n[5] = float(row[1])
                    diff = float(row[3]) - n[6]
            count = count + 1
def sravn(n):
    n.append(n[15] - n[0]) # n[36] - первый промежуток внутри
    n.append(n[3] - n[12]) # n[37] - второй промежуток внутри
    n.append(n[21] - n[18]) # n[38] - промежуток до
    n.append(n[30] - n[27]) # n[39] - промежуток после
    n.append(n[3] - n [0]) # n[40] - максимальный промежуток
    r = 0
    if (n[39] >= n[38]):
        if (n[39] + n[40] >= n[36] + n[37]):
            n[6] = n[27]
            n[7] = n[28]
            n[8] = n[29]
            n[9] = n[30]
            n[10] = n[31]
            n[11] = n[32]
        if (n[39] + n[40] < n[36] + n[37]):
            r = n[3]
            n[3] = n[15]
            n[9] = r
            r = n[4]
            n[4] = n[16]
            n[10] = r
            r = n[5]
            n[5] = n[17]
            n[11] = r
            n[6] = n[12]
            n[7] = n[13]
            n[8] = n[14]
    if (n[39] < n[38]):
        if (n[38] + n[40] >= n[36] + n[37]):
            r = n[0]
            n[0] = n[18]
            n[6] = r
            r = n[1]
            n[1] = n[19]
            n[7] = r
            r = n[2]
            n[2] = n[20]
            n[8] = r
            r = n[3]
            n[3] = n[21]
            n[9] = r
            r = n[4]
            n[4] = n[22]
            n[10] = r
            r = n[5]
            n[5] = n[23]
            n[11] = r
        if (n[38] + n[40] < n[36] + n[37]):
            n[3] = n[15]
            n[4] = n[16]
            n[5] = n[17]
def varone():
    n = []
    poiskone(n)
    ldata.config(text = "Дата покупки:")
    ldata.place(x = 150, y = 270)
    ldataR.config(text = int(n[1]))
    ldataR.place(x = 150, y = 300)
    ltime.config(text = "Время покупки:")
    ltime.place(x = 400, y = 270)
    ltimeR.config(text = int(n[2]))
    ltimeR.place(x = 400, y = 300)
    lprice.config(text = "Стоимость при покупке:")
    lprice.place(x = 650, y = 270)
    lpriceR.config(text = n[0])
    lpriceR.place(x = 650, y = 300)
    sdata.config(text = "Дата продажи:")
    sdata.place(x = 150, y = 350)
    sdataR.config(text = int(n[4]))
    sdataR.place(x = 150, y = 380)
    stime.config(text = "Время продажи:")
    stime.place(x = 400, y = 350)
    stimeR.config(text = int(n[5]))
    stimeR.place(x = 400, y = 380)
    sprice.config(text = "Стоимость при продаже:")
    sprice.place(x = 650, y = 350)
    spriceR.config(text = n[3])
    spriceR.place(x = 650, y = 380)
    pr.config(text = "Прибыль составила")
    pr.place(x = 369, y = 420)
    pri.config(text = (n[3] - n[0]))
    pri.place(x = 485, y = 420)
    ldata2.place(x = 1000, y = 1000)
    ldataR2.place(x = 1000, y = 1000)
    ltime2.place(x = 1000, y = 1000)
    ltimeR2.place(x = 1000, y = 1000)
    lprice2.place(x = 1000, y = 1000)
    lpriceR2.place(x = 1000, y = 1000)
    sdata2.place(x = 1000, y = 1000)
    sdataR2.place(x = 1000, y = 1000)
    stime2.place(x = 1000, y = 1000)
    stimeR2.place(x = 1000, y = 1000)
    sprice2.place(x = 1000, y = 1000)
    spriceR2.place(x = 1000, y = 1000)
    pr2.place(x = 1000, y = 1000)
    pri2.place(x = 1000, y = 1000)
def vartwo():
    n = []
    poiskone(n)
    delenie(n)
    poiskdo(n)
    poiskposle(n)
    sravn(n)
    ldata.config(text = "Дата покупки:")
    ldata.place(x = 150, y = 270)
    ldataR.config(text = int(n[1]))
    ldataR.place(x = 150, y = 300)
    ltime.config(text = "Время покупки:")
    ltime.place(x = 400, y = 270)
    ltimeR.config(text = int(n[2]))
    ltimeR.place(x = 400, y = 300)
    lprice.config(text = "Стоимость при покупке:")
    lprice.place(x = 650, y = 270)
    lpriceR.config(text = n[0])
    lpriceR.place(x = 650, y = 300)
    sdata.config(text = "Дата продажи:")
    sdata.place(x = 150, y = 350)
    sdataR.place(x = 150, y = 380)
    sdataR.config(text = int(n[4]))
    stime.config(text = "Время продажи:")
    stime.place(x = 400, y = 350)
    stimeR.place(x = 400, y = 380)
    stimeR.config(text = int(n[5]))
    sprice.config(text = "Стоимость при продаже:")
    sprice.place(x = 650, y = 350)
    spriceR.place(x = 650, y = 380)
    spriceR.config(text = n[3])
    pr.config(text = "Прибыль составила")
    pr.place(x = 369, y = 420)
    pri.config(text = (n[3] - n[0]))
    pri.place(x = 485, y = 420)
    
    ldata2.config(text = "Дата покупки:")
    ldata2.place(x = 150, y = 500)
    ldataR2.config(text = int(n[7]))
    ldataR2.place(x = 150, y = 530)
    ltime2.config(text = "Время покупки:")
    ltime2.place(x = 400, y = 500)
    ltimeR2.config(text = int(n[8]))
    ltimeR2.place(x = 400, y = 530)
    lprice2.config(text = "Стоимость при покупке:")
    lprice2.place(x = 650, y = 500)
    lpriceR2.config(text = n[6])
    lpriceR2.place(x = 650, y = 530)
    sdata2.config(text = "Дата продажи:")
    sdata2.place(x = 150, y = 580)
    sdataR2.place(x = 150, y = 610)
    sdataR2.config(text = int(n[10]))
    stime2.config(text = "Время продажи:")
    stime2.place(x = 400, y = 580)
    stimeR2.place(x = 400, y = 610)
    stimeR2.config(text = int(n[11]))
    sprice2.config(text = "Стоимость при продаже:")
    sprice2.place(x = 650, y = 580)
    spriceR2.place(x = 650, y = 610)
    spriceR2.config(text = n[9])
    pr2.config(text = "Прибыль составила")
    pr2.place(x = 369, y = 650)
    pri2.config(text = (n[9] - n[6]))
    pri2.place(x = 485, y = 650)
def varthree(chis):
    pred.config(text = "Для этого варианта ответ выводится к консоль!")
    pred.place(x = 330, y = 400)
    masmax = []
    masmin = []
    time = []
    data = []
    diff = 0
    i = 0
    count = 0
    with open ('C:\\Users\\Павел\\Desktop\\123.csv', encoding = 'utf-8') as f_file:
        f_reader = csv.reader(f_file, delimiter = ",")
        for row in f_reader:
            if (count > 0):
                masmax.append (float(row[4]))
                masmin.append (float(row[3]))
                data.append (float(row[0]))
                time.append (float(row[1]))
                i = i + 1
            count = 1
        n = [[0] * (len(masmax)) for i in range (chis+1)]
        for k in range (1,chis+1):
            diff = -1 * masmin[0]
            for q in range (1, len(masmax)):
                n[k][q] = max(n[k][q-1], masmax[q] + diff)
                diff = max(diff, n[k-1][q] - masmin[q])
        i = chis
        j = len(masmax) - 1
        pr = []
        tm = []
        dt = []
        diff = 0
        while(i != 0 and j != 0):
            if (n[i][j] == n[i][j-1]):
                j = j - 1
            else:
                pr.append(masmax[j])
                tm.append(time[j])
                dt.append(data[j])
                diff = n[i][j] - masmax[j]
                k = j - 1
                while (k >= 0):
                    if (n[i-1][k] - masmin[k] == diff):
                        i = i - 1
                        j = k
                        pr.append(masmin[j])
                        tm.append(time[j])
                        dt.append(data[j])
                        break
                    k = k - 1
        pr.reverse()
        tm.reverse()
        dt.reverse()
        for i in range (len(pr)):
            print()
            if (i % 2 == 0):
                print("Цена при покупке: ", pr[i])
                print("Время покупки: ", tm[i])
                print("Дата покупки: ", dt[i])
            if (i % 2 == 1):
                print("Цена при продаже: ", pr[i])
                print("Время продажи: ", tm[i])
                print("Дата продажи: ", dt[i])
            if (i % 2 == 1):
                print ()
                print ("Прибыль за этот промежуток составит ", pr[i] - pr[i-1])
def prog (event):
    resvar = combo.get()
    if (resvar == "Одна покупка/продажа"):
        varone()
    if (resvar == "Две покупки/продажи"):
        vartwo()
    if (resvar == "Много покупок/продаж"):
        lablol.place(x=270, y=250)
        vvod.place(x=390, y=300)
        butnum.place(x=425, y=340)
def kolich (event):
    chislo = vvod.get()
    if (provint(chislo) == True):
        chis = int(chislo)
        if (chis > 0):
            if (chis == 1):
                varone()
            elif (chis == 2):
                vartwo()
            else:
                varthree(chis)
        else:
            labosh.place(x=300, y=375)
    else:
        labosh.place(x=300, y=375)
win = tk.Tk()
win.geometry("900x900")
win.config(bg='bisque4')
lablol=tk.Label(win,text="Введите, пожалуйста, количество возможных покупок/продаж")
lablol.config(font=("Arial",11),bg='azure2')
vvod=tk.Entry(win, width = 20)
txt=tk.Label(win,text="Когда стоило покупать акции?")
txt.config(font=("Comic Sans MS",25,"bold"))
txt.place(x=200,y=40)
lab=tk.Label(win,text="Выберите уровень сложности")
lab.config(font=("Arial",12),bg='antique white')
lab.place(x=350,y=120)
combo=Combobox(win)
combo["values"]=("Одна покупка/продажа", "Две покупки/продажи","Много покупок/продаж")
combo.place(x=380,y=165)
combo.current("0")
but=tk.Button(win,text="Выбрать")
but.config(font=("Arial",10),bg='antique white')
but.place(x=426,y=205)
but.bind("<Button-1>", prog)
butnum=tk.Button(win,text="Указать")
butnum.config(font=("Arial",10),bg='antique white')
butnum.bind("<Button-1>", kolich)
labosh=tk.Label(win,text="Введите, пожалуйста, натуральное число!")
labosh.config(font=("Arial",15),bg = 'gray34',fg = 'red')
ldata=tk.Label(win, text = " ")
ldataR=tk.Label(win, text = " ")
ltime=tk.Label(win, text = " ")
ltimeR=tk.Label(win, text = " ")
lprice=tk.Label(win, text = " ")
lpriceR=tk.Label(win, text = " ")
sdata=tk.Label(win, text = " ")
sdataR=tk.Label(win, text = " ")
stime=tk.Label(win, text = " ")
stimeR=tk.Label(win, text = " ")
sprice=tk.Label(win, text = " ")
spriceR=tk.Label(win, text = " ")
pr=tk.Label(win, text = " ")
pri=tk.Label(win, text = " ")
ldata2=tk.Label(win, text = " ")
ldataR2=tk.Label(win, text = " ")
ltime2=tk.Label(win, text = " ")
ltimeR2=tk.Label(win, text = " ")
lprice2=tk.Label(win, text = " ")
lpriceR2=tk.Label(win, text = " ")
sdata2=tk.Label(win, text = " ")
sdataR2=tk.Label(win, text = " ")
stime2=tk.Label(win, text = " ")
stimeR2=tk.Label(win, text = " ")
sprice2=tk.Label(win, text = " ")
spriceR2=tk.Label(win, text = " ")
pr2=tk.Label(win, text = " ")
pri2=tk.Label(win, text = " ")
pred=tk.Label(win,text = " ")
win.mainloop()