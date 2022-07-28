"""This program is called Sam's Discount Shoes. It is an application where you can purchase low price
shoes and order them."""

# importing modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# initializing root window, setting title, background color
root = Tk()
root.title("Sam's Discount Shoes")      # title of the Window
root.geometry('1500x1000')      # setting window dimensions
root.resizable(width=True, height=True)     # making the window resizable
root.configure(bg='black')      # configuring the window with a black background

# setting frames for the root window
first_frame = Frame(root)
first_frame.configure(bg='black')       # making all frame black background
first_frame.pack()
second_frame = Frame(root)
second_frame.configure(bg='black')
second_frame.pack()
third_frame = Frame(root)
third_frame.configure(bg='black')
third_frame.pack()
fourth_frame = Frame(root)
fourth_frame.configure(bg='black')
fourth_frame.pack()

# adding logo image
logo = Image.open("logo.jpg")       # creating logo with logo.jpg
resized = logo.resize((1200, 100), Image.LANCZOS)           # resizing logo to fit the way I want
new_logo = ImageTk.PhotoImage(resized)      # Resized
Label(first_frame, image=new_logo).pack()

# adding title header text, background color, and font
first_label = Label(first_frame, text="Welcome to Sam's Discount Shoes", font="Times_New_Roman, 30", bg='black')
first_label.pack()
second_label = Label(first_frame, text="Shop our Selection of Shoes!", font="Times_New_Roman, 15", bg='black')
second_label.pack()


# configuring images of shoes
img1 = Image.open("AirForceOnes.jpg")
resized = img1.resize((200, 200), Image.LANCZOS)
new_img1 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img1).grid(row=0, column=0, padx=50)  # padding each image in a grid formation for space

# configuring images of shoes
img2 = Image.open("Vans.jpg")
resized = img2.resize((200, 200), Image.LANCZOS)
new_img2 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img2).grid(row=0, column=1, padx=50)

# configuring images of shoes
img3 = Image.open("ultraboost.jpg")
resized = img3.resize((200, 200), Image.LANCZOS)
new_img3 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img3).grid(row=0, column=2, padx=50)

# configuring images of shoes
img4 = Image.open("reebok.jpg")
resized = img4.resize((200, 200), Image.LANCZOS)
new_img4 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img4).grid(row=0, column=3, padx=50)

# configuring SpinBoxes for shoe amount selection
currentValue1 = StringVar(value='0')        # making default value say 0
spinBox1 = Spinbox(second_frame, from_=0, to=10, textvariable=currentValue1, bg='black')  # values from 0 to 10
spinBox1.grid(row=2, column=0)

# configuring SpinBoxes for shoe amount selection
currentValue2 = StringVar(value='0')    # making default value say 0
spinBox2 = Spinbox(second_frame, from_=0, to=10, textvariable=currentValue2, bg='black')  # values from 0 to 10
spinBox2.grid(row=2, column=1)

# configuring SpinBoxes for shoe amount selection
currentValue3 = StringVar(value='0')    # making default value say 0
spinBox3 = Spinbox(second_frame, from_=0, to=10, textvariable=currentValue3, bg='black')  # values from 0 to 10
spinBox3.grid(row=2, column=2)

# configuring SpinBoxes for shoe amount selection
currentValue4 = StringVar(value='0')    # making default value say 0
spinBox4 = Spinbox(second_frame, from_=0, to=10, textvariable=currentValue4, bg='black')  # values from 0 to 10
spinBox4.grid(row=2, column=3)

# Labeling the shoes with prices
img5_label = Label(second_frame, text="Nike $30", font="Times_New_Roman, 20", bg='black')  # giving all shoes a label
img5_label.grid(row=1, column=0)
img6_label = Label(second_frame, text="Vans $30", font="Times_New_Roman, 20", bg='black')  # giving all shoes a label
img6_label.grid(row=1, column=1)
img7_label = Label(second_frame, text="Adidas $30", font="Times_New_Roman, 20", bg='black')  # giving all shoes a label
img7_label.grid(row=1, column=2)
img8_label = Label(second_frame, text="Reebok $30", font="Times_New_Roman, 20", bg='black')  # giving all shoes a label
img8_label.grid(row=1, column=3)

# configuring images of shoes
img5 = Image.open("puma.jpg")
resized = img5.resize((200, 200), Image.LANCZOS)
new_img5 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img5).grid(row=3, column=0, padx=50)

