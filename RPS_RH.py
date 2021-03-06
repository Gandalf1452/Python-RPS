########How I did scoring is that I based it off of whether or not you won, then went off of the ratio of Player Wins to CPU Wins, making it a 1 to 10 scale#################
########For tie scores, the new score is added next to the old score##############
###########Last Update: 3-8-18###############
############New Features: Added Button Input#########
import random
from gpiozero import Button
import time
ranNum = 0
end = False
global playerWins,cpuWins,cpuChoicee,playagain1,playagain2,score,score_file,scores,topTen,fileName,highScores
rock = Button(12)
paper = Button(17)
scissors = Button(26)
userName = input("What is your name? ")
fileName = input("Name the file where scores will be held: ")

######This function allows the player to view the top 10 scores if they wish#########
def view_scores():
    highScores = input("Would you like to view the high scores?(Y/N) ")
    if highScores.startswith("y") or highScores.startswith("Y"):
        words = []
        score_file2 = open(fileName + ".txt","r")
        for line in score_file2:
            words += line.split()
        words.sort()
        words.reverse()
        score_file2.close()
        print("Top Scores")
        print("-------------")
        if len(words) == 11:
            words.remove(words[10])
            print(words)
        else:
            print(words)
    elif highScores.startswith("n") or highScores.startswith("N"):
        print("OK then, if that is your choice!")
    else:
        print("Invalid input, try again")
        view_scores()      
topTen = []
cpuChoicee = "0"
playerWins = 0
cpuWins = 0

######This function generates the CPU's choice of Rock, Paper, Scissors######
def gen_num():
    global cpuChoicee
    global ranNum
    ranNum = random.randint(1,3)
    if ranNum == 1:
        cpuChoicee = "Rock"
    elif ranNum == 2:
        cpuChoicee = "Paper"
    elif ranNum == 3:
        cpuChoicee = "Scissors"
        
#######This function gets the score based on the outcome of the game#######        
def score_gen():
    global score
    if playerWins == 5 and cpuWins == 0:
        score = 10
    elif playerWins == 5 and cpuWins == 1:
        score = 9
    elif playerWins == 5 and cpuWins == 2:
        score = 8
    elif playerWins == 5 and cpuWins == 3:
        score = 7
    elif playerWins == 5 and cpuWins == 4:
        score = 6
    elif playerWins == 0 and cpuWins == 5:    
        score = 1
    elif playerWins == 1 and cpuWins == 5:
        score = 2
    elif playerWins == 2 and cpuWins == 5:
        score = 3
    elif playerWins == 3 and cpuWins == 5:
        score = 4
    elif playerWins == 4 and cpuWins == 5:
        score = 5
    else:
        score = 0
        
#######This function writes the score out to the specified file########        
def get_score():
    s = " "
    topTen = (str(score) + "," + userName)
    s.join(topTen)
    score_file = open(fileName + ".txt","a+")
    score_file.write("\n" + topTen)
    score_file.close()
    
#######This is the while loop where the Rock Paper Scissors game runs####################            
while end == False:
    global score
    global playerChoice
    global cpuChoice
    global playerChoices
    gen_num()
    cpuChoice = ranNum
    if playerWins < 5 and cpuWins < 5:
        #time.sleep(1)
        #print("The CPU has chosen...")
        #time.sleep(1)
        #playerChoice = input("Choose Rock, Paper, or Scissors: ")
        time.sleep(.5)
        if rock.is_pressed:
            if cpuChoice == 1:
                print("It is a tie!" + " The CPU picked " + cpuChoicee + "\nPlayer Wins: " + str(playerWins) + " || " + "CPU Wins: " + str(cpuWins))
            elif cpuChoice == 2:
                cpuWins += 1
                print("CPU wins the round!" + " The CPU picked " + cpuChoicee + "\nPlayer Wins: " + str(playerWins) + " || " + "CPU Wins: " + str(cpuWins))
            elif cpuChoice == 3:
                playerWins += 1
                print(userName + " wins the round!" + " The CPU picked " + cpuChoicee + "\nPlayer Wins: " + str(playerWins) + " || " + "CPU Wins: " + str(cpuWins))
        elif paper.is_pressed:
            playerChoice = 2
            if cpuChoice == 1:
                playerWins += 1
                print(userName + " wins the round!" + " The CPU picked " + cpuChoicee + "\nPlayer Wins: " + str(playerWins) + " || " + "CPU Wins: " + str(cpuWins))
            elif cpuChoice == 2:
                print("It is a tie!" + " The CPU picked " + cpuChoicee + "\nPlayer Wins: " + str(playerWins) + " || " + "CPU Wins: " + str(cpuWins))
            elif cpuChoice == 3:
                cpuWins += 1
                print("CPU wins the round!" + " The CPU picked " + cpuChoicee + "\nPlayer Wins: " + str(playerWins) + " || " + "CPU Wins: " + str(cpuWins))
        elif scissors.is_pressed:
            playerChoice = 3
            if cpuChoice == 1:
                cpuWins += 1
                print("CPU wins the round!" + " The CPU picked " + cpuChoicee + "\nPlayer Wins: " + str(playerWins) + " || " + "CPU Wins: " + str(cpuWins))
            elif cpuChoice == 2:
                playerWins+= 1
                print(userName + " wins the round!" + " The CPU picked " + cpuChoicee + "\nPlayer Wins: " + str(playerWins) + " || " + "CPU Wins: " + str(cpuWins))
            elif cpuChoice == 3:
                print("It is a tie!" + " The CPU picked " + cpuChoicee + "\nPlayer Wins: " + str(playerWins) + " || " + "CPU Wins: " + str(cpuWins))
        else:
            time.sleep(.05)
    elif playerWins == 5:
        score_gen()
        print(userName + " wins!!!")
        print("Score: " + str(score))
        get_score()
        view_scores()
        playAgain1 = input("Play Again?(y/n) ")
        if playAgain1 == "y" or playAgain1 == "Y":
            playerWins = 0
            cpuWins = 0
        elif playAgain1 == "n" or playAgain1 == "N":
            break
        else:
            print("Invalid input, try again")
    elif cpuWins == 5:
        score_gen()
        print("Aww... the CPU won...")
        print("Score: " + str(score))
        get_score()
        view_scores()
        playAgain2 = input("Play Again?(y/n) ")
        if playAgain2 == "y" or playAgain2 == "Y":
            playerWins = 0
            cpuWins = 0
        elif playAgain2 == "n" or playAgain2 == "N":
            break
        else:
            print("Invalid input, try again")



