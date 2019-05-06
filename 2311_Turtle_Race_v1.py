import turtle

class Route():
    
    listofparticipants = []
      
    def __init__(self, length, width, fillcolor, nb_participants):
       
        # screen setup:
        # create
        self.__screen = turtle.Screen()                              # method of turtle: Screen()
        # customize
        self.__screen.setup(length, width)
        self.__screen.bgcolor(fillcolor)
        self.__startline  = -0.45 * length
        self.__finishline =  0.45 * length
        
        
        
        # participants setup:
        self.__nb_participants = nb_participants
        self.customize = []
        for i in range(self.__nb_participants):
            # maximum number of participants = 7
            potential_y_coordinate      = [0, 1/4, -1/4, 1/8, -1/8, 1/6, -1/6]
            potencial_color_participant = ['red', 'blue', 'green', 'orange', 'black', 'yelow', 'pink']
            self.customize.append((potential_y_coordinate[i], potencial_color_participant[i]))

        for i in self.customize:
            # create
            participant = turtle.Turtle()                             # method of turtle: Turtle()
            # customize
            participant.color(i[1])
            participant.shape('circle')
            participant.penup()                                       # pull the pen up – no drawing when moving
            participant.setposition(self.__startline, i[0] * width)
            
            
            
            
            # refill listofparticipants
            self.listofparticipants.append(participant)
        

if __name__ == '__main__':
    course_map = Route(640, 480, 'lightgray', 5)
        
        