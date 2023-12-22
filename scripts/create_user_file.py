import os.path

lb_file =  "./resources/serpent_academy_leaderboard.csv"
save_file =  "./resources/serpent_academy_leaderboard.csv"

def newLeaderboard():
    if os.path.isfile(lb_file):
        print("Leaderboard already exists")
    else:
        with open(lb_file, "w") as file_object:
            file_object.write("name,password")

        print("Users csv file initiated")

        file_object.close()  

def newSaveFile():
    if os.path.isfile(save_file):
        print("Save File already exists")
    else:
        with open(save_file, "w") as file_object:
            file_object.write("name,password")

        print("Users csv file initiated")

        file_object.close()  