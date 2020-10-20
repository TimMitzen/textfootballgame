# 1 run == 3 yards
# 2 run == 10 yards
# 3 run == 20 yards
# 4 run == 50 yards
# 5 run == touchdown
from Scoreboard import ScoreBoard
from Downs import downs
from Yards import yard_per


def running(run):
    if run == 1:
        print("No Gain on the play")
        downs(2)

    elif run == 2:
        yards = 10
        ScoreBoard.yards.append(run)
        print('You ran for 10 yards')
        yard_per(yards)
        downs(1)
    elif run == 3:
        yards = 20
        ScoreBoard.yards.append(run)
        print("You ran for 20 yards")
        yard_per(yards)
        downs(1)

    elif run == 4:
        yards = 50
        ScoreBoard.yards.append(yards)
        print("You gained 50 yards")
        yard_per(yards)
        downs(1)

    elif run == 5:
        yards = 100
        ScoreBoard.yards.append(yards)
        yard_per(yards)
