import tkinter
screen = tkinter.Tk()
screen.title("first")
screen.minsize(height=600, width=500)


# Label

# myLabel = tkinter.Label(text="My First Label", font=("Arial", 22, "bold"), background="aqua", border=130)
# myLabel.pack()

# myLabel["text"] = "Vikas Singh Label"  : to change label via this method.
# myLabel.config(text="new Label")       : to change label via this method.


# def button_clicked():
#     print("I am clicked")
#
#
# button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()

# when button clicked show label as button clicked.

# def button_clicked():
#     mylabel = tkinter.Label(text="Button Clicked", font=("Arial", 22, "bold"), background="red", border=130)
#     mylabel.pack()


# whn button clicked whatever written in input written in label.
input_data = tkinter.Entry(width=15,string = "write your name")
input_data.pack()


def button_clicked():
    mylabel = tkinter.Label(text=input_data.get(), font=("Arial", 22, "bold"), background="red", border=130)
    mylabel.pack()


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()
screen.mainloop()
