import datetime
import tkinter as tk
from tkinter import ttk 		# 'ttk' makes the entry fields, buttons more lookable than 'tk'
from PIL import Image, ImageTk

# Creates a Window
window = tk.Tk()
window.geometry('500x700')
window.title('Age Calculator App')

# Creates Labels
name_label = tk.Label(text = 'Name')
name_label.grid(row = 1, column = 0)

year_label = tk.Label(text = 'Year')
year_label.grid(row = 2, column = 0)

month_label = tk.Label(text = 'Month')
month_label.grid(row = 3, column = 0)

date_label = tk.Label(text = 'Date')
date_label.grid(row = 4, column = 0)

# Creates Entry fields
name_entry = ttk.Entry()
name_entry.grid(row = 1, column = 1)

year_entry = ttk.Entry()
year_entry.grid(row = 2, column = 1)

month_entry = ttk.Entry()
month_entry.grid(row = 3, column = 1)

date_entry = ttk.Entry()
date_entry.grid(row = 4, column = 1)

# Function to carry out the required tasks
def calculate_age():
	print(name_entry.get())
	print(year_entry.get())
	print(month_entry.get())
	print(date_entry.get())
	user = Person(str(name_entry.get()), datetime.date(
		int(year_entry.get()),
		int(month_entry.get()),
		int(date_entry.get())
		)
	)
	print(user.age())
	display_text = tk.Text(master = window, height = 20, width = 30)
	display_text.grid(row = 6, column = 1)
	text_display =  '{name} is {age} years old.'.format(name = user.name, age = user.age())
	display_text.insert(tk.END, text_display)

# Creates a Button
calculate_button = ttk.Button(text = 'Calculate Age Now', command = calculate_age)
calculate_button.grid(row = 5, column = 1)

name_label.config(font = ('Arial', 22))
year_label.config(font = ('Arial', 22))
month_label.config(font = ('Arial', 22))
date_label.config(font = ('Arial', 22))
#calculate_button.config(height = 3)

class Person:
	def __init__(self, name, birthdate):
		self.name = name
		self.birthdate = birthdate

	def age(self):
		today = datetime.date.today()
		Age = today.year - self.birthdate.year
		return Age

# Creates an Image
image = Image.open('G:\Python\Learn Python OOP\Images\Age Calculator App Logo.jpg')
image.thumbnail((300, 300), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(image)

logo_image = ttk.Label(image = logo)
logo_image.grid(row = 0, column = 1)

window.mainloop()