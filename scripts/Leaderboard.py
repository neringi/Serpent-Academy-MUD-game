import json
from Player import Player 

class Leaderboard:
    def __init__(self, filename):
        self.filename = filename
    
    def save_score(self, player):
        with open(self.filename, 'r+') as f:
            text = f.read()
            f.seek(0)
            if len(text) == 0:
                file = []
            else:
                file = json.loads(text)
            try:
                index = [user["name"] for user in file].index(player.username)
                file[index]["points"] = player.points
            except ValueError:
                file += [{ "name": player.username, "points": player.points }]
            f.write(json.dumps(file))

    def __str__(self):
        with open(self.filename, 'r') as f:
            str = "\033[1;37;40m------- Leaderboard -------\033[0;37;48m"
            text = f.read()
            if len(text) == 0:
                return f"{str}\nNo Entries"
            file = json.loads(text)
            s = sorted(file, key=lambda u: u["points"], reverse=True)
            if type(file) is not list:
                return f"Error reading file, is {self.filename} corrupted?"
            for idx, score in enumerate(s):
                str += f"\n      \033[1;37;40m({idx+1}) {score['name']} - {score['points']}\033[0;37;48m"
            str += "\n\033[1;37;40m---------------------------\033[0;37;48m"
            return str
        
    def reset(self):
        with open(self.filename, 'w+') as f:
            file = []
            f.write(json.dumps(file))