import random as rn
import os

class Player:
    def __init__(self, name):
        self.stats = {
            "name": name,
            "score": 0,
            "age": 0,
            "money": 0,
            "health": rn.randint(75, 100),
            "happiness": rn.randint(75, 100),
            "relations": rn.randint(75, 100),
            "intelligence": rn.randint(33, 66)
        }
        
        self.kid_events = {
            "School": self.school,
            "Hobby": self.hobby
        }

        self.adult_events = {
            "Date": self.date,
            "Work": self.work,
            "Relationships": self.family,
            "Hobby": self.hobby
        }

        self.senior_events = {
            "Health Issues": self.health_issue,
            "Time with grandkids": self.family,
            "Hobby": self.hobby
        }

        
        self.important_people = []
        
        self.alive = True

    def grow_older(self):
        self.stats["age"] += 1
        self.stats["health"] -= rn.randint(0, 2)
        self.stats["happiness"] -= rn.randint(0, 2)
        
        if self.stats["health"] <= 0 or self.stats["happiness"] <= 0:
            self.alive = False
    
    def school(self):
        print("You are at school.")
        choice = input("Do you want to study hard or relax? (study/relax) ")

        if choice == "study":
            self.stats["intelligence"] += rn.randint(8, 12)
            self.stats["happiness"] -= rn.randint(3, 6)
            print("You studied hard.")
        else:
            self.stats["happiness"] += rn.randint(3, 6)
            self.stats["relations"] += rn.randint(2, 5)
            print("You relaxed with friends.")
        
    def work(self):
        print("You are at work.")
        
        if self.stats["intelligence"] > 60:
            choice = input("Work normally or take a risky promotion? (normal/risky) ")
        else:
            choice = "normal"

        if choice == "risky":
            if rn.random() < 0.5:
                self.stats["money"] += 10000
                self.stats["happiness"] += 5
                print("Promotion successful!")
            else:
                self.stats["health"] -= 10
                self.stats["happiness"] -= 10
                print("The risk backfired.")
        else:
            self.stats["money"] += rn.randint(2000, 4000)
            self.stats["happiness"] -= rn.randint(1, 4)

        
    def family(self):
        self.stats["score"] += rn.randint(0, 5)
        self.stats["happiness"] += rn.randint(5, 10)
        self.stats["relations"] += rn.randint(5, 10)
        
        for member in self.important_people:
            if member["relation"] == "family":
                self.stats["happiness"] += 1
                self.stats["relations"] += 1
                member["happiness"] += rn.randint(1, 5)
                member["relations"] += rn.randint(1, 5)
        
        print(f"{self.stats['name']} spends time with family and feels happier!")

    def check_stat(self):
        for stat, value in self.stats.items():
            if isinstance(value, int):
                if value < 0:
                    self.stats[stat] = 0
                elif value > 100 and stat != "money":
                    self.stats[stat] = 100
     
    
    def health_issue(self):
        tipe = rn.choice(["minor", "major"])
        
        if self.stats["age"] < 30:
            tipe = "minor"
        elif self.stats["age"] > 70:
            tipe = "major"
        
        if tipe == "minor":
            self.stats["health"] -= rn.randint(5, 15)
            self.stats["happiness"] -= rn.randint(0, 5)
        else:
            self.stats["health"] -= rn.randint(20, 50)
            self.stats["happiness"] -= rn.randint(10, 20)

        print(f"{self.stats['name']} has a {tipe} health issue.")

    def hobby(self):
        self.stats["happiness"] += rn.randint(5, 15)
        self.stats["health"] += rn.randint(0, 5)
        self.stats["relations"] += rn.randint(0, 5)
        
        if self.stats["age"] < 18:
            if rn.random() <= 0.5:
                self.important_people.append({"name": "Friend", "relation": "friend"})
        elif self.stats["age"] < 60:
            if rn.random() <= 0.3:
                self.important_people.append({"name": "Friend", "relation": "friend"})
        else:
            if rn.random() <= 0.6:
                self.important_people.append({"name": "Friend", "relation": "friend"})
        
        print(f"{self.stats['name']} enjoys a hobby and feels happier!")
    
    def date(self):
        if self.stats["age"] < 25:
            self.stats["happiness"] += rn.randint(10, 20)
            self.stats["relations"] += rn.randint(5, 10)
        elif self.stats["age"] < 40:
            self.stats["happiness"] += rn.randint(5, 15)
            self.stats["relations"] += rn.randint(3, 7)
        else:
            self.stats["happiness"] += rn.randint(2, 10)
            self.stats["relations"] += rn.randint(1, 5)

        print(f"{self.stats['name']} goes on a date and feels happier!")

    def random_event(self):
        if self.stats["age"] < 18:
            event_name, event_func = rn.choice(list(self.kid_events.items()))
        elif self.stats["age"] < 60:
            event_name, event_func = rn.choice(list(self.adult_events.items()))
        else:
            event_name, event_func = rn.choice(list(self.senior_events.items()))
        event_func()
    
    def choose_event(self):
        if self.stats["age"] < 18:
            events = self.kid_events
            for event in events:
                print(f"- {event}")
            event_name = input("Choose an event: ")
            if event_name in events:
                events[event_name]()
            else:
                print("Invalid event.")
        elif self.stats["age"] < 60:
            events = self.adult_events
            for event in events:
                print(f"- {event}")
            event_name = input("Choose an event: ")
            if event_name in events:
                events[event_name]()
            else:
                print("Invalid event.")
        else:
            events = self.senior_events
            for event in events:
                print(f"- {event}")
            event_name = input("Choose an event: ")
            if event_name in events:
                events[event_name]()
            else:
                print("Invalid event.")

name = input("Enter your name: ")
player = Player(name)

while True:
    if not player.alive:
        print(f"{player.stats['name']} has passed away at age {player.stats['age']}.")
        break
    
    if rn.random() < 0.4:
        player.choose_event()
    else:
        player.random_event()

    player.check_stat()
    player.grow_older()
    
    print(f"Age: {player.stats['age']}\nHealth: {player.stats['health']}\nHappiness: {player.stats['happiness']}\nRelations: {player.stats['relations']}\nIntelligence: {player.stats['intelligence']}\nMoney: {player.stats['money']}\n")