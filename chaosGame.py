from graphics import *                                                      
from random import randint



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
        
        

    


main()
