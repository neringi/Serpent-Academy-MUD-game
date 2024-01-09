import json


def new_score(player, score):
    with open('leaderboard.txt', 'a') as file:
        file.write(f"{player}, {score}\n")


#update from the game file itself?
def update_from_game():
    with open('game_scores.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            player_name,score = line.strip().split(',')
            new_score(player_name, int(score))
    update_from_game()

def update_from_game_2(file_path):
    with open(file_path, 'r') as file:
        read_csv = csv.reader(file)
        for row in read_csv:
            player_name, score = row
            new_score(player_name,int(score))
game_file_one = ''
update_from_game_2()

def update_from_game_3(file_path):
    with open(file_path, 'r') as file:
        read_json = json.load(file)
        for value in read_json:
            player_name = value[f"Player {player_name}"]
            score = value["Score"]
            new_score(player_name, score)

game_file_two = ''
update_from_game_3(game_file_two)

def leaderboard(n):
    scores = []
    with open('leaderboard.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip().split(',') for line in lines]  # strips whitespaces and makes each word a list item
        # sort based on the scores
        sort = sorted(lines, key=lambda x: int(x[1]), reverse=True) #sorts in descending
        top_score = sort[:n]
        scores = [(name, int(score)) for name, score in top_score]
    return scores

#Test
#new_score('Test 1', 200)
#new_score('Test 2', 300)
#new_score('Test 3', 500)
#new_score('Test 4', 900)

top_score = leaderboard(10) #returns the top 10 players
print("Leaderboard: ")
for player_name, score in enumerate(top_score, start=1): #counts each score printed
    print(f"{player_name} : {score}")

