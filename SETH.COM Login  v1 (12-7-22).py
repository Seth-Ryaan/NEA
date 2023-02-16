from tkinter import *
#----
main_window = Tk()
#----
background_image = PhotoImage(file = "background.png")
logo_image = PhotoImage(file = "seth.com.png")
logo_image_small = logo_image.subsample(2,2)
#----
main_window.title("Seth.com Login")
login_background = Label(main_window, i=background_image, anchor="center")
#----
title_font = (25)
username_label=Label(main_window, text="Username: ", fg='black', bg ='white', font = title_font)
username_entry=Entry(main_window, font = title_font)
password_label=Label(main_window, text="Password: ", fg='black', bg ='white', font = title_font)
password_entry=Entry(main_window, font = title_font, show = "*")
submit_button=Button(main_window, text="Submit", fg='black', cursor = "hand2")
logo_label=Label(main_window, image = logo_image_small)
#----
submit_button.place(x=570, y=550)
password_label.place(rely = .675, relx = .379, anchor = "center")
password_entry.place(rely = .675, relx = .51, anchor = "center")
username_label.place(rely = .6, relx=.3795, anchor ="center")
username_entry.place(rely = .6, relx = .51, anchor = "center")
logo_label.place(x=400, y=50)
#----
login_background.pack()
main_window.mainloop()
