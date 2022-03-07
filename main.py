'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  '''This function draws a square
  args: myturtle (turtle object), width (int), top_left (int or float), top_right(int or float) 
  returns: None'''
  myturtle.up()
  myturtle.goto(top_left_x, top_left_y)
  myturtle.down()
  for i in range(4):
    myturtle.right(90)
    myturtle.forward(width)
def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  '''This function draws a line
  args: myturtle (turtle object), x_start (int or float), y_start (int or float), x_end (int or float), y_end (int or float)
  returns: None'''
  myturtle.up()
  myturtle.goto(x_start,y_start)
  myturtle.down()
  myturtle.goto(x_end,y_end)
  myturtle.up()
def drawCircle(myturtle=None, radius=0): #why is circle not round?
  '''This function draws a circle
  args: myturtle (turtle object), radius (int)'''
  myturtle.up()
  myturtle.goto(0,-1)
  myturtle.down()
  myturtle.circle(radius)
  myturtle.up()
def setUpDartboard(myscreen=None, myturtle=None):
  '''This function sets up a dartboard using the above functions
  args: myscreen (screen), myturtle (turtle object)
  returns: None'''
  myscreen.setworldcoordinates(-1,-1,1,1)
  drawSquare(myturtle,2,1,1)
  drawLine(myturtle,-1,0,1,0)
  drawLine(myturtle,0,-1,0,1)
  drawCircle(myturtle,1)
def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  '''This function determines if a dot is in the circle
  args: myturtle (turtle object), circle_center_x (int or float), circle_center_y (int or float), radius (int)
  returns: True or False'''
  if myturtle.distance(circle_center_x,circle_center_y) <= radius:
    return True
  else:
    return False
def throwDart(myturtle=None): #how big should dot be?
  '''This function simulates throwing a dart
  args: myturtle (turtle object)
  returns: None'''
  myturtle.up()
  x=random.uniform(-1,1)
  y=random.uniform(-1,1)
  myturtle.goto(x,y)
  if isInCircle(myturtle,0,0,1)==True:
    color = "pink"
  else:
    color = "purple"
  myturtle.dot(5,color)
def playDarts(myturtle=None): #am I allowed to put a print statement? should it return anything?
  '''This function simulates a game of darts between two players
  args: myturtle (turtle object)
  returns: None'''
  player_one_score = 0
  player_two_score = 0
  for i in range(10):
    throwDart(myturtle)
    if isInCircle(myturtle,0,0,1)==True:
      player_one_score=player_one_score + 1
    throwDart(myturtle)
    if isInCircle(myturtle,0,0,1)==True:
      player_two_score=player_two_score + 1
  if player_one_score > player_two_score:
    print("Player One Wins!")
  elif player_one_score < player_two_score:
    print("Player Two Wins!")
  else:
    print("Tie!")
def montePi(myturtle=None, num_darts=0):
  '''This function simulates an algorithm that returns the approximation of pi
  args: myturtle (turtle object), num_darts (int)
  returns: pi'''
  inside_count = 0
  for i in range(num_darts):
    throwDart(myturtle)
    if isInCircle(myturtle,0,0,1)==True:
      inside_count = inside_count + 1
  pi = 4*(inside_count/num_darts)
  return pi
  
#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
    window = turtle.Screen()
    darty = turtle.Turtle()
    darty.speed(0) # as fast as it will go!
    setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
    for i in range(10):
        throwDart(darty)
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    darty.clear()
    setUpDartboard(window, darty)
    playDarts(darty)
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    darty.clear()
    setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = montePi(darty, number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    window.exitonclick()

main()
