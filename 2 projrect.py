import time
import random
import json

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


rare_waifus = [
    "nezuko", "nezuko kamado", "emilia", "rem", "yor", "yor forger",
    "robin", "nami", "akeno", "akeno himejima", "rias", "rias gremory",
    "mitsuri", "mitsuri kanroji", "mio", "mio naruse", "tohka", 
    "tohka yatogami", "kurumi", "kurumi tokisaki", "astolfo", "mordred",
    "saber", "rin tohsaka", "esdeath", "akame", "erza", "erza scarlet",
    "boa hancock", "lucy heartfilia", "shinobu kocho", "kanao tsuyuri",
    "ilyasviel", "nino", "itsuki"
]


legendary_waifus = [
    "hinata", "hinata hyuga", "asuna", "asuna yuuki", "mikasa", "mikasa ackerman",
    "zero two", "makima", "anzu hanashiro", "orihime", "aneko", "tomori", 
    "miku nakano", "asuna goddess", "hina sama"
]


questions = [
    {"q": "Who is best?\n1. Hinata\n2. Sakura", "answer": "1"},
    {"q": "Who's cooler?\n1. Itachi\n2. Sasuke", "answer": "1"},
    {"q": "Cutest demon girl?\n1. Nezuko\n2. Esdeath", "answer": "1"},
    {"q": "Most elegant?\n1. Aqua\n2. Yor Forger", "answer": "2"},
    {"q": "Who would win in a fight?\n1. Mikasa\n2. Rem", "answer": "1"},
    {"q": "Which waifu has pink hair?\n1. Mikasa\n2. Zero Two", "answer": "2"},
    {"q": "Who deserves more love?\n1. Orihime\n2. Sakura", "answer": "1"},
    {"q": "Best 'useless' waifu?\n1. Aqua\n2. Sakura", "answer": "1"},
    {"q": "Who has big chest?\n1. Nami\n2. T.Sunade", "answer": "2"}                    
]



def game():
    user_name = input("What is your name: ").lower()



    if 3 <= len(user_name) <= 10:

        print()
        print(f"Welcome to the waifu game, {user_name}!")
        print("You have to earn coin to summon your waifu!\nJust answer questions and earn coin!\n")

        class Waifu:

            def __init__(self, owner, coin = 0):
                self.owner = owner
                self.coin = coin
                # self.waifus = []
            
            def lod_coin(self):
                with open("game_save.json", "r") as file:
                    coin = json.load(file)
                self.coin = coin["coins"]


            def question(self):

                q = random.choice(questions)
                user_ans = input(q["q"] + "\n: ").lower()

                if user_ans == q["answer"]:
                    print("Correct! You got 10 coins~ 💰\n")
                    with open("game_save.json", "r") as file:
                        data = json.load(file)
                    data["coins"] += 10
                    self.coin += 10
                    with open("game_save.json", "w") as file:
                        json.dump(data, file, indent=2)
                else:        
                    print("Wrong! Try again~\n")
            

            def show_coin(self):
                with open("game_save.json", "r") as file:
                    coins = json.load(file)
                print(f"Coin: {coins['coins']}\n")


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
                    with open("game_save.json", "r") as file:
                        data = json.load(file)
                    data["coins"] = self.coin
                    data["waifus"].append(c_waifu)
                    with open("game_save.json", "w") as file:
                        json.dump(data, file, indent=2)
                    # with open("2_waifus.txt", "a") as file:
                    #     file.write(f"{c_waifu}\n")
                    # self.waifus.append(c_waifu)
                else:
                    print("Not enough coin!")

            
            def summon_rare_waifu(self):
                cost = 30
                if self.coin >= cost:
                    r_waifu = random.choice(rare_waifus)
                    print()
                    print(f"✨ Summoning waifu... ✨")
                    time.sleep(2)
                    print(f"💘 Congratulations! {r_waifu} has joined your harem~ ❤️")
                    print()
                    time.sleep(1)
                    self.coin -= cost
                    with open("game_save.json", "r") as file:
                        data = json.load(file)
                    data["coins"] = self.coin
                    data["waifus"].append(r_waifu)
                    with open("game_save.json", "w") as file:
                        json.dump(data, file, indent=2)                    
                    # with open("2_waifus.txt", "a") as file:
                    #     file.write(f"{r_waifu}\n")                    
                    # self.waifus.append(r_waifu)
                else:
                    print("Not enough coin!")                

        
            def summon_legendary_waifu(self):
                cost = 80
                if self.coin >= cost:
                    l_waifu = random.choice(legendary_waifus)
                    print()
                    print(f"✨ Summoning waifu... ✨")
                    time.sleep(2)
                    print(f"💘 Congratulations! {l_waifu} has joined your harem~ ❤️")
                    print()
                    time.sleep(1)
                    self.coin -= cost
                    with open("game_save.json", "r") as file:
                        data = json.load(file)
                    data["coins"] = self.coin
                    data["waifus"].append(l_waifu)
                    with open("game_save.json", "w") as file:
                        json.dump(data, file, indent=2)                    
                    # with open("2_waifus.txt", "a") as file:
                    #     file.write(f"{l_waifu}\n")                    
                    # self.waifus.append(l_waifu)
                else:
                    print("Not enough coin!")


            def show_waifus(self):
                with open("game_save.json", "r") as file:
                    data = json.load(file)
                    if not data["waifus"]:
                        print("No waifus yet... so lonely 😭. Try summoning some waifus!")
                    else:
                        print()
                        print(f"{user_name}s collected waifus:")
                        for i, w in enumerate(data["waifus"], start = 1):
                            print(f"{i}. {w.strip()}")
                        print()

        # system = Waifu(user_name)
            def user_interface(self):
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
                        with open("game_save.json", "r") as file:
                            data = json.load(file)
                        data["coins"] += 500
                        self.coin = data["coins"]
                        # coin += 500
                        with open("game_save.json", "w") as file:
                            json.dump(data, file, indent=2)
                        # self.coin = coin
                        print("Ara~ You really love me that much, onii-chan? ❤️\nI'll give you some coins as a reward~ tehe~ 💕\n")


                    elif user in ["1", "question"]:
                        system.question()

                    elif user in ["2", "show coin"]:
                        system.show_coin() 

                    elif user in ["3", "summon", "summon waifu"]:
                        print()

                        print("Where do you want to spin?")
                        print("1. Common for 10 coin.")
                        print("2. Rare for 30 coin.")
                        print("3. Legendary for 80 coin.")
                        sy = input("Enter your choice between 1 to 3: ").lower()
                        if sy == "1":
                            system.summon_common_waifu()
                        elif sy == "2":
                            system.summon_rare_waifu()
                        elif sy == "3":
                            system.summon_legendary_waifu()
                        else:
                            print("Please, choose between 1 to 3! ")

                    elif user in ["4", "see my waifus"]:
                        system.show_waifus()

                    elif user in ["5", "quit"]:
                        print("Thanks for playing the Waifu game! Goodbye!")
                        break

                    else:
                        print("Invalid input! Please try again.")
        
        system = Waifu(user_name)
        system.lod_coin()
        system.user_interface()



    else:
        print("Your name should be between 3 to 10 characters!")

game()