"""
Roster using tkinter
completed
1. create the main frame 
2. add widgets that are buttons adding new and exporting
3. add adding functions
4. add delete function
*. add sort functions https://stackoverflow.com/questions/1966929/tk-treeview-column-sort/1967793#1967793
*. import a csv file
5. exporting function 
"""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import csv

# init
root = Tk()
# name the window
root.title("Class Roster for CS5001")
# create a background canvas
root.resizable(height=False, width=False)
my_canvas = Canvas(root, height=500, width=800, bg="#A0EFC8")
my_canvas.pack(fill="both", expand=True)
# create a inner frame that consists of all information
main_frame = Frame(root, bg="white")
main_frame.place(relheight=0.5, relwidth=0.77, relx=0.1, rely=0.1)





# create scrollbar for both vertical and horizontal view
y_scroll = Scrollbar(main_frame, orient='vertical')
y_scroll.pack(side=RIGHT, fill=Y)

x_scroll = Scrollbar(main_frame, orient='horizontal')
x_scroll.pack(side=BOTTOM, fill=X)


class_roster = ttk.Treeview(main_frame, yscrollcommand=y_scroll.set,
                            xscrollcommand=x_scroll.set)
class_roster.pack()

y_scroll.config(command=class_roster.yview)
x_scroll.config(command=class_roster.xview)

# create headers for class roster
style = ttk.Style()
# modify the font of headings
style.configure("Treeview.Heading", font=('Garamond', 16))
style.configure("Treeview", font=('Garamond', 16))  # modify the font of body

class_roster['column'] = ("Student_ID", "Student_Name", "Quiz_1",
                          "Quiz_2", "Quiz_3", "Midterm_1", "Final")

class_roster.column("#0", width=0,  stretch=NO)
class_roster.column("Student_ID", anchor=CENTER,
                    minwidth=90, width=90, stretch=NO)
class_roster.column("Student_Name", anchor=CENTER,
                    minwidth=150, width=150, stretch=NO)
class_roster.column("Quiz_1", anchor=CENTER, minwidth=90, width=90, stretch=NO)
class_roster.column("Quiz_2", anchor=CENTER, minwidth=90, width=90, stretch=NO)
class_roster.column("Quiz_3", anchor=CENTER, minwidth=90, width=90, stretch=NO)
class_roster.column("Midterm_1", anchor=CENTER, width=90, stretch=NO)
class_roster.column("Final", anchor=CENTER, minwidth=90, width=90, stretch=NO)

class_roster.heading("#0", text="", anchor=CENTER)
class_roster.heading("Student_ID", text="ID", anchor=CENTER)
class_roster.heading("Student_Name", text="Name", anchor=CENTER)
class_roster.heading("Quiz_1", text="Quiz_1", anchor=CENTER)
class_roster.heading("Quiz_2", text="Quiz_2", anchor=CENTER)
class_roster.heading("Quiz_3", text="Quiz_3", anchor=CENTER)
class_roster.heading("Midterm_1", text="Midterm_1", anchor=CENTER)
class_roster.heading("Final", text="Final", anchor=CENTER)
class_roster.pack()

# dummy data
data = [
    ['500101', 'Scooby-doo', '80', '84', '85', '85', '90'],
    ['500102', 'Bart', '90', '81', '83', '87', '86'],
    ['500103', 'Eric', '76', '81', '86', '89', '86'],
    ['500104', 'Morty', '55', '69', '99', '100', '100']

]

# read in dummy data
global count
count = 0

for record in data:
    class_roster.insert(parent='', index='end', iid=count,
                        text='', values=(record[0], record[1],
                                         record[2], record[3], record[4], record[5],
                                         record[6]))
    count += 1


# Input a new record
Input_frame = Frame(second_frame)
Input_frame.pack(ipadx=1, ipady=1)

# create input record headings
ID = Label(Input_frame, text='ID')
ID.grid(row=0, column=0)

Student_Name = Label(Input_frame, text='Student_Name')
Student_Name.grid(row=0, column=1)

Quiz_1 = Label(Input_frame, text='Quiz_1')
Quiz_1.grid(row=0, column=2)

Quiz_2 = Label(Input_frame, text='Quiz_2')
Quiz_2.grid(row=0, column=3)

Quiz_3 = Label(Input_frame, text='Quiz_3')
Quiz_3.grid(row=0, column=4)

