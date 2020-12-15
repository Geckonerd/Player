class Player:
    def __init__(self, PName, CName):
        self.PName = PName
        self.CName = CName

f = open("player.txt", "w")
f.write("Player, Character")
f.close

option = None
while option != "3":
    print("1) Create new Player and write to file")
    print("2) Read file")
    print("3) Read file and exit")
    option = input("> ")
    if option == "1":
        PlayerName = input("Input player name: ")
        CharacterName = input("Input character name: ")
        player = Player(PlayerName, CharacterName)

        f = open("player.txt", "a")
        f.write("\n" + player.PName + ", " + player.CName)
        f.close()
        del player
    
    elif option == "2":
        print()
        f = open("player.txt")
        print(f.read())
        f.close()
    
    print()

f = open("player.txt")
print(f.read())
f.close()