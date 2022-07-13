from tkinter import *
from PIL import ImageTk, Image

root = Tk()     # initializing root window
root.title("Sam's Discount Shoes")
root.geometry('1500x1000')


first_frame = Frame(root, pady=25)
first_frame.pack()
second_frame = Frame(root)
second_frame.pack()
third_frame = Frame(root)
third_frame.pack()
fourth_frame = Frame(root)
fourth_frame.pack()


logo = Image.open("logo.jpg")
resized = logo.resize((1200, 100), Image.LANCZOS)
new_logo = ImageTk.PhotoImage(resized)
Label(first_frame, image=new_logo).pack()

first_label = Label(first_frame, text="Welcome to Sam's Discount Shoes", font="Times_New_Roman, 30")
first_label.pack()

second_label = Label(first_frame, text="Shop our Selection of Shoes!", font="Times_New_Roman, 15")
second_label.pack()


img1 = Image.open("AirForceOnes.jpg")
resized = img1.resize((200, 200), Image.LANCZOS)
new_img1 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img1).grid(row=0, column=0, padx=50)


img2 = Image.open("Vans.jpg")
resized = img2.resize((200, 200), Image.LANCZOS)
new_img2 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img2).grid(row=0, column=1, padx=50)

img3 = Image.open("ultraboost.jpg")
resized = img3.resize((200, 200), Image.LANCZOS)
new_img3 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img3).grid(row=0, column=2, padx=50)

img4 = Image.open("reebok.jpg")
resized = img4.resize((200, 200), Image.LANCZOS)
new_img4 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img4).grid(row=0, column=3, padx=50)


clicked1 = StringVar()
clicked1.set("Quantity")

drop1 = OptionMenu(second_frame, clicked1, "1", "2", "3", "4", "5")
drop1.grid(row=2, column=0)

clicked2 = StringVar()
clicked2.set("Quantity")

drop2 = OptionMenu(second_frame, clicked2, "1", "2", "3", "4", "5")
drop2.grid(row=2, column=1)

clicked3 = StringVar()
clicked3.set("Quantity")

drop3 = OptionMenu(second_frame, clicked3, "1", "2", "3", "4", "5")
drop3.grid(row=2, column=2)

clicked4 = StringVar()
clicked4.set("Quantity")

drop4 = OptionMenu(second_frame, clicked4, "1", "2", "3", "4", "5")
drop4.grid(row=2, column=3)


img5_label = Label(second_frame, text="Nike $59.99", font="Times_New_Roman, 20")
img5_label.grid(row=1, column=0)
img6_label = Label(second_frame, text="Vans $59.99", font="Times_New_Roman, 20")
img6_label.grid(row=1, column=1)
img7_label = Label(second_frame, text="Adidas $59.99", font="Times_New_Roman, 20")
img7_label.grid(row=1, column=2)
img8_label = Label(second_frame, text="Reebok $59.99", font="Times_New_Roman, 20")
img8_label.grid(row=1, column=3)

img5 = Image.open("puma.jpg")
resized = img5.resize((200, 200), Image.LANCZOS)
new_img5 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img5).grid(row=3, column=0, padx=50)


img6 = Image.open("newbalance.jpg")
resized = img6.resize((200, 200), Image.LANCZOS)
new_img6 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img6).grid(row=3, column=1, padx=50)

img7 = Image.open("converse.jpg")
resized = img7.resize((200, 200), Image.LANCZOS)
new_img7 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img7).grid(row=3, column=2, padx=50)

img8 = Image.open("underarmour.jpg")
resized = img8.resize((200, 200), Image.LANCZOS)
new_img8 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img8).grid(row=3, column=3, padx=50)

img1_label = Label(second_frame, text="Puma $59.99", font="Times_New_Roman, 20")
img1_label.grid(row=4, column=0)
img2_label = Label(second_frame, text="New Balance $59.99", font="Times_New_Roman, 20")
img2_label.grid(row=4, column=1)
img3_label = Label(second_frame, text="Converse $59.99", font="Times_New_Roman, 20")
img3_label.grid(row=4, column=2)
img4_label = Label(second_frame, text="Under Armour $59.99", font="Times_New_Roman, 20")
img4_label.grid(row=4, column=3)


clicked5 = StringVar()
clicked5.set("Quantity")

drop5 = OptionMenu(second_frame, clicked1, "1", "2", "3", "4", "5")
drop5.grid(row=5, column=0)

clicked6 = StringVar()
clicked6.set("Quantity")

drop6 = OptionMenu(second_frame, clicked2, "1", "2", "3", "4", "5")
drop6.grid(row=5, column=1)

clicked7 = StringVar()
clicked7.set("Quantity")

drop7 = OptionMenu(second_frame, clicked3, "1", "2", "3", "4", "5")
drop7.grid(row=5, column=2)

clicked8 = StringVar()
clicked8.set("Quantity")

drop8 = OptionMenu(second_frame, clicked4, "1", "2", "3", "4", "5")
drop8.grid(row=5, column=3)


def checkout():
    check_out = Tk()
    check_out.title("Checkout")
    check_out.geometry('1500x1000')

    frame = Frame(check_out)
    frame.pack()
    label = Label(frame, text="Welcome to Checkout", font="Times_New_Roman, 20")
    label.pack()

    check_out.mainloop()


Button(fourth_frame, text="Checkout", command=checkout).grid(row=1, column=5)


root.mainloop()