Midterm_1 = Label(Input_frame, text='Midterm_1')
Midterm_1.grid(row=0, column=5)

Final = Label(Input_frame, text='Final')
Final.grid(row=0, column=6)

# Entry box
ID_entry = Entry(Input_frame, width=8)
ID_entry.grid(row=1, column=0)

Student_Name_entry = Entry(Input_frame, width=8)
Student_Name_entry.grid(row=1, column=1)

Quiz_1_entry = Entry(Input_frame, width=8)
Quiz_1_entry.grid(row=1, column=2)

Quiz_2_entry = Entry(Input_frame, width=8)
Quiz_2_entry.grid(row=1, column=3)

Quiz_3_entry = Entry(Input_frame, width=8)
Quiz_3_entry.grid(row=1, column=4)

Midterm_1_entry = Entry(Input_frame, width=8)
Midterm_1_entry.grid(row=1, column=5)

Final_entry = Entry(Input_frame, width=8)
Final_entry.grid(row=1, column=6)


# Input a new record
def add_new_student():

    global count

    class_roster.insert(parent='', index='end', iid=count,
                        text='',
                        values=(ID_entry.get(), Student_Name_entry.get(),
                                Quiz_1_entry.get(), Quiz_2_entry.get(), Quiz_3_entry.get(),
                                Midterm_1_entry.get(), Final_entry.get()))
    count += 1

    ID_entry.delete(0, END)
    Student_Name_entry.delete(0, END)
    Quiz_1_entry.delete(0, END)
    Quiz_2_entry.delete(0, END)
    Quiz_3_entry.delete(0, END)
    Midterm_1_entry.delete(0, END)
    Final_entry.delete(0, END)


# Add New Student Button
add_new_btn = Button(root, text="Add New Student",
                     command=add_new_student,
                     padx=10, pady=5, fg="black", bg="#A0EFC8")
add_new_btn.pack(side=TOP)


# Open file for csv or all kinds of files
def open_file():
    # clear existed records
    for item in class_roster.get_children():
        class_roster.delete(item)

    filename = filedialog.askopenfilename(
        initialdir="/", title='Select File',
        filetypes=(
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )
    )

    with open(filename) as myfile:
        csvread = csv.reader(myfile, delimiter=',')
        i = 0
        for row in csvread:
            class_roster.insert(parent='', index='end', iid=i, text='',
                                values=row)
            i = i + 1
        # assign the i back to global count to make sure the iid is in order
        global count
        count = i
# # Create openFile button to allow user to import exisiting roster
# openFile = tk.Button(root, text='Open File',  padx=10,
#                      pady=5, fg='black', bg="#A0EFC8", command=open_file)
# openFile.pack(side=RIGHT)


# Export the completed roster to a file
def export_file():
    lst = []
    name = asksaveasfilename()
    with open(name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row_id in class_roster.get_children():
            row = class_roster.item(row_id, 'values')
            lst.append(row)
        for row in lst:
            csvwriter.writerow(row)


# exportFile = tk.Button(root, text="Export Roster", padx=10,
#                        pady=5, fg="black", bg="#A0EFC8", command=exportFile)
# exportFile.pack(side=RIGHT)


# delete a item
def delete():
    selected_item = class_roster.selection()[0]
    class_roster.delete(selected_item)


delete_btn = Button(root, text='Delete', fg="red", padx=10,
                    pady=5, bg="#A0EFC8", command=delete)

delete_btn.pack(side=LEFT)

# sort the column by clicking on columns


def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    # reverse sort next time
    tv.heading(col, text=col, command=lambda _col=col:
               treeview_sort_column(tv, _col, not reverse))


columns = class_roster['column']
treeview = class_roster
for col in columns:
    treeview.heading(col, text=col, command=lambda _col=col:
                     treeview_sort_column(treeview, _col, False))

# clear existed records


def clear_treeview():
    for item in class_roster.get_children():
        class_roster.delete(item)

# close roster window


def close_window():
    root.destroy()


# add a menu
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=clear_treeview)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save as...", command=export_file)
file_menu.add_separator()
file_menu.add_command(label="Close", command=close_window)

file_menu.add_separator()

menubar.add_cascade(label='File', menu=file_menu)

root.config(menu=menubar)
root.mainloop()