# configuring images of shoes
img6 = Image.open("newbalance.jpg")
resized = img6.resize((200, 200), Image.LANCZOS)
new_img6 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img6).grid(row=3, column=1, padx=50)

# configuring images of shoes
img7 = Image.open("converse.jpg")
resized = img7.resize((200, 200), Image.LANCZOS)
new_img7 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img7).grid(row=3, column=2, padx=50)

# configuring images of shoes
img8 = Image.open("underarmour.jpg")
resized = img8.resize((200, 200), Image.LANCZOS)
new_img8 = ImageTk.PhotoImage(resized)
Label(second_frame, image=new_img8).grid(row=3, column=3, padx=50)

# Labeling the shoes with prices
img1_label = Label(second_frame, text="Puma $30", font="Times_New_Roman, 20", bg='black')
img1_label.grid(row=4, column=0)
img2_label = Label(second_frame, text="New Balance $30", font="Times_New_Roman, 20", bg='black')
img2_label.grid(row=4, column=1)
img3_label = Label(second_frame, text="Converse $30", font="Times_New_Roman, 20", bg='black')
img3_label.grid(row=4, column=2)
img4_label = Label(second_frame, text="Under Armour $30", font="Times_New_Roman, 20", bg='black')
img4_label.grid(row=4, column=3)


# configuring SpinBoxes for shoe amount selection
currentValue5 = StringVar(value='0')
spinBox5 = Spinbox(second_frame, from_=0, to=10, textvariable=currentValue5, bg='black')
spinBox5.grid(row=5, column=0)

# configuring SpinBoxes for shoe amount selection
currentValue6 = StringVar(value='0')
spinBox6 = Spinbox(second_frame, from_=0, to=10, textvariable=currentValue6, bg='black')
spinBox6.grid(row=5, column=1)

# configuring SpinBoxes for shoe amount selection
currentValue7 = StringVar(value='0')
spinBox7 = Spinbox(second_frame, from_=0, to=10, textvariable=currentValue7, bg='black')
spinBox7.grid(row=5, column=2)

# configuring SpinBoxes for shoe amount selection
currentValue8 = StringVar(value='0')
spinBox8 = Spinbox(second_frame, from_=0, to=10, textvariable=currentValue8, bg='black')
spinBox8.grid(row=5, column=3)


# defining Total cost of the shoes. This function calculates the total price
def Total():
    totalCost = (int(currentValue1.get())+int(currentValue2.get())+int(currentValue3.get())+int(currentValue4.get())+
              int(currentValue5.get()) +int(currentValue6.get())+int(currentValue7.get())+int(currentValue8.get()))*30   # all values are added and multiplied by price
    global totalLabel
    totalLabel = Label(second_frame, text="Total: $"+str(totalCost), bg='black')    # creating label for total
    totalLabel.grid(row=6, column=2)


# defining the clear button. This function clears the order
def ClearButton():
    global currentValue1        # making this a global variable
    currentValue1 = StringVar(value='0')        # clear Button sets value back to 0
    spinBox1.config(textvariable=currentValue1)     # spin boxes are set back to 0
    global currentValue2        # making this a global variable
    currentValue2 = StringVar(value='0')
    spinBox2.config(textvariable=currentValue2)
    global currentValue3        # making this a global variable
    currentValue3 = StringVar(value='0')
    spinBox3.config(textvariable=currentValue3)
    global currentValue4        # making this a global variable
    currentValue4 = StringVar(value='0')
    spinBox4.config(textvariable=currentValue4)
    global currentValue5        # making this a global variable
    currentValue5 = StringVar(value='0')
    spinBox5.config(textvariable=currentValue5)
    global currentValue6        # making this a global variable
    currentValue6 = StringVar(value='0')
    spinBox6.config(textvariable=currentValue6)
    global currentValue7        # making this a global variable
    currentValue7 = StringVar(value='0')
    spinBox7.config(textvariable=currentValue7)
    global currentValue8        # making this a global variable
    currentValue8 = StringVar(value='0')
    spinBox8.config(textvariable=currentValue8)
    try:
        totalLabel.destroy()        # total label is destroyed and set back to 0
    except Exception as ex:
        pass


