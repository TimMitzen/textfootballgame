# 2nd down
# 3nd down
# 4rd down punt
from Scoreboard import ScoreBoard
from Cpu_turn import cpu_scorings


def downs(down):#for downs
    if down == 1:

        print('First down')
        ScoreBoard.downs.clear()#clears the downs
        ScoreBoard.downs.append(1)#adds to append
    elif down == 2:
        down = 1
        print(ScoreBoard.downs)
        ScoreBoard.downs.append(down)
        total_down = sum(ScoreBoard.downs)#adds the downs
        print(f"Number of Downs, {total_down}")
        if total_down == 4:
            print('You punted')
            cpu_scorings(1)
            ScoreBoard.downs.clear()
            ScoreBoard.yards.clear()
            ScoreBoard.downs.append(1)


