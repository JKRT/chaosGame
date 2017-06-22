from graphics import *                                                      
from random import randint
                                                          
def main():                                                                                                                            
    win = GraphWin("My Circle", 1024, 1024)  
       

    number_of_points = raw_input("Enter ammount of points to be placed!")
    original_points = []
    
    print "click to place your points"

    for i in range (0,int(number_of_points)):
        current_point_c = Circle(win.getMouse(),1)
        current_point_c.draw(win)
        original_points.append(current_point_c)


    print "Click to select starting point!"


    current_point = Circle(win.getMouse(),1)
    current_point.draw(win)
        
    for i in range(0,10000000): 
        comp_point = original_points[randint(0,int(number_of_points) - 1)]
        current_point = Circle(Point(current_point.center.x + (comp_point.center.x - current_point.center.x) / 2, 
                                     current_point.center.y + (comp_point.center.y - current_point.center.y) / 2
                                     ),1)
        current_point.draw(win)



    #win.close()    # Close window when done                                                                                            
    
                                                                                                                                      
main()     
