# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.forward(200)
# timmy.back(400)
# my_screen = Screen()
# my_screen.exitonclick()   # exit on click
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("city_name",["Jaipur", "Bikaner", "Ajmer", "Jodhpur", "Kota"])
table.add_column("s_name",["Vikas", "Nisha", "Vanya", "Mohit", "Surya"])
table.align = 'l'
print(table)
