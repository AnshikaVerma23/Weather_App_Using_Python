from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=68ea2792fd93efb0f15f9c8cafdfef11").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    t_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])



win = Tk()
win.title("AccuWeather..")
win.config(bg="yellow")
win.geometry("500x600")

name_label = Label(win,text="AccuWeather", font=("Palatino Linotype",30,"bold"))
name_label.place(x=25,y=50,width = 450,)

city_name = StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="AccuWeather",values=list_name,font=("Garamond",15,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


w_label = Label(win,text="Weather Climate",font=("Garamond",15,"bold"))
w_label.place(x=25,y=220,height=50,width=200)

w_label1 = Label(win,text="",font=("Garamond",15,"bold"))
w_label1.place(x=250,y=220,height=50,width=200)


wb_label = Label(win,text="Weather Description",font=("Garamond",15,"bold"))
wb_label.place(x=25,y=300,height=50,width=200)

wb_label1 = Label(win,text="",font=("Garamond",15,"bold"))
wb_label1.place(x=250,y=300,height=50,width=200)

t_label = Label(win,text="Temperature",font=("Garamond",15,"bold"))
t_label.place(x=25,y=370,height=50,width=200)

t_label1 = Label(win,text="",font=("Garamond",15,"bold"))
t_label1.place(x=250,y=370,height=50,width=200)


per_label = Label(win,text="Pressure",font=("Garamond",15,"bold"))
per_label.place(x=25,y=440,height=50,width=200)

per_label1 = Label(win,text="",font=("Garamond",15,"bold"))
per_label1.place(x=250,y=440,height=50,width=200)

done_button = Button(win, text="Done",font=("Garamond",15,"bold"),command=data_get)
done_button.place(y=510,height=50,width=280,x=100)

win.mainloop()
