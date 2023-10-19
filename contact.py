import tkinter
from tkinter import ttk
import os
from tkinter import messagebox
import openpyxl
from openpyxl import load_workbook

'''path="C:\\Users\\ANWAR\\CONTACT.xlsx"
wb=load_workbook(filename=path,read_only=False)
ws=wb.active'''

def enter_data():
    name=name_label_entry.get()
    contact=contact_label_entry.get()
    email=Email_label_entry.get()

    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        name = name_label_entry.get()
        contact= contact_label_entry.get()
        email=Email_label_entry.get()
        
        if name and contact:
            title = title_combobox.get()
            #age = age_spinbox.get()
            #ationality = nationality_combobox.get()
            

            
            print("name: ", name, "contact: ", contact)
            print( "Email :",email)
          
            print("------------------------------------------")
            filepath="C:\\Users\\ANWAR\\CONTACT.xlsx"
            if not os.path.exists(filepath):
                workbook=openpyxl.workbook()
                sheet=workbook.active
                heading=["Name","Contact","Email"]
            sheet.append(heading)
            workbook.save(filepath)
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
contact_frame =tkinter.LabelFrame(frame, text="CONTACT BOOK")
contact_frame.grid(row= 0, column=0, padx=20, pady=10)

name_label = tkinter.Label(contact_frame, text="NAME")
name_label.grid(row=0, column=0)
contact_label = tkinter.Label(contact_frame, text="CONATCT NUMBER")
contact_label.grid(row=0, column=1)

name_label_entry = tkinter.Entry(contact_frame)
contact_label_entry = tkinter.Entry(contact_frame)
name_label_entry.grid(row=1, column=0)
contact_label_entry.grid(row=1, column=1)

title_label = tkinter.Label(contact_frame, text="TITLE")
title_combobox = ttk.Combobox(contact_frame, values=["miss", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

''' age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0) '''

'''nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)'''

Email_label = tkinter.Label(contact_frame, text="EMAIL")
Email_label.grid(row=2, column=1)
Email_label_entry = tkinter.Entry(contact_frame)
Email_label_entry.grid(row=3, column=1)

for widget in contact_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
'''courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text= "# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5) '''

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="save data")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "Save Number",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
button = tkinter.Button(frame, text="View", command= enter_data)
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
button = tkinter.Button(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()
