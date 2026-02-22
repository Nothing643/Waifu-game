import time
import random
import json
import os
from pathlib import Path

rare_waifus = [
    'Nami (One Piece)',
    'Erza Scarlet (Fairy Tail)', 
    'Chika Fujiwara (Kaguya-sama: Love is War)', 
    'Faye Valentine (Cowboy Bebop)', 
    'Mitsuri Kanroji (Demon Slayer)', 
    'Maka Albarn (Soul Eater)', 
    'Yor Forger (Spy x Family)', 
    'Raphtalia (The Rising of the Shield Hero)', 
    'Rin Tohsaka (Fate/stay night)', 
    'Momo Yaoyorozu (My Hero Academia)', 
    'Ochaco Uraraka (My Hero Academia)', 
    'Saber (Fate/stay night)', 
    'Marin Kitagawa (My Dress-Up Darling)', 
    'Shinobu Oshino (Monogatari Series)', 
    'Chizuru Mizuhara (Rent-A-Girlfriend)', 
    'Kaguya Shinomiya (Kaguya-sama: Love is War)', 
    'Yoruichi Shihouin (Bleach)', 
    'Bulma (Dragon Ball)', 
    'Asuka Langley Soryu (Neon Genesis Evangelion)',
    'Nezuko Kamado (Demon Slayer)'
]



legendary_waifus = [
    "Rem (Re:Zero - Starting Life in Another World)",
    "Megumin (KonoSuba)",
    "Makima (Chainsaw Man)",
    "Shinobu Kocho (Demon Slayer)",
    "Hestia (DanMachi)",
    "Akeno Himejima (High School DxD)",
    "Zero Two (Darling in the Franxx)",
    "Asuna Yuuki (Sword Art Online)",
    "Mikasa Ackerman (Attack on Titan)",
    "Makise Kurisu (Steins;Gate)",
    "Mai Sakurajima (Rascal Does Not Dream of Bunny Girl Senpai)",
    "Hinata Hyuga (Naruto)",
    "Rias Gremory (High School DxD)",
    "Esdeath (Akame ga Kill!)",
    "Nico Robin (One Piece)"
]


import question as s