# defining the order button. This function orders your shoes and sends you to checkout
def order():
    # defining variables for each value of spin box
    one = int(currentValue1.get())
    two = int(currentValue2.get())
    three = int(currentValue3.get())
    four = int(currentValue4.get())
    five = int(currentValue5.get())
    six = int(currentValue6.get())
    seven = int(currentValue7.get())
    eight = int(currentValue8.get())
    # validating entry data
    if one > 0 or two > 0 or three > 0 or four > 0 or five > 0 or six > 0 or seven > 0 or eight > 0:
        check_out = Tk()        # creates new checkout window
        check_out.title("Checkout")     # window is named checkout
        check_out.geometry('1500x1000')     # configuring size of window
        check_out.configure(bg='black')  # configuring the background color

        # creating frames for the window
        first_frame = Frame(check_out, bg='black')      # making frames black background
        first_frame.pack()
        second_frame = Frame(check_out, bg='black')
        second_frame.pack()

        # Labeling the window with Headers
        Label(first_frame, font="Times_New_Roman 40", bg='black', text='Welcome to Checkout').grid(row=0, column=0)
        Label(first_frame, font="Times_New_Roman 40", bg='black', text='Please Enter Your Details Below').grid(row=1, column=0)

        # Name entry section
        Label(second_frame, font="Times_New_Roman 20", bg='black', text='Name:').grid(row=0, column=0)
        global name_entry
        name_entry = Entry(second_frame)
        name_entry.focus_set()
        name_entry.grid(row=0, column=1)

        # Address entry section
        Label(second_frame, font="Times_New_Roman 20", bg='black', text='Address:').grid(row=1, column=0)
        global address_entry
        address_entry = Entry(second_frame)
        address_entry.focus_set()
        address_entry.grid(row=1, column=1)

        # Email entry section
        Label(second_frame, font="Times_New_Roman 20", bg='black', text='Email:').grid(row=2, column=0)
        global email_entry
        email_entry = Entry(second_frame)
        email_entry.focus_set()
        email_entry.grid(row=2, column=1)
    else:
        #  error message is displayed if no shoe is selected
        messagebox.showerror('Error', 'Please select a shoe')

    # defining the submit button. This function submits your information
    def Submit():
        # naming variables to be used for input validation
        n = name_entry.get()
        a = address_entry.get()
        e = email_entry.get()
        special_character = ['@', '.']
        if len(n and a and e) == 0:     # if length of any entries are 0 then error
            messagebox.showerror('Error', 'Please enter the proper information.')
        elif any(ch.isdigit() for ch in n):     # if there are any numbers in the name then error
            messagebox.showerror('Error', 'Name cannot have numbers')
        elif not any(ch in special_character for ch in e):  # if there is no @ or . in email then error
            messagebox.showerror('Error', 'Invalid email address')
        else:
            root.destroy()      # Submit button destroys the root window
            check_out.destroy()     # submit button destroys the checkout window
            thank_you = Tk()        # creates thank you window
            thank_you.title("Thank you for your Order")
            thank_you.geometry('1500x1000')
            thank_you.resizable(width=True, height=True)
            thank_you.configure(bg='black')

            # creating frame
            thank_frame = Frame(thank_you, bg='black')
            thank_frame.pack()

            # Header for the Window
            Label(thank_frame, font='Times_New_Roman 40', text="Thank you for shopping at Sam's Discount Shoes", bg='black').grid(row=0, column=0)

            # Exit button to close application
            Button(thank_frame, text='Exit', bg='black', command=exit).grid(row=1, column=0)

    # defining the back button. This function allows you to go back to the root window
    def Back():
        check_out.destroy()     # the back button destroys the checkout window and goes back to the root

    # Configuring Buttons
    Button(second_frame, text='Submit', bg='black', command=Submit).grid(row=3, column=1)
    Button(second_frame, text='Back', bg='black', command=Back).grid(row=3, column=0)

# Defining the Exit Button. This button allows you to exit the application.
def exitButton():
    exit()


# Configuring buttons
exitButton = Button(second_frame, text='Exit', command=exitButton, bg='black')
exitButton.grid(row=8, column=1)
orderButton = Button(second_frame, text='Order', command=order, bg='black')
orderButton.grid(row=7, column=2)
clearButton = Button(second_frame, text='Clear Oder', command=ClearButton, bg='black')
clearButton.grid(row=7, column=1)
totalButton = Button(second_frame, text='Total', command=Total, bg='black')
totalButton.grid(row=6, column=1)

# Infinite loop to run GUI
root.mainloop()
