class ScoreBoard:
    downs = [1]
    passes = []
    runs = []
    touchdowns = []
    field_goals = []
    user_score = []
    cpu_score = []
    yards = []
    first_downs = []

    def __init__(self, downs, touchdowns, field_goals, user_score, cpu_score, runs, passes, yards, first_dowws):
        self.downs = downs
        self.runs = runs
        self.touchdowns = touchdowns
        self.field_goals = field_goals
        self.user_score = cpu_score
        self.passes = passes
        self.user_score = user_score
        self.yards = yards
        self.first_downs = first_dowws
