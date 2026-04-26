from tkinter import Button, Label, StringVar, Tk
from tkinter import ttk
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def dataget():
    city = com.get()  
    data = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q=" + city +
        "&appid=" + API_KEY
    ).json()

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(round(data["main"]["temp"] - 273.15, 2)) + " °C")
    pressure_label1.config(text=str(data["main"]["pressure"]) + " hPa")

new = Tk()
new.title("Weather App")
new.config(bg="blue")
new.geometry("500x530")  

name_label = Label(new, text="Weather App",
    font=("Times New Roman", 30, "bold"),  
    bg="black",
    fg="white")
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()

list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
"Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
"Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
"Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
"Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
"Uttarakhand", "West Bengal"]

com = ttk.Combobox(new, values=list_name, font=("Times New Roman", 20, "bold"))
com.place(x=25, y=120, height=50, width=450)

Search_button = Button(new, text="Search", bg="black", fg="white",
    font=("Times New Roman", 20, "bold"), command=dataget)
Search_button.place(x=200, y=190, height=50, width=100)

w_label = Label(new, text="Weather Climate", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(new, text="", font=("Times New Roman", 20), bg="blue", fg="white")  
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(new, text="Description", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
wb_label.place(x=25, y=330, height=50, width=210)
wb_label1 = Label(new, text="", font=("Times New Roman", 20), bg="blue", fg="white")  
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(new, text="Temperature", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(new, text="", font=("Times New Roman", 20), bg="blue", fg="white")  
temp_label1.place(x=250, y=400, height=50, width=210)

pressure_label = Label(new, text="Pressure", font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
pressure_label.place(x=25, y=470, height=50, width=210)
pressure_label1 = Label(new, text="", font=("Times New Roman", 20), bg="blue", fg="white")  
pressure_label1.place(x=250, y=470, height=50, width=210)

new.mainloop()

