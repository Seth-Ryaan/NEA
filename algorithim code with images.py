#algortihim code with image support

#implemet like button to add to algolist instead of view
from tkinter import *
import random
import os
import datetime
liketotal = 0
algo_list = [0]
comment_value = 3

#-----------------
main_window = Tk()
#main_window.attributes ("-fullscreen", True)

def refresh():
    main_window.destroy()
    os.popen("algorithim code with images.py")

def clock():
    realtime = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=realtime)
    clock_label['text'] = realtime
    main_window.after(1000, clock) # run itself again after 1000 ms

def comment_display():
    if comment_value == 3:  #cat
        comment_window.configure (text = "so cute")

def show_for_you():
    algo_choice = random.choice(algo_list)
    if algo_choice == (1):
        show_cars()
    if algo_choice == (2): #dogs
        show_dog()
    if algo_choice == (3):
        show_cat()
    if algo_choice == (4):
        show_celebrity()
    if algo_choice == (5):
        show_funny()

def show_dog():     #2
    chosen_image = PhotoImage(file = "dog.png")
    image.config (i=chosen_image)           #.config was the key
    like_button.configure (command = like_dog, text = "Like")  #runs like_dog when calling show_dog,  instead of running when button pressed, config = Text seems to fix error, changes function of the button now
    image.pack()
    main_window.mainloop()

def like_dog(): #2
    algo_list.append(2)
    print (algo_list)

def show_funny():   #5
    chosen_image = PhotoImage(file = "total drama camp.png")
    image.config (i=chosen_image)
    like_button.configure (command = like_funny, text = "Like")
    image.pack()
    main_window.mainloop()

def like_funny():     #5
    algo_list.append(5)
    print (algo_list)

def show_cat():     #3
    chosen_image = PhotoImage(file = "cat.png")
    image.config (i=chosen_image)
    comment_display()
    like_button.configure (command = like_cat, text = "Like")
    image.pack()
    main_window.mainloop()

def like_cat():
    algo_list.append(3)
    print (algo_list)

def show_cars():    #1
    chosen_image = PhotoImage(file = "car.png")
    image.config (i=chosen_image)
    like_button.configure (command = like_cars, text = "Like")
    image.pack()
    main_window.mainloop()

def like_cars():
    algo_list.append(1)
    print (algo_list)

def show_celebrity():   #4
    chosen_image = PhotoImage(file = "celebrity.png")
    image.config (i=chosen_image)
    like_button.configure (command = like_celebrity, text = "Like")
    image.pack()
    main_window.mainloop()

def like_celebrity():
    algo_list.append(4)
    print (algo_list)

main_window.title("SETH.COM/HOMEPAGE")
main_window.configure(bg = "#006d85")

chosen_image = PhotoImage(file = "default.png")
image = Label(main_window, i = chosen_image, anchor = "center")

comment_window = Label(main_window, bg = "#F8F0E3",relief = "raised", height = 32, width = 35)
comment_window.place (x=975, y=10)

clock_label = Label(main_window)
clock_label.place (x=100, y=50)

refresh_button=Button(main_window, text="Refresh", fg='black', cursor = "hand2", command = refresh)
refresh_button.place(x=670, y=600)

dog_button=Button(main_window, text ="Dog", fg="black", cursor = "hand2", command = show_dog)
dog_button.place(x=650, y=550)

funny_button=Button(main_window, text ="Funny", fg="black", cursor = "hand2", command = show_funny)
funny_button.place(x=690, y=550)

cat_button=Button(main_window, text ="Cat", fg="black", cursor = "hand2", command = show_cat)
cat_button.place(x=750, y=550)

car_button=Button(main_window, text ="Car", fg="black", cursor = "hand2", command = show_cars)
car_button.place(x=810, y=550)

celebrity_button=Button(main_window, text ="Celebrity", fg="black", cursor = "hand2", command = show_celebrity)
celebrity_button.place(x=890, y=550)

for_you_refresh_button=Button(main_window, text ="For You", fg="black", cursor = "hand2", command = show_for_you)
for_you_refresh_button.place(x=560, y=600)

like_button = Button(main_window, text = "Like", fg="black", cursor = "hand2", command = ())
like_button.place (x=625,y=600)

clock()
image.pack()
main_window.mainloop()
