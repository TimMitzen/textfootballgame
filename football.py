# football game
# throwing and running t for throwing and r for running, q for quit s for scoreboard
# have different yard gains need 10 yards for first down and 100 for td, and 70 for fg
# four downs, touchdown is 7 points, field goal is 3 points
# have the cpu score once in a while
# have a timer
# if throw either complete or incomplete 1-100 yard completion
# if run gain or no gain 1-100 yards
# if get to 70 yard and 4th down kick fg
# if 100 yards score td
# less then 70 punt
# do above for cpu
# if either get to 21 or 1 min end game and print scoreboard
from Passes import pass_throw
import random
from Scoreboard import ScoreBoard
from Running import running
from datetime import datetime, timedelta
from print_scoreboard import print_scoreboard

print('Football Game')
end_time = datetime.now() + timedelta(minutes= 2)# gives 2 mins to work
while datetime.now() < end_time:
    user_input = input('To throw a pass hit p, for a r for running, s to bring up the scoreboard and q for quit\n')
    if user_input.lower() == 'q':
        quit(print('Game Over'))
    elif user_input.lower() == 'p':

        if random.random() <= .10:

            pass_throw(4)

        elif random.random() <= .10:
            pass_throw(2)

        elif random.random() <= .10:
            pass_throw(3)

        elif random.random() <= .10:
            pass_throw(5)
        else:
            pass_throw(1)

    elif user_input.lower() == 's':
        score_yards = sum(ScoreBoard.yards)
        score_downs = sum(ScoreBoard.downs)
        score_game = sum(ScoreBoard.user_score)
        cpu_scores = sum(ScoreBoard.cpu_score)
        print(f"Scoreboard\nYour Score: {score_game}\n"
              f"Downs: {score_downs}\nYards: {score_yards}\nCpu Score: {cpu_scores}")

    elif user_input.lower() == "r":
        if random.random() <= .10:
            running(2)

        elif random.random() <= .10:
            running(3)

        elif random.random() <= .10:
            running(4)

        elif random.random() <= .10:
            running(5)

        else:
            running(1)
    else:
        print('You hit a wrong key')

print_scoreboard()