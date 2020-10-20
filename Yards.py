# yards
# 10 yards for first down 100 yards for td
from Scoreboard import ScoreBoard
from print_scoreboard import print_scoreboard

def yard_per(yard):
    if yard == 100:
        print('Touchdown!')
        ScoreBoard.yards.clear()#clears yards in scoreboard
        ScoreBoard.passes.clear()#clears passses
        ScoreBoard.downs.clear()#clears downs
        score = 7
        ScoreBoard.user_score.append(score)#add user score in dict
        scores = sum(ScoreBoard.user_score)#uses sum to add the score
        print(f"Score: {scores}")
        ScoreBoard.downs.append(1)#adds to downs it dict
        print_scoreboard()
