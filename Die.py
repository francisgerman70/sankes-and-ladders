#this class simulates a die that can be tossed
#import random for die class
import random
class Die:
    #The _ _init_ _ method initializes the faceup data attribute with 1. 
    def __init__(self):
        self.__faceup = 1
		
    #the throw method gives a random number from 1 - 6    
    def throw(self):
        if random.randint(1,6) == 1:
            self.__faceup = 1
        elif random.randint(1,6) == 2:
            self.__faceup = 2
        elif random.randint(1,6) == 3:
            self.__faceup = 3
        elif random.randint(1,6) == 4:
            self.__faceup = 4
        elif random.randint(1,6) == 5:
            self.__faceup = 5
        else:
            self.__faceup = 6
			
    #the get_faceup method returns a random number from 1-6    
    def get_faceup(self):
        return self.__faceup