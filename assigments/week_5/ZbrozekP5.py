# ZbrozekP5
# Programmer: Mike Zbrozek
# Email: MZbrozek1@cnm.edu
# Purpose:Play a game of rock paper scissors 

# Import Math random
import random

# List of valid game elements
gameList = ["rock", "paper", "scissors"]

# Initialize Variables to keep score of the game 
#game tally 
gameTally = 0
# Number of ties
tieCount = 0
# Number of wins
winTally = 0
# Number of losses
lossTally = 0

# Validate user entry
def inputValidation(userChoice, gameList):
    for object in gameList:
        if userChoice in gameList:
            userChoice = userChoice
        else: userChoice = input(" !! Enter a Valid choice: Rock, Paper or Scissors: \n").lower()
    return userChoice

# Score Keeper Function
def scoreKeeper(userScore, computerScore,tieCount, roundOver):
    if userScore == 2:
        roundOver = 0
        print("You won this round!")
    elif computerScore == 2:
        roundOver = 0
        print("You lost this round!")
    else:
        print(f"Score - You:{userScore} Computer:{computerScore} Ties: {tieCount}")
    return roundOver
   

# While user wants to keep playing
play_Again = "y"
while play_Again == "y": 
    roundOver = 1
    userScore = 0
    computerScore = 0  

    # While user score or computer score < 2 play game
    while not (roundOver == 0):

        # Ask user for their choice Rock/Paper/Scissors 
        userChoice = input("Enter your choice: Rock, Paper or Scissors: \n").lower()
        userChoice = inputValidation(userChoice, gameList)

        # Use a random number generator to generate the computer's choice
        computerChoice = gameList[random.randint(0,2)]
        
        # Show the user what was selected
        print(f"You selected {userChoice}, the computer selected {computerChoice}\n")

        # Evaluate who one or lost the round or if it was a tie
        if userChoice == computerChoice:
            print("You tied! Try harder!")
            # Increment # of ties
            tieCount += 1
        elif userChoice == "rock":
            if computerChoice == "scissors":
                print("You won! Rock knocks Scissors")
                userScore += 1
            elif computerChoice == "paper":
                print("You lose! Paper covers Rock")
                computerScore += 1
        elif userChoice == "paper":
            if computerChoice == "rock":
                print("You won! Paper covers Rock")
                userScore += 1
            elif computerChoice == "scissors":
                print("You lose! Scissors cut Paper")
                computerScore += 1
        elif userChoice == "scissors":
            if computerChoice == "paper":
                print("You win! Scissors cut Paper")
                userScore += 1
            elif computerChoice == "rock":
                print("You lose! Rock knocks Scissors")
                computerScore += 1
            
        
        # Run scoreKeeper function
        roundOver = scoreKeeper(userScore, computerScore, tieCount, roundOver)

        #Increment user stats
        gameTally += 1
        # if user wins round + 1
        if userScore == 2:
            winTally += 1
        # if user losses round lossTally +=1
        elif computerScore == 2:
            lossTally += 1
        else: tieCount 
    
    


    # Ask the player if they want to play again
    play_Again = input("You you like to play again? (y/n):").lower()
#Display goodbye message
print(f"You played {gameTally} rounds. You won {winTally}, lost {lossTally}.\nYou should be proud! :)")
