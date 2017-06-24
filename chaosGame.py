from graphics import *                                                      
from random import randint
                                                          
def main():

    mode = raw_input("Enter mode: \t\t")
    win = GraphWin("chaosGame", 1024, 1024)  

    if mode == "triangle":
        Sierpinski_triangle(win)
    elif mode == "square":
        square(win)
    elif mode == "pentagon":
        pentagon(win)
    

def point_placement(original_points,current_point,number_of_points,win):

    print "click to place your points"

    for i in range (0,int(number_of_points)):
        current_point_c = Circle(win.getMouse(),1)
        current_point_c.draw(win)
        original_points.append(current_point_c)

    print "Click to select starting point!"
        
    current_point = Circle(win.getMouse(),1)
    current_point.draw(win)
        
    return current_point
  
def Sierpinski_triangle(win):
    
    number_of_points = 3
    original_points = []

    current_point = point_placement(original_points,
                    Circle(Point(0,0),1),
                    number_of_points,win)

    for i in range(0,10000000): 
        comp_point = original_points[randint(0,int(number_of_points) - 1)]
        current_point = Circle(Point(current_point.center.x + (comp_point.center.x - current_point.center.x) / 2, 
                                     current_point.center.y + (comp_point.center.y - current_point.center.y) / 2 ),1)
        current_point.draw(win)

def square(win):

    number_of_points = 4
    original_points = []

    print "Click to select starting point!"

    current_point = point_placement(original_points,
                                    Circle(Point(0,0),1),
                                    number_of_points,win)

    #Temporary values before the loop

    prev_comp_point = Circle(Point(0,0),1)

    #The first point can be just any point

    comp_point = original_points[randint(0,int(number_of_points) - 1)]

    not_same_vertex_twice(comp_point,
                          prev_comp_point,
                          current_point,
                          original_points,
                          number_of_points,
                          win)



def pentagon(win):

    number_of_points = 5
    original_points = []

    print "Click to select starting point!"

    current_point = point_placement(original_points,
                                    Circle(Point(0,0),1),
                                    number_of_points,win)

    #Temporary values before the loop

    prev_comp_point = Circle(Point(0,0),1)

    #The first point can be just any point

    comp_point = original_points[randint(0,int(number_of_points) - 1)]
    
    not_same_vertex_twice(comp_point,
                          prev_comp_point,
                          current_point,
                          original_points,
                          number_of_points
                          ,win)

        
def not_same_vertex_twice(comp_point,prev_comp_point,current_point,original_points,number_of_points,win):
       for i in range(0,10000000):
        #Make sure that a new point is not selected twice in a row
        while comp_point.center.x == prev_comp_point.center.x and comp_point.center.y == prev_comp_point.center.y :
                    comp_point = original_points[randint(0,int(number_of_points) - 1)]

        prev_comp_point = comp_point
        current_point = Circle(Point(current_point.center.x + (comp_point.center.x - current_point.center.x) / 2, 
                                     current_point.center.y + (comp_point.center.y - current_point.center.y) / 2 ),1)
        current_point.draw(win)



        

main()     
