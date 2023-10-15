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

    def display_doors(self):
        return f'Round #{self.round_number}: Door 1 | Door 2 | Door 3 '

    def user_choose_door(self):
        return int(input("Choose a door: "))

    def reveal_goat_door(self, user_choice):
        return random.choice([door for door in self.doors if door != user_choice and self.doors[door] == "Goat"])

    def inform_about_reveal_goat(self, revealed_door):
        return f"Goat is in Door {revealed_door}"

    def user_stay_or_switch(self):
        # strip removes the extra spaces from the beginning and end of the input.
        return input("Stay or Switch? ").strip().lower()

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
    
    def show_outcome(self, stay_or_switch, user_choice, outcome):
        return f'You {stay_or_switch}ed with Door {user_choice} ... You {outcome}!'

    
    def record_results(self, user_choice, stay_or_switch, outcome):
        self.result_table.append([self.round_number, user_choice, stay_or_switch, outcome])
        self.round_number += 1
        
    def display_results(self):
        print("\nRESULTS TABLE\n")
        print("Round Choice Action Outcome")
        for result in self.result_table:
            print(f'{result[0]}     {result[1]}      {result[2]}    {result[3].capitalize()}')

    def display_summary(self):
        print("\nSUMMARY\n")
        print(f'Wins with switch = {self.win_switch}')
        print(f'Wins with stay = {self.win_stay}')
        total_rounds = self.round_number - 1
        print(f'Pr(Winning with switch) = {self.win_switch/total_rounds*100}%')
        print(f'Pr(Winning with stay) = {self.win_stay/total_rounds*100}%')

    def simulate(self):
        while(True):
            self.initialise_doors()
            print(self.display_doors())
            user_choice = self.user_choose_door()
            if user_choice == 0:
                break
            revealed_door = self.reveal_goat_door(user_choice)
            print(self.inform_about_reveal_goat(revealed_door))
            stay_or_switch = self.user_stay_or_switch()
            outcome = self.determine_outcome(user_choice, revealed_door, stay_or_switch)
            print(self.show_outcome(stay_or_switch, user_choice, outcome))
            self.record_results(user_choice, stay_or_switch, outcome)
           

if __name__ == '__main__':
    simulation = Threedoorproblem()
    simulation.simulate()
    simulation.display_results()
    simulation.display_summary()



    


            
            


              
    

    




    


