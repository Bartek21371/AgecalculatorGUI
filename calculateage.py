import tkinter as tk
from tkinter import *
from datetime import date
today = date.today() #add time today
#Window settings
win = tk.Tk()
win.title("Calculator age")
win.geometry('200x250')
win.iconbitmap('calcx.ico')
win.resizable(False,False)   

#Captions
day_text = tk.Label(win,text="Day") #day
day_text.place(x=45,y=10)
month_text = tk.Label(win,text="Month") #month
month_text.place(x=74,y=10)
year_text = tk.Label(win,text="Year") #year
year_text.place(x=115,y=10) 
your_text = tk.Label(win,text="Your age:") #your age:|result|
your_text.place(x=45,y=140)

#Entry data window
day_win = tk.Entry(win,width=2) #day
day_win.place(x=50,y=45)
month_win = tk.Entry(win,width=2) #month
month_win.place(x=82,y=45)
year_win = tk.Entry(win,width=4) #year
year_win.place(x=115,y=45)

#Get age operation def
def get_age():
    day=int(day_win.get())
    month=int(month_win.get())
    year=int(year_win.get())
    age =today.year-year-((today.month, today.day)<(month,day))
    Age.config(state='normal')
    Age.delete('1.0', tk.END)
    Age.insert(tk.END,age)
    Age.config(state='disabled')
#Button to show result
Result = tk.Button(win,text="Show age!",command=get_age)
Result.place(x=60,y=90)          
#Show result
Age = tk.Text(win,width=3,height=0,state="disabled")    
Age.place(x=105,y=143)


#Style config
win.configure(bg="grey") #win config

day_text.configure(bg="grey",fg="white",font=('Helvetica bold', 10)) #text config
month_text.configure(bg="grey",fg="white",font=('Helvetica bold', 10))
year_text.configure(bg="grey",fg="white",font=('Helvetica bold', 10))
your_text.configure(bg="grey",fg="white",font=('Helvetica bold', 10))

day_win.configure(bg="black",fg="white",font=('Helvetica bold', 10)) #input frame config
month_win.configure(bg="black",fg="white",font=('Helvetica bold', 10))
year_win.configure(bg="black",fg="white",font=('Helvetica bold', 10))

Age.configure(bg="black",fg="green",font=('Helvetica bold', 10)) #output frame config

Result.configure(bg="black",fg="white",font=('Helvetica bold', 10)) #button to action config

win.mainloop()