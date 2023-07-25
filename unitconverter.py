
from tkinter import *

class UnitConverter:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("305x409")
        self.root.title("Unit Converter")
        self.frame = Frame(self.root, width=305, height=409)
        self.frame.pack()
        self.main_widgets()

    def main_widgets(self):
        self.label = Label(self.frame, text="What you want to Convert ?", font=("Roboto", 15), height=2)
        self.length_btn = Button(self.frame, text="Length", width=10, height=5, borderwidth=2,
                                    font=("Roboto", 9), command=self.length_widget)
        self.speed_btn = Button(self.frame, text="Speed", width=10, height=5, borderwidth=2,
                                   font=("Roboto", 9), command=self.speed_widget)
        self.temp_btn = Button(self.frame, text="Temperature", width=10, height=5, borderwidth=2,
                                  font=("Roboto", 9), command=self.temp_widget)
        self.age_btn = Button(self.frame, text="Age", width=10, height=5, borderwidth=2,
                                 font=("Roboto", 9), command=self.age_widget)
        self.weight_btn = Button(self.frame, text="Weight", width=10, height=5, borderwidth=2,
                                    font=("Roboto", 9), command=self.weight_widget)
        self.pressure_btn = Button(self.frame, text="Pressure", width=10, height=5, borderwidth=2,
                                      font=("Roboto", 9), command=self.pressure_widget)

        self.label.grid(row=1, column=1, columnspan=4)
        self.length_btn.grid(row=2, column=1)
        self.speed_btn.grid(row=2, column=2)
        self.temp_btn.grid(row=2, column=3)
        self.age_btn.grid(row=3, column=1)
        self.weight_btn.grid(row=3, column=2)
        self.pressure_btn.grid(row=3, column=3)

        self.frame.place(relx=0.5, rely=0.4, anchor="center")

    def destroy(self):
        self.label.destroy()
        self.length_btn.destroy()
        self.speed_btn.destroy()
        self.temp_btn.destroy()
        self.age_btn.destroy()
        self.weight_btn.destroy()
        self.pressure_btn.destroy()

    def back(self):
        self.label1.destroy()
        self.label2.destroy()
        self.convert_btn.destroy()
        self.entry1.destroy()
        self.back_button.destroy()
        self.res.destroy()
        self.main_widgets()

class Length(UnitConverter):
    def length_widget(self):
        self.destroy()

        self.label1 = Label(self.frame, text="Mile (mi) >", width=15)
        self.label2 = Label(self.frame, text="Kilometer (km) >", width=15)
        self.entry1 = Entry(self.frame)
        self.res = Label(self.frame, text="")
        self.back_button = Button(self.frame, text="Back", command=self.back)
        self.convert_btn = Button(self.frame, text="Convert", command=self.length_cnvrt)

        self.label1.grid(row=1, column=1)
        self.entry1.grid(row=1, column=2)
        self.label2.grid(row=2, column=1)
        self.res.grid(row=2, column=2)
        self.back_button.grid(row=3, column=1)
        self.convert_btn.grid(row=3, column=2)

    def length_cnvrt(self):
        try:
            len_mile = float(self.entry1.get())
            len_km = round(len_mile * 1.60934,3)
            self.res.config(text=str(len_km))
        except ValueError:
            self.res.config(text="Invalid Format")

class Speed(UnitConverter):
    def speed_widget(self):
        self.destroy()

        self.label1 = Label(self.frame, text="Kilometer/hour (Km/h) >", width=20)
        self.label2 = Label(self.frame, text="Meter/second (m/s) >", width=20)
        self.entry1 = Entry(self.frame)
        self.res = Label(self.frame, text="")
        self.back_button = Button(self.frame, text="Back", command=self.back)
        self.convert_btn = Button(self.frame, text="Convert", command=self.speed_cnvrt)

        self.label1.grid(row=1, column=1)
        self.entry1.grid(row=1, column=2)
        self.label2.grid(row=2, column=1)
        self.res.grid(row=2, column=2)
        self.back_button.grid(row=3, column=1)
        self.convert_btn.grid(row=3, column=2)

    def speed_cnvrt(self):
        try:
            speed_kmph = float(self.entry1.get())
            speed_mps = round(speed_kmph * 0.277778,3)
            self.res.config(text=str(speed_mps))
        except ValueError:
            self.res.config(text="Invalid Format")

