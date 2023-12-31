from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)

        if location is None:
            messagebox.showerror("Weather App", "City not found!")
            return
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
        name.config(text="CURRENT WEATHER")
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        

        #  weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=e82e468f9e70bac860a7df1f73182caf&units=metric"  
        json_data = requests.get(api).json()
        print(json_data)
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"])
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        print("exception***", e)
        messagebox.showerror("Weather App", "Invalid Entry!")




# Search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=200, y=20)

textfield = tk.Entry(root, justify='center', width=17, font=('poppins', 25, 'bold'), bg='#404040', border=0, fg='white')
textfield.place(x=230, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=580, y=34)

# Logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=270, y=100)

# Bottom box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.config(height=100)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=210)
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=180)

# Label
labell1 = Label(root, text="WIND (m/s)", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
labell1.place(x=120, y=410)
labell2 = Label(root, text="HUMIDITY (%)", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
labell2.place(x=280, y=410)
labell3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
labell3.place(x=460, y=410)
labell4 = Label(root, text="PRESSURE (hPa)", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
labell4.place(x=650, y=410)

t = Label(text="...", font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=560, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=560, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=130, y=440)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=310, y=440)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=480, y=440)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=680, y=440)

root.mainloop()      
