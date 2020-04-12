import Die
import SL_Board
import Player

def main():
	# Your code goes here
	# this program plays a game of snakes and ladders with two players
    print("SNAKES AND LADDERS")
    print("")
	
	#define variables for random alphabet from a-z
    alpha = ''
    bet = ''
	
	#create accumulators
    quick = 1
    post = 1  
		
#Add and document suitable functions
    game = boardData()
	#display the board 
    print("")
    print("The board:")
    print("")
    print(game)
    play = start(quick,post)
	
#this function contains the activity of the players	
def start(quick,post):
    #create an object
    my_die = Die.Die()
	
	#create variables for random aplhabets from a-z
    alpha = ''
    bet = ''
	#create an object for player1
    player1 = Player.Player("aaron",alpha,quick)
    player1.set_symbol()
    alpha = player1.get_symbol()
    print("player1 =" ,player1)
    
	#create an object for player2
    player2 = Player.Player("quinn",bet,post)
    player2.set_symbol()
    bet = player2.get_symbol()
    print("player2 =" ,player2)
	#use while loop to get the position of the players
    while quick < 36 and post < 36:
        my_die.throw()
        hat = my_die.get_faceup()
        if quick == 14:
            quick = 3
        elif quick == 8:
            quick = 29
        elif quick == 17:
            quick = 28
        elif quick == 25:
            quick = 10
        elif quick == 24:
            quick = 26
        elif quick == 23:
            quick = 10
        elif quick == 31:
            quick = 13
        elif quick == 34:
            quick = 25
        
        quick = quick + hat
        
        my_die.throw()
        tail = my_die.get_faceup()
        if post == 14:
            post = 3
        elif post == 8:
            post = 29
        elif post == 17:
            post = 28
        elif post == 24:
            post = 26
        elif post == 2:
            post = 10
        elif post == 31:
            post = 13
        elif post == 34:
            post = 25
        post = post + tail
        print("aaron","(",alpha,"):",quick)
        
        print("Quinn","(",bet,"):",post)
        
        
        if quick >= 36:
            print("Winner aaron ",alpha)
        elif post >= 36:
            print("Winner quinn ",bet)
			
#This function can be called in your program. 	
def boardData():
	with open("boardConfig.txt","r") as fileHandle:
		size = int(fileHandle.readline().strip("\n"))
		snakeData = fileHandle.readline().split()
		for i in range(len(snakeData)):
			snakeData[i] = int(snakeData[i].strip("\n"))
		ladderData = fileHandle.readline().split()
		for i in range(len(ladderData)):
			ladderData[i] = int(ladderData[i].strip("\n"))
		
		# Convert snakes to a list of tuples
		snakes = []
		for i in range(0,len(snakeData)//2):
			snakes.append( (snakeData[2*i], snakeData[2*i+1]) )
		
		# Convert ladders to a list of tuples
		ladders = []
		for i in range(0,len(ladderData)//2):
			ladders.append( (ladderData[2*i], ladderData[2*i+1]) )
		newBoard = SL_Board.SL_Board(size,snakes,ladders)
		return newBoard

# Do not change anything below here. 		
if __name__ == "__main__":
	main()