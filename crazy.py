import random

def crazy_eights()->int:
    """# This function initializes the game and plays the game to completion. Both the left reel
    # and right reel are spun simultaneously. If a reel lands on the number 8, the big number 8
    # above the reel lights up 1/8 of the way until it is fully lit. Once one reel's big 8 is fully
    # lit, then the player is awarded 10 credits each time that specific reel lands on the number 8
    # until the game ends. The game ends once both big number 8s above the reels are lit and the 
    # player is awarded 50 credits.

    Returns:
        int: [Amount of credits won or lost after playing the game to completion. A positive number
        implies that the user won credits, and a negative number implies that the user lost credits]
    """    
    game={
    "over":False,
    "left":[1,2,3,4,5,6,7,8,9],
    "right":[0,1,2,3,4,5,6,7,8,9],
    "left_eight":0,
    "right_eight":0,
    "credit_count":0
    }
    # Plays the game until completion
    while not game["over"]:
        # Each play costs one credit
        game["credit_count"]-=1
        # randomly "spin" each reel
        left=random.choice(game["left"])
        right=random.choice(game["right"])
        # print(f'Left    Right\n{left}       {right}')
        if left==8:
            game["left_eight"]+=1
            # print(f'Congrats! You hit an 8!! \nLeft Big Eight Progress: {game["left_eight"]}/8\nRight Big Eight Progress: {game["right_eight"]}/8')
            if game["right_eight"]>=8 and game["left_eight"]>=8:
                game["credit_count"]+=50
                game["over"]=True
                # print(f'Game Over! Total Credits: {game["credit_count"]}')
                break
            elif game["left_eight"]>8:
                game["credit_count"]+=10
        if right==8:
            game["right_eight"]+=1
            # print(f'Congrats! You hit an 8!! \nLeft Big Eight Progress: {game["left_eight"]}/8\nRight Big Eight Progress: {game["right_eight"]}/8')
            if game["left_eight"]>=8 and game["right_eight"]>=8:
                game["credit_count"]+=50
                game["over"]=True
                # print(f'Game Over! Total Credits: {game["credit_count"]}')
                break
            elif game["right_eight"]>=8:
                game["credit_count"]+=10
    return game["credit_count"]

def crazy_monte_carlo(trials:int)->list:
    credit_count=0
    avg=0
    for t in range(1,trials+1):
        final=crazy_eights()
        credit_count+=final
        if t%(trials//100)==0:
            avg=credit_count/t
            print(f"Progress: {(t/trials) * 100:3.0f}%   Average Credits: {avg:.3f}")
    avg_credits=credit_count/trials
    return round(avg_credits)

print(f'Credits won: {crazy_eights()}\n')
print(crazy_monte_carlo(100))