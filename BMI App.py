import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('600x700')
root.title('BMI Calculator App')
root.configure(bg = '#ff3333')

name_label = ttk.Label(root, text = 'Name', font = font.Font(family = 'Arial', size = 16, weight = 'bold'))
name_label.grid(row = 1, column = 0)

weight_label = ttk.Label(root, text = 'Weight(in Kg.)', font = font.Font(family = 'Arial', size = 16, weight = 'bold'))
weight_label.grid(row = 2, column = 0)

height_label = ttk.Label(root, text = 'Height(in Cm.)', font = font.Font(family = 'Arial', size = 16, weight = 'bold'))
height_label.grid(row = 3, column = 0)

name_entry = ttk.Entry(root)
name_entry.grid(row = 1, column = 1)

weight_entry = ttk.Entry(root)
weight_entry.grid(row = 2, column = 1)

height_entry = ttk.Entry(root)
height_entry.grid(row = 3, column = 1)

def BodyMassIndex():
	print(name_entry.get())
	print(weight_entry.get())
	print(height_entry.get())
	user = Person(name_entry.get(), weight_entry.get(), height_entry.get())
	print(user.BMI())
	if(user.BMI() < 18.5):
		display_text = tk.Text(root, height = 30, width = 40)
		display_text.grid(row = 5, column = 1)
		text_display = '{name}, your BMI index is {index}.\n\nYou are UNDERWEIGHT.'.format(
			name = user.name,
			index = str(round(user.BMI(), 2))
			)
		display_text.insert(tk.END, text_display)
	elif(user.BMI() >= 18.5 & user.BMI() < 25.0):
		display_text = tk.Text(root, height = 30, width = 40)
		display_text.grid(row = 5, column = 1)
		text_display = '{name}, your BMI index is {index}.\n\nYou are NORMAL.'.format(
			name = user.name,
			index = str(round(user.BMI(), 2))
			)
		display_text.insert(tk.END, text_display)
	elif(user.BMI() >= 25.0 & user.BMI() < 30.0):
		display_text = tk.Text(root, height = 30, width = 40)
		display_text.grid(row = 5, column = 1)
		text_display = '{name}, your BMI index is {index}.\n\nYou are OVERWEIGHT.'.format(
			name = user.name,
			index = str(round(user.BMI(), 2))
			)
		display_text.insert(tk.END, text_display)
	elif(user.BMI() >= 30.0):
		display_text = tk.Text(root, height = 30, width = 40)
		display_text.grid(row = 5, coulmn = 1)
		text_display = '{name}, your BMI index is {index}.\n\nYou are OBESE.'.format(
			name = user.name,
			index = str(round(user.BMI(), 2))
			)
		display_text.insert(tk.END, text_display)

class Person:
	def __init__(self, name, weight, height):
		self.name = name
		self.weight = weight
		self.height = height

	def BMI(self):
		bmi = float(self.weight) / float((float(self.height) / 100.0) ** 2)
		bmi = float(bmi)
		return bmi

calculate_button = ttk.Button(root, text = 'Calculate Now!', command = BodyMassIndex)
calculate_button.grid(row = 4, column = 1)

image = Image.open('G:\Python\Learn Python OOP\Images\BMI_logo.jpg')
image.thumbnail((250, 250), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(image)

logo_image = ttk.Label(image = logo)
logo_image.grid(row = 0, column = 1)

root.mainloop()