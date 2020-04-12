#this class simulates a player's
#name, symbol and position
#import random and string
import string
import random
class Player:
    #The _ _init_ _ method accepts an argument for name, symbol and position.
    #and they are assigned to __name,__symbol,__position attribute.
    def __init__(self,name,symbol,position):
        self.__name = name
        self.__symbol = symbol
        self.__position = position
		
    #the set_name method accepts an argument for name and it is assigned to __name
    def set_name(self,name):
        self.__name = name
        
    #the set_symbol method gives a random letter for player from a-z
    def set_symbol(self):
        self.__symbol = random.choice(string.ascii_letters[0:26])

    #the get_name method returns a name for player    
    def get_name(self):
        return self.__name
    
    #the get_symbol method returns a random symbol for player
    def get_symbol(self):
        return self.__symbol
    
    #the set_position method accepts an argument for position and it is assigned to __position
    def set_position(self, position):
        self.__position = position
    
    #the get_position method returns a value for player
    def get_position(self):
        return self.__position
    
    # The _ _str_ _ method returns a string 
    def __str__(self):
        return (self.__name) +"("+ (self.__symbol)+")"+":"+str(self.__position)
    