class Temp(UnitConverter):
    def temp_widget(self):
        self.destroy()

        self.label1 = Label(self.frame, text="Degree Celsius (°C) >", width=20)
        self.label2 = Label(self.frame, text="Degree Fahrenheit (°F) >", width=20)
        self.entry1 = Entry(self.frame)
        self.res = Label(self.frame, text="")
        self.back_button = Button(self.frame, text="Back", command=self.back)
        self.convert_btn = Button(self.frame, text="Convert", command=self.temp_cnvrt)

        self.label1.grid(row=1, column=1)
        self.entry1.grid(row=1, column=2)
        self.label2.grid(row=2, column=1)
        self.res.grid(row=2, column=2)
        self.back_button.grid(row=3, column=1)
        self.convert_btn.grid(row=3, column=2)

    def temp_cnvrt(self):
        try:
            temp_celsius = float(self.entry1.get())
            temp_fahrenheit = (temp_celsius * 9/5) + 32
            self.res.config(text=str(temp_fahrenheit))
        except ValueError:
            self.res.config(text="Invalid Format")

class Age(UnitConverter):
    def age_widget(self):
        self.destroy()

        self.label1 = Label(self.frame, text="Enter Date of Birth (DD-MM-YYYY)", width=30)
        self.label2 = Label(self.frame, text="Age: ", width=20)
        self.entry1 = Entry(self.frame)
        self.res = Label(self.frame, text="")
        self.back_button = Button(self.frame, text="Back", command=self.back)
        self.convert_btn = Button(self.frame, text="Convert", command=self.age_cnvrt)

        self.label1.grid(row=1, column=1, columnspan=4)
        self.entry1.grid(row=2, column=1)
        self.label2.grid(row=3, column=1)
        self.res.grid(row=3, column=2)
        self.back_button.grid(row=4, column=1)
        self.convert_btn.grid(row=4, column=2)

    def age_cnvrt(self):
        from datetime import date
        dob = self.entry1.get().split("-")
        try:
            current = date.today()
            age = (((current.year * 12) + current.month) - ((int(dob[2]) * 12) + int(dob[1]))) // 12
            self.res.config(text=str(age))
        except ValueError:
            self.res.config(text="Invalid Format")

class Weight(UnitConverter):
    def weight_widget(self):
        self.destroy()

        self.label1 = Label(self.frame, text="Kilogram (Kg) >", width=15)
        self.label2 = Label(self.frame, text="Gram (g) >", width=15)
        self.entry1 = Entry(self.frame)
        self.res = Label(self.frame, text="")
        self.back_button = Button(self.frame, text="Back", command=self.back)
        self.convert_btn = Button(self.frame, text="Convert", command=self.weight_cnvrt)

        self.label1.grid(row=1, column=1)
        self.entry1.grid(row=1, column=2)
        self.label2.grid(row=2, column=1)
        self.res.grid(row=2, column=2)
        self.back_button.grid(row=3, column=1)
        self.convert_btn.grid(row=3, column=2)

    def weight_cnvrt(self):
        try:
            weight_kg = float(self.entry1.get())
            weight_g = round(weight_kg * 1000,3)
            self.res.config(text=str(weight_g))
        except ValueError:
            self.res.config(text="Invalid Format")

class Pressure(UnitConverter):
    def pressure_widget(self):
        self.destroy()

        self.label1 = Label(self.frame, text="Bar (bar) >", width=15)
        self.label2 = Label(self.frame, text="Pascal (Pa) >", width=15)
        self.entry1 = Entry(self.frame)
        self.res = Label(self.frame, text="")
        self.back_button = Button(self.frame, text="Back", command=self.back)
        self.convert_btn = Button(self.frame, text="Convert", command=self.pressure_cnvrt)

        self.label1.grid(row=1, column=1)
        self.entry1.grid(row=1, column=2)
        self.label2.grid(row=2, column=1)
        self.res.grid(row=2, column=2)
        self.back_button.grid(row=3, column=1)
        self.convert_btn.grid(row=3, column=2)

    def pressure_cnvrt(self):
        try:
            pressure_pa = float(self.entry1.get())
            pressure_bar = round(pressure_pa * 100000,3)
            self.res.config(text=str(pressure_bar))
        except ValueError:
            self.res.config(text="Invalid Format")

class Action(Length, Speed, Temp, Age, Weight, Pressure):
    def run(self):
        self.root.mainloop()

obj = Action()
obj.run()
