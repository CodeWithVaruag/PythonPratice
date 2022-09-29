from tkinter import *

frame = Tk()
# calling TK library

frame.title("login Page")
# setting title for login page

frame.geometry('1850x900')
# setting length and breadth of frame

# the label for user_name
user_name = Label(frame,  text="Username",font="normal").place(x=600, y=250)

# the label for user_password
user_password = Label(frame,text="Password",font="normal",textvariable="passw_var").place(x=600, y=310)

login_button = Button(frame,text="Login",bg="yellow",height=1,width=5,font="normal",command=frame.destroy).place(x=700,y=400)

user_name_input_area = Entry(frame, width=20,font="normal").place(x=740,y=255)

user_password_entry_area = Entry(frame,width=20,font="normal").place(x=740,y=315)

frame.mainloop()
# adding button to the frame

# img = PhotoImage(file="loginimg.jpg")
# backgroundlabel = Label(image="img")
# backgroundlabel.pack()



frame.mainloop()