import tkinter as tk
from tkinter import messagebox
from functools import partial
 
 
temp_Val = "Celsius"
 
def store_temp(set_temp):
    global temp_Val
    temp_Val = set_temp
 
def call_convert(rlabel1,  inputn):
    temp = inputn.get()
     
    if temp_Val == 'Celsius':
         
        # Conversion of celsius temperature to fahrenheit
        f = float((float(temp) * 9 / 5) + 32)
        rlabel1.config(text ="%.1f Fahrenheit" % f, bg="light green")
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Fahrenheit ", )
         
    if temp_Val == 'Fahrenheit':
         
        # Conversion of fahrenheit temperature to celsius
        c = float((float(temp) - 32) * 5 / 9)
        rlabel1.config(text ="%.1f Celsius" % c, bg="light green")
        messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Celsius ")
    return
 
 
root = tk.Tk()

 
root.title('GUI - Temperature Converter')
 
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(1, weight = 1)
 
inputNumber = tk.StringVar()
var = tk.StringVar()

input_label = tk.Label(root, text ="Enter temperature", bg="orange")
input_entry = tk.Entry(root, textvariable = inputNumber)
input_label.grid(row = 1)
input_entry.grid(row = 1, column = 1)
result_label = tk.Label(root)
result_label.grid(row = 3, columnspan = 4)
 
# drop down setup
dropDownList = ["Celsius", "Fahrenheit"]
drop_down = tk.OptionMenu(root, var, *dropDownList,
                          command = store_temp)
var.set(dropDownList[0])
drop_down.grid(row = 1, column = 2)
 
# button widget
call_convert = partial(call_convert, result_label,
                       inputNumber)
result_button = tk.Button(root, text ="Convert",bg="light blue",
                          command = call_convert)
result_button.grid(row = 2, columnspan = 2)
 

root.mainloop()
