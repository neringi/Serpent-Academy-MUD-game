import random
import time

class StudentNPC:
    def __init__(self, name, mood="neutral", social=20):
        self.name = name
        self.mood = mood
        self.social = social

    def introduction(self):
        print(f"Hi USER my name is {self.name} nice to meet you!")

    def talk(self):
        if self.mood == "Happy":
            return "I'm having a great day! How are you?"
        elif self.mood == 'Sad':
            return "I'm feeling a bit rough. What's going on?"
        elif self.mood == "Grumpy":
            return "What do you want?"
        elif self.mood == "Neutral":
            return "Hey! Nice to see you, Whats up?"

    # social skill with player
    def social(self):
        if self.respond or self.talk:
            self.social += random.randint(2, 5)
            print(f"Social skill has increased by {self.social}")
            if self.social == 25:
                print(f"Your friendship with {self.name} has levelled up!")

    def respond(self, response):
        if "study" in response.lower():
            self.social += random.randint(2, 5)
            return random.choice(["I have been studying hard for the test",
                                  "I have been learning new spells",
                                  "I have combat class later"])
        if "Lake" in response.lower():
            self.social += random.randint(3, 6)
            return random.choice(["I am going out to the lake later",
                                  "There have been so many stories about the lake",
                                  "I was lost in the mist last week!"])
        elif "Courtyard" in response.lower():
            self.social += random.randint(3, 6)
            return random.choice(["The courtyard has beautiful flowers",
                                  "I am going to the courtyard after class,"
                                  "I think the gargoyle in the courtyard moves"])
        elif "mood" in response.lower():
            return "I am Feeling", self.mood

        else:
            return "It is a nice day outside"


Student_1 = StudentNPC(name="Luna", mood="Happy")
Student_2 = StudentNPC(name="Caspian", mood="Sad")
Student_3 = StudentNPC(name="Orion", mood="Grumpy")
Student_4 = StudentNPC(name="Calista", mood="Happy")
Student_5 = StudentNPC(name="Thorne", mood="Happy")
Student_6 = StudentNPC(name="Fae", mood="Neutral")
Student_7 = StudentNPC(name="Lyra", mood="Grumpy")
Student_8 = StudentNPC(name="Rune", mood="Sad")


class BoatmanNPC: #Boat/ferryman from lake
    def __init__(self,name,social = 10):
        self.name = name
        self.social = social

    def riddle(self):
        self.social += 5
        print("Hello Traveller....I have a question for you")
        time.sleep(2)
        print("Answer correctly and you will be rewarded handsomely...")
        time.sleep(2)
        print('''
        In lily padded kingdoms, I reside
        A silent hunter, eyes open wide,
        With a flick of my tongue, I dine,
        An expert of camouflage, in colours divine.
        What am I?
        ''')
        time.sleep(2)
        user_response = input("What is your answer?: ")
        if user_response.lower() == 'Frog':
            return self.give_item()
        else:
            print("That is incorrect. Farewell, Traveller...")
            return self.incorrect_answer()

    def give_item(self):
        items = ["Rusty Talisman", "Healing Balm", "Thorny Dagger"]
        chosen_item = random.choice(items)
        return f"{self.name} gives you the {chosen_item}"

    def incorrect_answer(self):
        print(f"{self.name} disappears into thin air")


boatman = BoatmanNPC(name="Captain Cedric")
print(boatman.riddle())
print(boatman.give_item())#testing


class TeacherNPC:
    def __init__(self,name,teach,subject):
        self.name = name
        self.teach = teach
        self.subject = subject
        self.skill = ""
        self.social = 0

    def teach(self):
        if self.skill == 'Warrior':
            self.skill += random.randint(2,6)
        elif self.skill == 'Mage':
            self.skill += random.randint(2,6)
        elif self.skill == 'Trickster':
            self.skill += random.randint(2,6)

Teacher1 = TeacherNPC(name="Eden Eldritch",teach="Warrior",subject="Combat")
Teacher2 = TeacherNPC(name="Seraphina Spellweaver", teach="Mage", subject="Magic")
Teacher3 = TeacherNPC(name="Mr Wily", teach="Trickster", subject="Trickery")