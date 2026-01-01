import time
import random
import json
import os


# =========================== Unnecessary# =========================== #
common_waifus = [
    "sakura", "sakura matou", "kanao", "shouko", "yui", "megumin",
    "aqua", "darkness", "lalatina", "itsuki", "yotsuba", "ichika",
    "miku", "nino", "rin", "illya", "mine", "leone", "sheele",
    "lucy", "lucy heartfilia", "jibril", "schwi", "schwi dola",
    "yui yuigahama", "shiro", "mashiro", "mashiro shiina", 
    "shinobu", "taiga", "taiga aisaka", "mai", "mai sakurajima", 
    "yukino", "yukino yukinoshita", "kaguya", "kaguya shinomiya",
    "chika", "chika fujiwara", "hestia", "raphtalia"
]
# =========================== Unnecessary# =========================== #

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

        def __init__(self, owner):
            self.owner = owner
            self.coin = 0
            # self.waifus = []
        
        def lod_coin(self):                      # ======= load method ======== #
            with open(save_path, "r") as file:
                coin = json.load(file)
            self.coin = coin["coins"]


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
                # print(spin)
                print(f"Correct! You got {coin} coins~ 💰")
                print(f"+{xp} xp")
                with open(save_path, "r") as file:
                    data = json.load(file)
                data["coins"] += coin
                data["xp"] += xp
                self.coin += coin
                with open(save_path, "w") as file:
                    json.dump(data, file, indent=2)
                system.level()
            else:        
                print("Wrong! Try again~\n")
        

        def show_coin(self):                           # ======= show_coin method ======== #
            with open(save_path, "r") as file:
                coins = json.load(file)
            print(f"Coin: {coins['coins']}\n")

# =========================== Unnecessary# =========================== #
        def summon_common_waifu(self):
            cost = 10
            if self.coin >= cost:
                c_waifu = random.choice(common_waifus)
                print()
                print(f"✨ Summoning waifu... ✨")
                time.sleep(2)
                print(f"💘 Congratulations! {c_waifu} has joined your harem~ ❤️")
                print()
                time.sleep(1)
                self.coin -= cost
                with open(save_path, "r") as file:
                    data = json.load(file)
                data["coins"] = self.coin
                data["waifus"].append(c_waifu)
                with open(save_path, "w") as file:
                    json.dump(data, file, indent=2)
            else:
                print("Not enough coin!")
# =========================== Unnecessary# =========================== #
        
        def summon_rare_waifu(self):                   # ======= summon_rare_waifu method ======== #
            cost = 80
            xp = 90
            
            r_waifu = random.choice(rare_waifus)
            print()
            print(f"✨ Summoning waifu... ✨")
            time.sleep(2)
            print(f"💘 Congratulations! {r_waifu} has joined your harem~ ❤️")
            
            with open(save_path, "r") as file:
                data = json.load(file)
                if r_waifu in data["waifus"]:
                    print(f"Seems like you already have {r_waifu}") 
                    print(f"There is your {cost} coin back")
                else:
                    print(f"+{xp} xp")
                    time.sleep(1)
                    self.coin -= cost
                    with open(save_path, "r") as file:
                        data = json.load(file)
                    data["coins"] = self.coin
                    data["waifus"].append(r_waifu)
                    data["xp"] += xp
                    with open(save_path, "w") as file:
                        json.dump(data, file, indent=2)
                    system.level()                    
               

    
        def summon_legendary_waifu(self):         # ======= summon_legendary_waifu method ======== #
            cost = 160
            xp = 180

            l_waifu = random.choice(legendary_waifus)
            print()
            print(f"✨ Summoning waifu... ✨")
            time.sleep(2)
            print(f"💘 Congratulations! {l_waifu} has joined your harem~ ❤️")
            
            with open(save_path, "r") as file:
                data = json.load(file)
                if l_waifu in data["waifus"]:
                    print(f"Seems like you already have {l_waifu}") 
                    print(f"There is your {cost} coin back\n")    
                else:
                    print(f"+{xp} xp")          
                    time.sleep(1)
                    self.coin -= cost
                    with open(save_path, "r") as file:
                        data = json.load(file)
                    data["coins"] = self.coin
                    data["waifus"].append(l_waifu)
                    data["xp"] += xp
                    with open(save_path, "w") as file:
                        json.dump(data, file, indent=2) 
                    system.level()                   



        def show_waifus(self):
            with open(save_path, "r") as file:
                data = json.load(file)
                if not data["waifus"]:
                    print("No waifus yet... so lonely 😭. Try summoning some waifus!\n")
                else:
                    print()
                    print(f"{name}s collected waifus:")
                    for i, w in enumerate(data["waifus"], start = 1):
                        print(f"{i}. {w.strip()}")
                    print()
        

        def level(self):                                    # ======= Leve and xp method ======== #
            with open(save_path, 'r') as file:
                data = json.load(file)
            current_level = data["level"]
            new_level = max(1, min(15, data["xp"] // 200) + 1)
            if new_level > current_level:
                print(f"Level {new_level}")
            data["level"] = new_level
            with open(save_path, 'w') as file:
                json.dump(data, file, indent=2)
            print()

    # system = Waifu(user_name)
        def user_interface(self):          # ======= user_interface method ======== #
            while True:
                print("Chose an action!")
                print("1. Question.")
                print("2. Show coin.")
                print("3. Summon waifu.")
                print("4. See my waifus.")
                print("5. Quit.")
                user = input("Enter your choice: ").lower().strip()
                print()

                if user == "i love hina":
                    with open(save_path, "r") as file:
                        data = json.load(file)
                    data["coins"] += 500
                    data["xp"] += 100
                    self.coin = data["coins"]
                    # coin += 500
                    with open(save_path, "w") as file:
                        json.dump(data, file, indent=2)
                    # self.coin = coin
                    print("Ara~ You really love me that much, onii-chan? ❤️\nI'll give you some coins as a reward~ tehe~ 💕")
                    system.level()


                elif user in ["1", "question"]:
                    system.question()

                elif user in ["2", "show coin"]:
                    system.show_coin() 

                elif user in ["3", "summon", "summon waifu"]:
                    print()

                    print("Where do you want to pull?")
                    print("1. Summon Rare waifu.") ##################
                    print("2. Summon Legendary waifu.")
                    sy = input("Enter your choice between 1 to 2: ").lower()
                    print()
                    if sy == "1": ###############
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
                    elif sy == "2": ############
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
                        print() ########

                elif user in ["4", "See my waifus"]:
                    system.show_waifus()

                elif user in ["5", "quit"]:
                    print("Thanks for playing the Waifu game! Goodbye!")
                    break

                else:
                    print("Invalid input! Please try again.")
    
    system = Waifu(name)
    system.lod_coin()
    system.user_interface()




current_folder = os.path.dirname(__file__)
save_path = os.path.join(current_folder, "game_save.json")
if not os.path.exists(save_path):
    while True:
        user_name = input("What is your name: ").lower()
        if 3 <= len(user_name) <= 10:
            break
        else:
            print("Your name should be between 3 to 10 characters!")
    with open(save_path, 'w') as f:
        data = {"player": user_name, "coins": 0, "xp": 0, "level": 1, "waifus": []}    # ========== Json Format ==========
        json.dump(data, f, indent=2)
        time.sleep(2)
    game(user_name)
else:
    with open(save_path, 'r') as f:
        data = json.load(f)
        game(data['player'])