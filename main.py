
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#def hurdle():
#    #move()
#    turn_left()
#    #move()
#    while not right_is_clear():
#        move()
#    turn_right()
#    move()
#    turn_right()
#   while front_is_clear():
#        move()
#    turn_left()
       
#for i in range(1,7):
#    hurdle()
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    