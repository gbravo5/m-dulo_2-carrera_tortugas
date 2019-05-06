import turtle
import random

class Route():
 
    def __init__(self, length, width, fillcolor, nb_participants):
       
        # a) screen setup:
        # create
        self.__screen = turtle.Screen()                                                      # method of turtle: Screen()
        # customize
        self.__screen.setup(length, width)
        self.__screen.bgcolor(fillcolor)
        self.__startline  = -0.45 * length
        self.__finishline =  0.45 * length
        
        # b) participants setup:
        self.__nb_participants = nb_participants
        # maximum number of participants = 7
        potential_y_coordinate      = [0, 1/4, -1/4, 1/8, -1/8, 1/6, -1/6]
        potencial_color_participant = ['red', 'blue', 'green', 'orange', 'black', 'yelow', 'pink']
        
        self.__listofparticipants = []
        for i in range(self.__nb_participants):
            # create
            participant = turtle.Turtle()                                                     # method of turtle: Turtle()
            # customize
            participant.color(potencial_color_participant[i])
            participant.shape('circle')
            participant.penup()                                                               # pull the pen up – no drawing when moving
            participant.setposition(self.__startline, potential_y_coordinate[i] * width)
            # refill listofparticipants
            self.__listofparticipants.append(participant)
            
    def compete(self):
        winner = False
        while not winner:
            for participant in self.__listofparticipants:
                nb_step = random.randint(1,6)
                participant.forward(nb_step)
                if participant.position()[0] >= self.__finishline:
                    winner = True
                    print('the color {} has won'.format(participant.color()[0]))

if __name__ == '__main__':
    race = Route(640, 480, 'lightgray', 5)
    race.compete()
  
      
                
            
            
            
            
        


        
        