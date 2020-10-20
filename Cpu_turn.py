from Scoreboard import ScoreBoard
import random
from print_scoreboard import print_scoreboard

def cpu_scorings(cpu):#if the user punts and then cpu scores
    if cpu == 1:
        if random.random() <= .30:# 30 percent chance
            print("Cpu ran for 40 yards")
            print("\n\nForth down, Cpu kicks and scored a Field goal")
            ScoreBoard.cpu_score.append(3) #adds to the cpu score
            print_scoreboard()
        elif random.random() <= .50:#fifty percent chance
            print('\n\nCpu runs for a td!')
            ScoreBoard.cpu_score.append(7)
            print_scoreboard()

        else:
            print("\n\nCpu throw incomplete pass 4th down")
            print('Cpu punted')
            print_scoreboard()