'''
Программа для подсчета выгоды от съема жилья в командировках.
Выгода берется из разницы в стоимостях между гостиницей и съемной квартирой.
Если жить в съемной квартире, но отчитываться чеком из гостиницы на большую
сумму, то можно забрать себе разницу.
Пример: снять квартиру за 1500 руб/сутки, отчитаться на 5000 руб/сутки, то
за вычетом процента за чек(от суммы или от разницы, который берут квартиранты)
можно дополнительно получать около 3000 руб/сутки
'''
import os
import tkinter as tk
from datetime import datetime



class Hoteldata: #класс содержит методы для подсчета процентов и дохода
    def __init__(self,price,realprice,days=1,percent=0,switch=1,city='Мухосранск'):
        self.price=price
        self.realprice=realprice
        self.days=days
        self.percent=percent
        self.switch=switch
        self.city=city
        self.date=datetime.now().date()
    def __str__(self):    #конструирует строки, отображающие результат подсчета для вывода и/или сохранения
        return 'Дата: %s\nГород: %s\nСумма по чеку: %s\nСумма по факту: %s\nПроцент в день: %s\nПроцент за все дни: %s\nПрибыль: %s' % (self.date,self.city,
                                                                                                                        self.price*self.days,
                                                                                                                        self.realprice*self.days,
                                                                                                                        Hoteldata.perconday(self),
                                                                                                                        Hoteldata.perc_days(self),
                                                                                                                        Hoteldata.profit(self))

    def perconday(self): #считает процент в день
        return self.percent*(self.price*0.01) if self.switch==1 else self.percent*((self.price-self.realprice)*0.01)
    def perc_days(self): #считает процент за все дни
        return Hoteldata.perconday(self)*self.days
    def profit(self): #считает выгоду за все дни
        return (self.price*self.days)-((Hoteldata.perconday(self)*self.days)+(self.realprice*self.days))
    def getter(self): #возвращает текущую дату с помощью datetime
        return self.date


def disp(): #забирает введенные данные из полей ввода и передает их методам класса
    sum=entry1.get()
    rsum=entry2.get()
    ddays=entry3.get()
    dperc=entry4.get()
    dcity=entry5.get()
    global data #обьявляется глобальной чтобы была видна в функции writer
    data=Hoteldata(int(sum),int(rsum),days=int(ddays),percent=int(dperc),switch=selected.get(),city=str(dcity))
    label['text']=data
def writer():  #сохраняет сконструированные методом класса строки в файл txt
    adr = entry5.get()
    file = open(u'D://Hotels//' + adr + ' ' + str(data.getter()) + '.txt', 'w+')
    disp = print(data, file=file)
    file.close()
window=tk.Tk()  #графический интерфейс
window.geometry('250x400')
label_cs=tk.Label(text='Классический схемач')
label=tk.Label(text='res')
label_cs.pack()
selected=tk.IntVar()
rad1=tk.Radiobutton(window,text='От суммы',value=1,variable=selected);rad1.pack()
rad2=tk.Radiobutton(window,text='От разницы',value=2,variable=selected);rad2.pack()
entry1=tk.Entry();entry1.insert(0,'Сумма по чеку');entry1.pack()
entry2=tk.Entry();entry2.insert(0,'Сумма по факту');entry2.pack()
entry3=tk.Entry();entry3.insert(0,'Дни');entry3.pack()
entry4=tk.Entry();entry4.insert(0,'Процент');entry4.pack()
entry5=tk.Entry();entry5.insert(0,'Город');entry5.pack()
button1=tk.Button(text='Посчитать',command=disp);button1.pack()
button2=tk.Button(text='Сохранить',command=writer);button2.pack()
label=tk.Label(text=0);label.pack()
rad1.pack();rad2.pack()
window.mainloop()



