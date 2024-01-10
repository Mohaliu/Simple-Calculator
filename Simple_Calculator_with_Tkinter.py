#!/usr/bin/env python
# coding: utf-8

# In[47]:


# importing necessary libraries
from tkinter import Tk
from tkinter import Entry
from tkinter import Button

# create a variable to hold the method Tk
root = Tk()

# creating a title for the display window
root.title('Simple Calculator')

# creating an entry widget to show our inputs and outputs
display = Entry(root, width=20, borderwidth=10, font=('Helvetica', 16))
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# variable to keep our displayed values
inputs = ''

# function that gives output to the display when a number or symbol button is clicked
def button_commands(sym_num):
    global inputs
    inputs += str(sym_num)
    display.delete(0, 'end')
    display.insert(0, inputs)
    
# function that performs all the calculation operations
def equal_to():
    try:
        global inputs
        display.delete(0, 'end')
        display.insert(0, round(eval(inputs), 5))
    except ZeroDivisionError:
        clear()
        display.insert(0, 'Cannot divide a number by 0.')
    except SyntaxError:
        clear()
        display.insert(0, 'Input is invalid')

# function to clear the display on the screen
def clear():
    global inputs
    display.delete(0, 'end')
    inputs = ''

# creating the buttons for each numbers and placing it in a grid format
button_1 = Button(root, text='1', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(1))
button_1.grid(row=1, column=0)
button_2 = Button(root, text='2', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(2))
button_2.grid(row=1, column=1)
button_3 = Button(root, text='3', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(3))
button_3.grid(row=1, column=2)
button_4 = Button(root, text='4', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(4))
button_4.grid(row=2, column=0)
button_5 = Button(root, text='5', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(5))
button_5.grid(row=2, column=1)
button_6 = Button(root, text='6', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(6))
button_6.grid(row=2, column=2)
button_7 = Button(root, text='7', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(7))
button_7.grid(row=3, column=0)
button_8 = Button(root, text='8', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(8))
button_8.grid(row=3, column=1)
button_9 = Button(root, text='9', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(9))
button_9.grid(row=3, column=2)
button_0 = Button(root, text='0', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands(0))
button_0.grid(row=4, column=1)

# creating the buttons for each symbols and placing it in a grid format
button_decimal = Button(root, text='.', font=('Arial', 15), padx=35, pady=20, command=lambda: button_commands('.'))
button_decimal.grid(row=5, column=1)
button_addition = Button(root, text='+', font=('Arial', 15), padx=35, pady=20, command=lambda: button_commands('+'))
button_addition.grid(row=4, column=0)
button_subtraction = Button(root, text='-', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands('-'))
button_subtraction.grid(row=4, column=2)
button_multplication = Button(root, text='x', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands('*'))
button_multplication.grid(row=5, column=0)
button_division = Button(root, text='/', font=('Arial', 15), padx=36, pady=20, command=lambda: button_commands('/'))
button_division.grid(row=6, column=0)
button_equals = Button(root, text='=', font=('Arial', 15), padx=90, pady=20, command=equal_to)
button_equals.grid(row=6, column=1, columnspan=2)
button_clear = Button(root, text='C', font=('Arial', 15), padx=36, pady=20, command=clear)
button_clear.grid(row=5, column=2)

# calling the mainloop of Tk to run the program
root.mainloop()


# In[56]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




