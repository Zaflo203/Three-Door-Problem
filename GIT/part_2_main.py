import random 

class Threedoorproblem:

    def __init__(self):
        self.round_number = 1
        self.win_switch = 0
        self.win_stay = 0
        self.result_table = []

    def initialise_doors(self):
        self.doors = {
            1: "Goat",
            2: "Goat",
            3: "Goat"
        }
        self.prize_door = random.randint(1, 3)
        self.doors[self.prize_door] = "Car"

    def reveal_goat_door(self, user_choice):
        return random.choice([door for door in self.doors if door != user_choice and self.doors[door] == "Goat"])
    
    def determine_outcome(self, user_choice, revealed_door, stay_or_switch):
        if (stay_or_switch == "stay" and user_choice == self.prize_door) or (stay_or_switch == "switch" and self.doors[user_choice] == "Goat"):
            outcome = "WIN"
            if stay_or_switch == "switch":
                self.win_switch += 1
            else:
                self.win_stay += 1
        else:
            outcome = "lose"
        return outcome
    
    def record_results(self, user_choice, stay_or_switch, outcome):
        self.result_table.append([self.round_number, user_choice, stay_or_switch, outcome])
        self.round_number += 1

    def stimulate_silent(self):
        for i in range(50):
            self.initialise_doors()
            user_choice = random.randint(1,3)
            reveal_door = self.reveal_goat_door(user_choice)
            stay_or_switch = random.choice(["stay", "switch"])
            outcome = self.determine_outcome(user_choice, reveal_door, stay_or_switch)
            self.record_results(user_choice, stay_or_switch, outcome)

    def display_results(self):
        print("Round Choice Action Outcome")
        for result in self.result_table:
            print(f'{result[0]}     {result[1]}      {result[2]}    {result[3].capitalize()}')





