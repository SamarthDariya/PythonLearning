import random

def roll():
        roll = random.randint(1,6)
        return roll

while True:
        players = input("Enter the number of players between 2-4: ")
        if players.isdigit():
                players = int(players)
                if 2<= players <=4:
                        break
                else:
                        print("invalid input")
        else:
                print("invalid input.")

max_score = 50
scores = [0 for player in range(players)]

while max(scores) < max_score:

        for player_id in range(players):
                print("Player no.",player_id+1,"turn has started:")
                current_score = 0
                while True:
                        choice = input("Do you wanna continue the roll:(y or n) ")

                        if(choice != 'y'):
                                break
                        
                        value = roll()

                        if(value == 1):
                                print("taking all score away")
                                current_score = 0
                                print("terminating the turn")
                                break
                        
                        current_score+=value
                        print("YOUR CURRENT SCORE HAS BECOME", current_score)
                
                scores[player_id]+=current_score
                print("Your total score is:",scores[player_id])

win_score = max(scores)
winner = scores.index(win_score)

print("the winner is player",winner+1)