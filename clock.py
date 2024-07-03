import time
import turtle

# ---------------Function to move the hands -------------START -----------------------------#
def move_hands():
    current_time = time.localtime()
    second = current_time.tm_sec
    minute = current_time.tm_min
    hour = current_time.tm_hour % 12

    # --------------Move second hand -------------------START --------------------------#
    second_hand.penup()
    second_hand.goto(0, 0)
    second_hand.setheading(90)
    angle = second * 6
    second_hand.right(angle)
    second_hand.pendown()
    # --------------Move second hand -------------------END ----------------------------#

    # --------------Move minute hand -------------------START---------------------------#
    minute_hand.penup()
    minute_hand.goto(0, 0)
    minute_hand.setheading(90)
    angle = minute * 6
    minute_hand.right(angle)
    minute_hand.pendown()
    # --------------Move minute hand -------------------END ----------------------------#

    # -------------Move hour hand ---------------------START ---------------------------#
    hour_hand.penup()
    hour_hand.goto(0, 0)
    hour_hand.setheading(90)
    angle = (hour * 30) + (minute * 0.5)
    hour_hand.right(angle)
    hour_hand.pendown()
    # --------------Move hour hand --------------------END -----------------------------#
    scr.update()
    scr.ontimer(move_hands, 1000)

# ---------------Function to move the hands -------------END --------------------------------#

# -------------------- set up the screen --------------------START---------------------------#
scr = turtle.Screen()
scr.title("Our beautiful Clock")
scr.setup(width=900, height=800)

# --------------------Draw a clock face ---------------------START--------------------#

# ------------ Set the background image ----------------------------------------------#
scr.bgpic("image/imgclock.gif")
scr.tracer(0)

# ---------------Draw a hour marker ------------------------START ------------------#

# ---------------Create a hands of the clock----------------------------------------#
second_hand = turtle.Turtle()
second_hand.penup()
second_hand.shape('arrow')
second_hand.color('red')
second_hand.pendown()
second_hand.shapesize(stretch_wid=1, stretch_len=18)
second_hand.speed(0)

minute_hand = turtle.Turtle()
minute_hand.shape('arrow')
minute_hand.color('blue')
minute_hand.shapesize(stretch_wid=1, stretch_len=15)
minute_hand.speed(0)

hour_hand = turtle.Turtle()
hour_hand.shape('arrow')
hour_hand.color('green')
hour_hand.shapesize(stretch_wid=1, stretch_len=10)
hour_hand.speed(0)

# -------------initialize the clock hand -------------------------------------#
move_hands()
scr.mainloop()

# -------------------- set up the screen --------------------END---------------------------#
