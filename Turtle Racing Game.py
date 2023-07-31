import turtle as tr
import random
screen = tr.Screen()
turtle_set=[]
screen.setup(500,400)
user_bet=screen.textinput(title='Make you choice',prompt="Which tutle will win the Race?Enter a choice:")
print(user_bet)
colour=["red","orange","yellow","green","blue","purple"]
ang=[60,40,20,0,-20,-40]
x_ax = -230
for i in range(6):
    new_turtle = tr.Turtle(shape="turtle")
    new_turtle.color(colour[i])
    new_turtle.penup()
    new_turtle.goto(x=x_ax,y=ang[i])
    turtle_set.append(new_turtle)

if user_bet:
    race_on=True

while race_on:
    for tur in turtle_set:
        if tur.xcor()>210:
            win_turtle=tur.pencolor()
            if win_turtle==user_bet:
                print(f"You Won..!The {win_turtle} turtle is the winner")
            else:
                print(f"You Lost..!The {win_turtle} turtle is the winner")
            race_on=False
        ran_distance = random.randint(0, 10)
        tur.forward(ran_distance)





screen.exitonclick()