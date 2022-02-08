from random import *
from tkinter import *
from tkinter import messagebox

code      = 4803 # pass code (can be any)
fieldCode = ''   # user-entered code
btn       = []   # array to fill with buttons


def rpc(): # creates an array for button values
	global list1
	array = [0,1,2,3,4,5,6,7,8,9] # array of values for buttons
	list1 = []                    # array for values for buttons

	for i in range(9, -1, -1):
		c = randint(0, i)
		list1.append(array[c])
		del array[c]
rpc()

def insertText(s): # array for values for buttons
	textDiary.insert(INSERT, s)
	textDiary.see(END)

def check(num): # checks the entered password:
	global code, fieldCode
	fieldCode += str(num)
	insertText(num)

	if (len(fieldCode) > 3 and int(fieldCode) != code): # -does it exceed the allowed length
		messagebox.showinfo('', 'Превышен лимит символов')
		textDiary.delete(1.0, END)
		fieldCode = ''
		rpc()
		placeAllButton()
	if (fieldCode.isdigit()): # removes the invalid literal for int() with base 10 error
		if (int(fieldCode) == code): # -whether it matches the passcode
			messagebox.showinfo('РЕЗУЛЬТАТ', 'Вы успешно вошли в систему!')		
			textDiary.delete(1.0, END)
			fieldCode = ''
			rpc()
			placeAllButton()

def placeAllButton(): # places all buttons except the last one
	# creating buttons in a list
	for i in range(10):
		btn.append(Button(text=f'{list1[i]}', font='arial 20', width=5, background='black', fg='white', command=lambda x=i: check(list1[x])))

	# button placement cycle
	y1 = 1
	b = 0
	for i in range(3):
		x1 = 20
		for j in range(1, 4):
			btn[b].place(x=x1, y=y1*80)
			x1 += 105
			b += 1
		y1 += 1

	# last button
	btn[9].place(x=125,y=320)

# creating a Tkinter window and setting parameters
root = Tk()

root["bg"] = "gray22"

WIDTH = 350
HEIGHT = 500

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.title('Пин-код панель')
root.resizable(False, False)
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

# Text window
textDiary = Text(width=6, height=1,font='arial 20', wrap=WORD)
textDiary.place(x=125,y=20)

placeAllButton()

root.mainloop()