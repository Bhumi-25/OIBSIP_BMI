from tkinter import *

def BMI():
    weight = float(weight_value.get())
    height_feet = int(height_feet_value.get())
    height_inch = int(height_inch_value.get())
    height = (height_feet * 12) + height_inch
    bmi = float((weight * 703) / (height * height))

    bmi_num.set("Your BMI is %.2f" % bmi)
    if bmi < 18.5:
        bmi_text.set("You are underweight")
    elif 18.5 <= bmi < 25:
        bmi_text.set("You are normal")
    elif 25 <= bmi < 30:
        bmi_text.set("You are overweight")
    elif bmi >= 30:
        bmi_text.set("You are obese")

root = Tk()

# Adjusted geometry and set min and max size
root.geometry("380x300")
root.minsize(350, 300)
root.maxsize(500, 350)

# Set background color to light baby pink
root.configure(bg='#FFB6C1')

root.title("BMI calculator made by bhumi shah")
title_calculator = Label(root, text="BMI calculator", padx="20", pady="20", font="comicsansms 20 bold", bg='#FFB6C1')

title_calculator.grid(row=0, column=1, columnspan=4)

weight = Label(root, text="Enter your weight in pounds:", font=("Arial", 12, 'bold'), bg='#FFB6C1')
height_feet = Label(root, text="Enter your height in feet:", font=("Arial", 12, 'bold'), bg='#FFB6C1')
height_inch = Label(root, text="Enter your height in inch:", font=("Arial", 12, 'bold'), bg='#FFB6C1')

weight.grid(row=1, column=1)
height_feet.grid(row=2, column=1)
height_inch.grid(row=3, column=1)

weight_value = StringVar()
height_feet_value = StringVar()
height_inch_value = StringVar()

weight_entry = Entry(root, textvariable=weight_value)
height_feet_entry = Entry(root, textvariable=height_feet_value)
height_inch_entry = Entry(root, textvariable=height_inch_value)

weight_entry.grid(row=1, column=2)
height_feet_entry.grid(row=2, column=2)
height_inch_entry.grid(row=3, column=2, columnspan=2)

Button(text="Submit", command=BMI, font=("Arial", 12, 'bold')).grid(row=4, column=1, columnspan=2)
bmi_num = StringVar()
Label(root, textvariable=bmi_num, font=("Arial", 20, 'bold'), bg='#FFB6C1').grid(row=5, column=1, columnspan=2)

# Same thing here
bmi_text = StringVar()
Label(root, textvariable=bmi_text, font=("Arial", 14, 'bold'), bg='#FFB6C1').grid(row=6, column=1, columnspan=2)

root.mainloop()
