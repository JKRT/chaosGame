from graphics import *                                                      
from random import randint
import numpy as np


def main():

    mode = raw_input("Enter mode: \t\t")
    colour_mode = raw_input("Enter colour mode: \t") # Night, Day
    win = GraphWin("chaosGame", 1024, 1024)
    object_colour = 'black'

    
    if colour_mode == "Night":
        win.setBackground('black')
        object_colour = 'white'
    elif raw_input("Do you want a grid? \t") == "Yes": # Yes, No
        draw_cordinate_system(win)

  #  if not colour_mode == "Night":    
  #      draw_cordinate_system(win)

    if mode == "triangle":
        Sierpinski_triangle(win, object_colour)
    elif mode == "square":
        square(win, object_colour)
    elif mode == "pentagon":
        pentagon(win,space_pentagon, object_colour)
    elif mode == "hexagon":
        hexagon(win, object_colour)
    elif mode == "fern":
        Barnsley_Fern(win, object_colour)


def compare_points(p1,p2):
    if p1.x == p2.x and p1.y == p2.y:
        return True

    return False


def compare_vertexes(v1,v2):
    if v1.label == v2.label:
        return True

    return False

def point_placement(original_points,current_point,number_of_points,win, colour):

    print "click to place your points"

    for i in range (0,int(number_of_points)):
        current_point_c = Vertex(win.getMouse(),1,i)
        current_point_c.setOutline(colour)
        current_point_c.setFill(colour)
        current_point_c.draw(win)
        original_points.append(current_point_c)

    print "Click to select starting point!"
        
    current_point = Vertex(win.getMouse(),0.0001,0)
    current_point.setOutline(colour)
    current_point.setFill(colour)
    current_point.draw(win)
        
    return current_point


#Constraints
def space_pentagon(comp_point,prev_comp_point,current_point,original_points,number_of_points,win, colour):
    curr = 0
    prev = 0
    
    done = True

    for p in original_points:
        print p.label
    
    
    for i in range(0,100000000):
        
        done = False
        while not done:
            comp_point = original_points[randint(0,int(number_of_points) - 1)]
        
            if not comp_point.label == curr + 1 % 5 and not comp_point.label == prev + 4 % 5:
                done = True

        prev = curr
        
        curr = comp_point.label

        current_point = Circle(Point(current_point.center.x + (comp_point.center.x - current_point.center.x) / 2, 
                                     current_point.center.y + (comp_point.center.y - current_point.center.y) / 2 ),1)
        current_point.setOutline(colour)
        current_point.setFill(colour)
        current_point.draw(win)


def not_same_vertex_twice(comp_point,prev_comp_point,
                          current_point,original_points,number_of_points,win, colour):

    for i in range(0,10000000):
        #Make sure that a new point is not selected twice in a row
        while comp_point.center.x == prev_comp_point.center.x and comp_point.center.y == prev_comp_point.center.y :
                    comp_point = original_points[randint(0,int(number_of_points) - 1)]

        prev_comp_point = comp_point
        current_point = Circle(Point(current_point.center.x + (comp_point.center.x - current_point.center.x) / 2, 
                                     current_point.center.y + (comp_point.center.y - current_point.center.y) / 2 ),0.00001)

        current_point.setOutline(colour)
        current_point.setFill(colour)
        current_point.draw(win)

  
def Sierpinski_triangle(win, colour):
    
    number_of_points = 3
    original_points = []

    current_point = point_placement(original_points,
                    Circle(Point(0,0),0.0001),
                                    number_of_points,win, colour)

    for i in range(0,10000000): 
        comp_point = original_points[randint(0,int(number_of_points) - 1)]
        current_point = Circle(Point(current_point.center.x + (comp_point.center.x - current_point.center.x) / 2, 
                                     current_point.center.y + (comp_point.center.y - current_point.center.y) / 2 ),0.000001)
        current_point.setOutline(colour)
        current_point.setFill(colour)
        current_point.draw(win)

def square(win, colour):

    number_of_points = 4
    original_points = []

    print "Click to select starting point!"

    current_point = point_placement(original_points,
                                    Circle(Point(0,0),0.0001),
                                    number_of_points,win, colour)

    #Temporary values before the loop

    prev_comp_point = Circle(Point(0,0),1)

    #The first point can be just any point

    comp_point = original_points[randint(0,int(number_of_points) - 1)]

    not_same_vertex_twice(comp_point,
                          prev_comp_point,
                          current_point,
                          original_points,
                          number_of_points,
                          win, colour)

def pentagon(win,constraint, colour):

    number_of_points = 5
    original_points = []

    print "Click to select starting point!"

    current_point = point_placement(original_points,
                                    Circle(Point(0,0),0.0001),
                                    number_of_points,
                                    win, colour)

    #Temporary values before the loop

    prev_comp_point = Vertex(Point(0,0),1,0)

    #The first point can be just any point

    comp_point = original_points[randint(0,int(number_of_points) - 1)]

    constraint(comp_point,prev_comp_point,current_point,
               original_points,number_of_points,win, colour)

def hexagon(win, colour):

    number_of_points = 6
    original_points = []

    print "Click to select starting point"


    current_point = point_placement(original_points,
                                    Circle(Point(0,0),1),
                                    number_of_points,
                                    win, colour)

    #Temporary values before loop
    prev_comp_point = Circle(Point(0,0),1)

    comp_point = original_points[randint(0,int(number_of_points) -1)]

    not_same_vertex_twice(comp_point,
                          prev_comp_point,
                          current_point,
                          original_points,
                          number_of_points
                          ,win, colour)


def draw_cordinate_system(win):

    xaxis = Line( Point(0,512), Point(1024,512))
    xaxis.draw(win)

    yaxis = Line (Point(512,0), Point(512,1024))
    yaxis.draw(win)

    origo = Circle(Point(512,512),3)
    origo.draw(win)

    for i in range(0,1024):
        if i % 64 == 0:
            stepLineX = Line(Point(0,i), Point(1024,i))
            stepLineY = Line(Point(i,0),Point(i,1024))

            stepLineX.draw(win)
            stepLineY.draw(win)
        

############# Barnsley Fern #############
            
def f_1(x_array):
    A = np.array([[0,0],[0,0.16]])
    y_array = np.dot(A,x_array)
    return y_array
    
def f_2(x_array):
    A = np.array([[0.85,0.04],[-0.04,0.85]])
    b = np.array([0,1.6])
    y_array = np.dot(A,x_array) + b
    return y_array

def f_3(x_array):
    A = np.array([[0.2,-0.26],[0.23,0.22]])
    b = np.array([0,1.6])
    y_array = np.dot(A,x_array) + b
    return y_array

def f_4(x_array):
    A = np.array([[-0.15,0.28],[0.26,0.24]])
    b = np.array([0,0.44])
    y_array = np.dot(A,x_array) + b
    return y_array

def Cartesian_to_Circle(x_array):
    origin = np.array([512,800])
    trans = np.array([[70,0],[0,70]])
    y_array = origin - np.dot(trans,x_array)
    c = Circle(Point(y_array[0],y_array[1]),0.0001)
    return c
    
def Barnsley_Fern(win, colour):
    cart = np.array([0,0])

    for i in range(0,10000000):
        p = Cartesian_to_Circle(cart)
        p.setOutline(colour)
        p.setFill(colour)
        p.draw(win)

        r = np.random.uniform(0,100)

        if r <= 1:
            cart = f_1(cart)
        elif r <= 86:
            cart = f_2(cart)
        elif r <= 93:
            cart = f_3(cart)
        else:
            cart = f_4(cart)
    
main()
