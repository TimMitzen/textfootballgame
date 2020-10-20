from Scoreboard import ScoreBoard
from Yards import yard_per
from Downs import downs
import random


# 1
# 2 pass == 10 yards
# 3 pass == 20 yards
# 4 pass == 50 yards
# 5 pass == touchdown
def pass_throw(passes):
    if passes == 1:# if pass on th football.py is 1
        print("incomplete pass")
        downs(2)#puts 2 into the downs function

    elif passes == 2:# if pass on th football.py is 2
        yards = 10
        ScoreBoard.yards.append(yards)#adds 10 to the yards dict
        print('You passed for 10 yards')
        yard_per(yards)#put yards into the yard_per function
        downs(1)#puts 1 into the downs fuction

    elif passes == 3:# if pass on th football.py is 3
        yards = 20
        ScoreBoard.yards.append(yards)#adds 20 to the yards dict
        print('You passed for 20 yards')
        yard_per(yards)#put yards into the yard_per function
        downs(1)#puts 1 into the downs function
    elif passes == 4:# if pass on th football.py is 4
        yards = 50
        ScoreBoard.yards.append(yards)#adds 50 to the yards dict
        print('You passed for 50 yards')
        yard_per(yards)#put yards into the yard_per function
        downs(1)#puts 1 into the downs function
    elif passes == 5:# if pass on th football.py is 5
        yards = 100
        ScoreBoard.yards.append(yards)#adds 50 to the yards dict

        yard_per(yards)#put yards into the yard_per function
    elif passes == 6:# if pass on th football.py is 6
        print('incomplete Pass!')
        downs(2)#puts 2 into the downs function
