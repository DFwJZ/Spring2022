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


class Roster(Tk):
    def __init__(self):
        # init
        super().__init__()

        self.title("Class Roster for CS5001") # name the window
        self.resizable(height=False, width=False) # create a background canvas
        self.my_canvas = Canvas(self, height=500, width=800, bg="#A0EFC8")
        self.my_canvas.pack(fill="both", expand=True)

        # create a inner frame that consists of all information
        self.main_frame = Frame(self, bg="white")
        self.main_frame.place(relheight=0.5, relwidth=0.77, relx=0.1, rely=0.1)


        self.second_frame = Label(self, bg='grey')
        self.second_frame.place(relx=0.1, rely=0.65)


        # create scrollbar for both vertical and horizontal view
        self.y_scroll = Scrollbar(self.main_frame, orient='vertical')
        self.y_scroll.pack(side=RIGHT, fill=Y)

        self.x_scroll = Scrollbar(self.main_frame, orient='horizontal')
        self.x_scroll.pack(side=BOTTOM, fill=X)

        self.class_roster = ttk.Treeview(self.main_frame, yscrollcommand=self.y_scroll.set,
                                         xscrollcommand=self.x_scroll.set)
        self.class_roster.pack()

        self.y_scroll.config(command=self.class_roster.yview)
        self.x_scroll.config(command=self.class_roster.xview)

        # create headers for class roster
        self.style = ttk.Style()
        # modify the font of headings
        self.style.configure("Treeview.Heading", font=('Garamond', 16))
        self.style.configure("Treeview", font=(
            'Garamond', 16))  # modify the font of body

        self.class_roster['column'] = ("Student_ID", "Student_Name", "Quiz_1",
                                "Quiz_2", "Quiz_3", "Midterm_1", "Final", "Final_Grade")

        self.class_roster.column("#0", width=0,  stretch=NO)
        self.class_roster.column("Student_ID", anchor=CENTER,
                            minwidth=90, width=90, stretch=NO)
        self.class_roster.column("Student_Name", anchor=CENTER,
                            minwidth=150, width=150, stretch=NO)
        self.class_roster.column(
            "Quiz_1", anchor=CENTER, minwidth=90, width=90, stretch=NO)
        self.class_roster.column(
            "Quiz_2", anchor=CENTER, minwidth=90, width=90, stretch=NO)
        self.class_roster.column(
            "Quiz_3", anchor=CENTER, minwidth=90, width=90, stretch=NO)
        self.class_roster.column(
            "Midterm_1", anchor=CENTER, width=90, stretch=NO)
        self.class_roster.column(
            "Final", anchor=CENTER, minwidth=90, width=90, stretch=NO)
        self.class_roster.column(
            "Final_Grade", anchor=CENTER, minwidth=90, width=90, stretch=NO)

        self.class_roster.heading("#0", text="", anchor=CENTER)
        self.class_roster.heading("Student_ID", text="ID", anchor=CENTER)
        self.class_roster.heading("Student_Name", text="Name", anchor=CENTER)
        self.class_roster.heading("Quiz_1", text="Quiz_1", anchor=CENTER)
        self.class_roster.heading("Quiz_2", text="Quiz_2", anchor=CENTER)
        self.class_roster.heading("Quiz_3", text="Quiz_3", anchor=CENTER)
        self.class_roster.heading("Midterm_1", text="Midterm_1", anchor=CENTER)
        self.class_roster.heading("Final", text="Final", anchor=CENTER)
        self.class_roster.heading(
            "Final_Grade", text="Final_Grade", anchor=CENTER)
        
        self.class_roster.pack()
    
        # dummy data
        self.data = [
            ['500101', 'Scooby-doo', '80', '84', '85', '85', '90'],
            ['500102', 'Bart', '90', '81', '83', '87', '86'],
            ['500103', 'Eric', '76', '81', '86', '89', '86'],
            ['500104', 'Morty', '55', '69', '99', '100', '100']

        ]

        # read in dummy data
        global count
        count = 0

        for record in self.data:
            self.class_roster.insert(parent='', index='end', iid=count,
                                text='', values=(record[0], record[1],
                                                record[2], record[3], record[4], record[5],
                                                record[6]))
            count += 1


        # Input a new record
        self.Input_frame = Frame(self.second_frame)
        self.Input_frame.pack(ipadx=1, ipady=1)

        # create input record headings
        self.ID = Label(self.Input_frame, text='ID')
        self.ID.grid(row=0, column=0)

        self.Student_Name = Label(self.Input_frame, text='Student_Name')
        self.Student_Name.grid(row=0, column=1)

        self.Quiz_1 = Label(self.Input_frame, text='Quiz_1')
        self.Quiz_1.grid(row=0, column=2)

        self.Quiz_2 = Label(self.Input_frame, text='Quiz_2')
        self.Quiz_2.grid(row=0, column=3)

        self.Quiz_3 = Label(self.Input_frame, text='Quiz_3')
        self.Quiz_3.grid(row=0, column=4)

        self.Midterm_1 = Label(self.Input_frame, text='Midterm_1')
        self.Midterm_1.grid(row=0, column=5)

        self.Final = Label(self.Input_frame, text='Final')
        self.Final.grid(row=0, column=6)

        # Entry box
        self.ID_entry = Entry(self.Input_frame, width=8)
        self.ID_entry.grid(row=1, column=0)

        self.Student_Name_entry = Entry(self.Input_frame, width=8)
        self.Student_Name_entry.grid(row=1, column=1)

        self.Quiz_1_entry = Entry(self.Input_frame, width=8)
        self.Quiz_1_entry.grid(row=1, column=2)

        self.Quiz_2_entry = Entry(self.Input_frame, width=8)
        self.Quiz_2_entry.grid(row=1, column=3)

        self.Quiz_3_entry = Entry(self.Input_frame, width=8)
        self.Quiz_3_entry.grid(row=1, column=4)

        self.Midterm_1_entry = Entry(self.Input_frame, width=8)
        self.Midterm_1_entry.grid(row=1, column=5)

        self.Final_entry = Entry(self.Input_frame, width=8)
        self.Final_entry.grid(row=1, column=6)

        # Add New Student Button
        self.add_new_btn = Button(self, text="Add New Student",
                                command=self.add_new_student,
                                padx=10, pady=5, fg="black", bg="#A0EFC8")
        self.add_new_btn.pack(side=TOP)

        # # Create openFile button to allow user to import exisiting roster
        # self.openFile = Button(self, text='Open File',  padx=10,
        #                        pady=5, fg='black', bg="#A0EFC8", command=self.open_file)
        # self.openFile.pack(side=RIGHT)

        # # save modified file to a new or existing directory 
        # self.exportFile = Button(self, text="Export Roster", padx=10,
        #                          pady=5, fg="black", bg="#A0EFC8", command=self.export_file)
        # self.exportFile.pack(side=RIGHT)

        # add a row deleting option
        self.delete_btn = Button(self, text='Delete', fg="red", padx=10,
                                 pady=5, bg="#A0EFC8", command=self.delete)

        self.delete_btn.pack(side=LEFT)

        # implement a sort method to sort columns by clicking
        self.columns = self.class_roster['column']
        self.treeview = self.class_roster
        for col in self.columns:
            self.treeview.heading(col, text=col, command=lambda _col=col:
                         self.treeview_sort_column(self.treeview, _col, False))

        # add a menu
        menubar = Menu(self)
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.clear_treeview)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save as...", command=self.export_file)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.close_window)
        file_menu.add_separator()
        menubar.add_cascade(label='File', menu=file_menu)
        self.config(menu=menubar)

    def add_new_student(self):
    #Input a new record
        global count

        self.class_roster.insert(parent='', index='end', iid=count,
                            text='',
                                 values=(self.ID_entry.get(), self.Student_Name_entry.get(),
                                         self.Quiz_1_entry.get(), self.Quiz_2_entry.get(), self.Quiz_3_entry.get(),
                                         self.Midterm_1_entry.get(), self.Final_entry.get()))
        count += 1

        self.ID_entry.delete(0, END)
        self.Student_Name_entry.delete(0, END)
        self.Quiz_1_entry.delete(0, END)
        self.Quiz_2_entry.delete(0, END)
        self.Quiz_3_entry.delete(0, END)
        self.Midterm_1_entry.delete(0, END)
        self.Final_entry.delete(0, END)

    # Open file for csv or all kinds of files
    def open_file(self):
        # clear existed records
        for item in self.class_roster.get_children():
            self.class_roster.delete(item)

        # allow csv or other(*) files to be input
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
                self.class_roster.insert(parent='', index='end', iid=i, text='',
                                    values=row)
                i = i + 1
            # assign the i back to global count to make sure the iid is in order
            global count
            count = i
        
    # Export the completed roster to a file
    def export_file(self):
        lst = []
        name = asksaveasfilename()
        with open(name, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for row_id in self.class_roster.get_children():
                row = self.class_roster.item(row_id, 'values')
                lst.append(row)
            for row in lst:
                csvwriter.writerow(row)

    # delete a item
    def delete(self):
        selected_item = self.class_roster.selection()
        for s in selected_item:
            self.class_roster.delete(s)

    # sort the column by clicking on columns
    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, text=col, command=lambda _col=col:
                self.treeview_sort_column(tv, _col, not reverse))

    # clear existed records
    def clear_treeview(self):
        for item in self.class_roster.get_children():
            self.class_roster.delete(item)

    # close roster window
    def close_window(self):
        self.destroy()

    # calculating the final grade
    # grade weighs 
if __name__ == "__main__":
    roster = Roster()
    roster.mainloop()
