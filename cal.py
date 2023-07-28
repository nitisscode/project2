# import libraries
from tkinter import *
from tkcalendar import *

#creating size color and title 
root=Tk()
root.geometry("400x400")
root.title("Calendar")
root.configure(bg="lightblue")


cal=Calendar(root,setmode="day",date_pattern="dd/mm/yyyy")
cal.pack(padx=15,pady=15)


#function for select the date
def selectDate():
    myDate.config(text=cal.get_date())
    

#button for show the selected date
open_cal=Button(root,text="Show Date",command=selectDate)
open_cal.pack(padx=15,pady=15)


#creating label for display the selected date
myDate=Label(root,text="",font=10)
myDate.configure(bg="lightblue")
myDate.pack(padx=2,pady=2)


root.mainloop()
