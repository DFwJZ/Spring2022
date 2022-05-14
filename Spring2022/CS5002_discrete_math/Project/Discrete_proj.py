"""
    CS5002 Spring 2022
    Discrete Math Project
    Haozhe Zhang
"""

"""
The Program will handle any integer decimal numbers and convert
it into a binary number if the input is positive and to a 12-bit
2's complement number if the input is negative.

@Haozhe Zhang

"""

import tkinter as tk
from tkinter import messagebox

# Function to handle the conversion of the input decimal integer
def decimal_conversion():
    # '-' sign needs to be determined separately from the original input
    check_type = enter_decimal_number.get()[1:]
    if not check_type.isdigit():
        messagebox.showerror("Error", "Please check your input, must be an integer")
    # continue to else statement if the input is a digit (with or without a '-' sign) 
    else:
        decimal_num = int(enter_decimal_number.get())
        if decimal_num < -2048 or decimal_num > 2047:
                messagebox.showwarning("Alert", "The input must be in range [-2048, 2047]")
        else:
            if decimal_num < 0:
                decimal_num = int(~decimal_num ^ 0b111111111111)
            # Get rid of 0b, which is a python notation to represent a bin number   
            binary_num = '{:08b}'.format(decimal_num)
            label_result2["text"] = f"{binary_num} (2)"
        
# init tk as root
root = tk.Tk()
root.title("Binary Number Converter [-2048, 2047]")
##root.resizable(width=75, height=50)

# Set the prompt window resizable 
root.columnconfigure(1, weight=1,minsize=100)
root.rowconfigure(0, weight=1,minsize=75)

# Creating decimal input box
frame_entry = tk.Frame(master=root)
enter_decimal_number = tk.Entry(master=frame_entry, width=10)
label_num = tk.Label(master=frame_entry, text="(10)")

# keep the entered number box to the leftmost edge of its grid cell
# e denotes easter, w denotes west
enter_decimal_number.grid(row=0, column=0, sticky='e')
label_num.grid(row=0, column=1, sticky='w')

# create a button to click on to convert the number
btn_convert = tk.Button(
    master=root,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=decimal_conversion
)
# Display the converted binary number
label_result2 = tk.Label(master=root, text="(2)")


# Place the frame_entry, btn_convert, label_result grid listed from left to right
frame_entry.grid(row=0, column=0, padx=20)
btn_convert.grid(row=0, column=1, pady=20)
label_result2.grid(row=0, column=2, padx=20)


root.mainloop()