def game(name):


    print()
    print(f"Welcome to the waifu game, {name}!")
    print("You have to earn coin to summon your waifu!\nJust answer questions and earn coin!\n")

    class Waifu:

        def __init__(self, name, save_path):
            self.name = name
            self.save_path = save_path
            self.coin = 0
            self.xp = 0
            self.p_xp = 0
            self.level = 1
            self.waifus = []
            self.xp_divide = 200

        def load_data(self):                      # ======= load method ======== #
            with open(self.save_path, "r") as file:
                data = json.load(file)
            self.coin = data["coins"]
            self.xp = data["xp"]
            self.p_xp = data["p_xp"]
            self.level = data["level"]
            self.waifus = data["waifus"]
            self.xp_divide = data["xp_divide"]


        def save_data(self):
            with open(self.save_path, 'r') as file:
                data = json.load(file)
            data["coins"] = self.coin
            data["xp"] = self.xp
            data["p_xp"] = self.p_xp
            data["level"] = self.level
            data["waifus"] = self.waifus
            data["xp_divide"] = self.xp_divide
            with open(self.save_path, 'w') as file:
                json.dump(data, file, indent=2)


        def question(self):                     # ======= question method ======== #

            q_r = random.choice([s.questions, s.questions1])
            q = random.choice(q_r)
            user_ans = input(q["q"] + "\n: ").lower()

            if user_ans == q["answer"]:
                spin = random.randint(1, 20)
                if spin in (7, 11, 17):
                    coin = 220
                    xp = 100
                else:
                    coin = 80
                    xp = 40
                print(f"Correct! You got {coin} coins~ 💰")
                print(f"+{xp} xp")
                system.level_xp()
                self.coin += coin
                self.xp += xp
                self.p_xp += xp
            else:        
                print("Wrong! Try again~\n")
        

        def show_coin(self):                           # ======= show_coin method ======== #
            print(f"Coin: {self.coin}\n")
        
        def summon_rare_waifu(self):                   # ======= summon_rare_waifu method ======== #
            cost = 80
            xp = 90
            
            r_waifu = random.choice(rare_waifus)
            print()
            print(f"✨ Summoning waifu... ✨")
            time.sleep(2)
            print(f"💘 Congratulations! {r_waifu} has joined your harem~ ❤️")

            if r_waifu in self.waifus:
                print(f"Seems like you already have {r_waifu}") 
                print(f"There is your {cost} coin back")
            else:
                print(f"+{xp} xp")
                time.sleep(1)
                self.coin -= cost
                self.xp += xp
                self.p_xp += xp
                self.waifus.append(r_waifu)
                system.level_xp()                    
               

    
        def summon_legendary_waifu(self):         # ======= summon_legendary_waifu method ======== #
            cost = 160
            xp = 180

            l_waifu = random.choice(legendary_waifus)
            print()
            print(f"✨ Summoning waifu... ✨")
            time.sleep(2)
            print(f"💘 Congratulations! {l_waifu} has joined your harem~ ❤️")
            
            if l_waifu in self.waifus:
                print(f"Seems like you already have {l_waifu}") 
                print(f"There is your {cost} coin back\n")    
            else:
                print(f"+{xp} xp")          
                time.sleep(1)
                self.coin -= cost
                self.xp += xp
                self.p_xp += xp
                self.waifus.append(l_waifu)
                system.level_xp()                   



        def show_waifus(self):
            if not self.waifus:
                print("No waifus yet... so lonely 😭. Try summoning some waifus!\n")
            else:
                print()
                print(f"{name}s collected waifus:")
                for i, w in enumerate(self.waifus, start=1):
                    print(f"{i}. {w.strip()}")
                print()
        

        def level_xp(self):                                    # ======= Level and xp method ======== #
            leveled_up = False
            while self.xp >= self.xp_divide:
                self.xp -= self.xp_divide
                self.level += 1
                self.xp_divide += 100
                print(f"🎉 Level up! Now you are level {self.level}!")
                leveled_up = True
            
            if leveled_up:
                self.save_data()
            print()

        def user_interface(self):          # ======= User_interface method ======== #
            while True:
                system.save_data()
                print("Chose an action!")
                print("1. Question.")
                print("2. Show coin.")
                print("3. Summon waifu.")
                print("4. See my waifus.")
                print("5. Quit.")
                user = input("Enter your choice: ").lower().strip()
                print()

                if user == "i love hina":
                    print("Ara~ You really love me that much, onii-chan? ❤️\nI'll give you some coins as a reward~ tehe~ 💕")
                    system.xp_coin_cheat()
                    system.level_xp()

                elif user == "clearj99":
                    system.json_clear()
                
                elif user == "xpinc":
                    system.xp_inc()
                    system.level_xp()



                elif user in ["1", "question"]:
                    system.question()

                elif user in ["2", "show coin"]:
                    system.show_coin() 

                elif user in ["3", "summon", "summon waifu"]:
                    print()

                    print("Where do you want to pull?")
                    print("1. Summon Rare waifu.") 
                    print("2. Summon Legendary waifu.")
                    sy = input("Enter your choice between 1 to 2: ").lower()
                    print()
                    if sy == "1": 
                        print("1: 1 pull for 80 coin.")
                        print("2: 10 pull for 800 coin.")
                        ak = input("Chose an option: ")
                        print()
                        if ak == "1":
                            cost = 80
                            if self.coin >= cost:
                                system.summon_rare_waifu()
                            else:
                                print("Not enough coin!\n")
                        elif ak == "2":
                            cost = 800
                            if self.coin >= 800:
                                for i in range(1, 11):
                                    system.summon_rare_waifu()
                            else:
                                print("Not enough coin!\n")
                        else:
                            print("Chose 1 or 2!")
                            print()
                    elif sy == "2": 
                        print("1: 1 pull for 160 coin.")
                        print("2: 10 pull for 1600 coin.")
                        ak = input("Chose an option: ")
                        print()
                        if ak == "1":
                            cost = 160
                            if self.coin >= cost:
                                system.summon_legendary_waifu()
                            else:
                                print("Not enough coin!\n")
                        elif ak == "2":
                            cost = 1600
                            if self.coin >= cost:
                                for i in range(1, 11):
                                    system.summon_legendary_waifu()
                            else:
                                print("Not enough coin!\n")
                                
                    else:
                        print("Please, choose between 1 or 2! ")
                        print()

                elif user in ["4", "See my waifus"]:
                    system.show_waifus()

                elif user in ["5", "quit"]:
                    print("Thanks for playing the Waifu game! Goodbye!")
                    break

                else:
                    print("Invalid input! Please try again.")

        # =================================== dev test side =================================== #
        def xp_coin_cheat(self):
            self.coin += 99999
            self.xp += 99999
            self.p_xp += 99999

        def json_clear(self):
            data = {"player": self.name, "coins": 0, "xp": 0, "p_xp": 0, "level": 1, "waifus": [], "xp_divide": 200}
            with open(self.save_path, 'w') as file:
                json.dump(data, file, indent=2)
            self.coin = 0
            self.xp = 0
            self.p_xp = 0
            self.level = 1
            self.waifus = []
            self.xp_divide = 200
        
        def xp_inc(self):
            try:
                n = int(input("Enter: "))
                self.xp += n
                self.p_xp += n
            except ValueError:
                print("Please enter a valid number!")

        # =================================== dev test side =================================== #



    system = Waifu(name, save_path)
    system.load_data()
    system.user_interface()



current_folder = Path(__file__).resolve().parent
save_path = Path(current_folder) / "game_save.json"
if not Path(save_path).exists():
    while True:
        user_name = input("What is your name: ").lower()
        if 3 <= len(user_name) <= 10:
            break
        else:
            print("Your name should be between 3 to 10 characters!")
    with open(save_path, 'w') as f:
        data = {"player": user_name, "coins": 0, "xp": 0, "p_xp": 0, "level": 1, "waifus": [], "xp_divide": 200}    # ========== Json Format ==========
        json.dump(data, f, indent=2)
    game(user_name)

elif Path(save_path).stat().st_size == 0:
    while True:
        user_name = input("What is your name: ").lower()
        if 3 <= len(user_name) <= 10:
            break
        else:
            print("Your name should be between 3 to 10 characters!")
    with open(save_path, 'w') as f:
        data = {"player": user_name, "coins": 0, "xp": 0, "p_xp": 0, "level": 1, "waifus": [], "xp_divide": 200}    # ========== Json Format ==========
        json.dump(data, f, indent=2)
    game(user_name)

else:
    with open(save_path, 'r') as f:
        data = json.load(f)
        game(data['player'])