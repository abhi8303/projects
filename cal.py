from tkinter import *
from tkcalendar import Calendar

def get_date():
    date_label.config(text="Selected date: " + cal.get_date())
root = Tk()
root.title("Calendar with Button")
root.geometry("300x300")
cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=20)
date_label = Label(root, text="Selected date: ")
date_label.pack(pady=10)
select_button = Button(root, text="Select Date", command=get_date)
select_button.pack(pady=10)
root.mainloop()
