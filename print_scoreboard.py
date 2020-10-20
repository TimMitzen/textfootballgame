from Scoreboard import ScoreBoard


def print_scoreboard():
    return print(f'\n\nScoreboard\nUser Score: {sum(ScoreBoard.user_score)}\nCpu Score: {sum(ScoreBoard.cpu_score)}')
